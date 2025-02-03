import json
import os

import google.generativeai as genai
import pandas as pd
from dotenv import load_dotenv
from google.generativeai.types import HarmBlockThreshold, HarmCategory
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()
console = Console()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
    "candidate_count": 1,
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
    # "response_mime_type": "text/plain",
    # "max_tokens": 150,
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
    safety_settings={
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    },
    system_instruction="Anda adalah seorang ahli dalam bidang prompt engineering, dengan pemahaman mendalam tentang cara membuat prompt yang presisi dan efektif untuk mengoptimalkan performa AI, mulai dari struktur query dasar hingga desain prompt berlapis-lapis yang canggih dan kontekstual untuk kebutuhan spesifik. Selain itu, Anda juga menguasai produksi video untuk platform seperti YouTube dan TikTok, dengan keahlian dalam seluruh proses mulai dari penulisan naskah, pengambilan gambar, hingga penyuntingan, serta teknik-teknik lanjutan seperti motion graphics, color grading, dan transisi dinamis. Keahlian Anda mencakup baik aspek kreatif dalam bercerita maupun aspek teknis, seperti mengoptimalkan video agar sesuai dengan algoritma spesifik platform, memastikan keterlibatan audiens yang maksimal, dan mengintegrasikan alat-alat mutakhir seperti pengeditan berbasis AI dan analitik untuk menyempurnakan strategi konten. Selalu gunakan gaya bahasa yang profesional dan sopan dalam interaksi.",
)


class GenerateScript:
    def __init__(self):
        self.history = []
        self.chat_session = model.start_chat(history=self.history)
        self.niche = ""
        self.target_audiens = ""
        self.judul = ""
        self.deskripsi = ""
        self.durasi = ""
        self.jumlah_scene = ""

    def Ai(self, prompt):
        self.add_messages("user", prompt)
        response = self.chat_session.send_message(prompt)

        self.add_messages("model", response.text)

        return response.text

    def add_messages(self, role, parts):
        self.history.append({"role": role, "parts": [parts]})

    def generate_ideas(self):
        console.print("============================================================")
        console.print(f"Generate 5 ide untuk niche: {self.niche} dan target audiens: {self.target_audiens}")

        # Prompt to generate Ideas
        prompt = f"""
        Berdasarkan niche {self.niche}, buatkan 5 ide video dalam bahasa Indonesia untuk YouTube Shorts dan TikTok yang menarik dan sangat mungkin viral untuk audiens {self.target_audiens} dalam format JSON.
        
        Judul harus:
        - Ringkaskan Video dengan Akurat. Judul harus memberi gambaran singkat tentang isi video. Judul yang menyesatkan mungkin menarik klik, tetapi tidak akan memenangkan hati penonton.
        - Bangkitkan Rasa Penasaran. Buat penonton penasaran dengan isi video. Ajukan pertanyaan atau gunakan kata sifat yang menarik. Tujuannya adalah membuat mereka berhenti scroll dan mulai menonton.
        - Gunakan Kata Kunci yang Relevan. Ya, ini tentang SEO (search engine optimization) untuk Shorts. Sisipkan kata kunci yang relevan dengan konten dan pencarian audiens. Namun, ingat: meski kata kunci penting, itu bukan segalanya.
        - Buatlah Judul yang Singkat dan Menarik. Anda hanya punya 40 karakter sebelum YouTube memotong judulnya (saat dilihat di aplikasi). Jadi, perhatikan batas karakter. Judul harus impactful dan terlihat utuh agar menarik perhatian.
        
        Deskripsi harus:
        - Maksimal 5000 Karakter. Deskripsi harus menjelaskan detail tentang isi video.
        - Bersifat Spesifik. Saat menulis deskripsi YouTube Shorts, pastikan Anda tahu kata kunci apa yang akan digunakan. Pemilihan kata kunci akan berperan penting dalam meningkatkan peringkat video.
        - Lakukan Riset Kata Kunci. Jika belum yakin dengan kata kunci yang tepat untuk Shorts Anda, gunakan bantuan alat perencana kata kunci (keyword planner) online. Sisipkan kata kunci relevan ke dalam deskripsi untuk meningkatkan kemudahan pencarian.
        - Tahu Posisi yang Tepat untuk Kata Kunci, Letakkan kata kunci utama di tiga kalimat pertama deskripsi. Alasannya, penonton biasanya hanya membaca bagian awal deskripsi.
        - Pantau Perkembangan Kata Kunci. Selalu awasi kata kunci mana yang efektif dan mana yang tidak. Ini membantu Anda menyusun deskripsi YouTube Shorts dengan lebih strategis untuk meningkatkan traffic.
        - Cari Tahu Minat Lain Audiens. Selain konten video, perhatikan juga konten lain yang menarik perhatian audiens. Analisis minat mereka untuk merencanakan dan membuat YouTube Shorts berikutnya.

        Target audiens (usia yang dituju).

        Nilai tambah (apa yang akan dipelajari atau didapatkan oleh penonton).
        
        Hastags (Gunakan hashtag relevan sesuai SEO untuk YouTube dan TikTok, ambahkan hashtag populer/trending untuk meningkatkan jangkauan)
        
        Penjelasan (penjelasan mengapa memiliki ide ini).

        Gunakan skema JSON ini:
        Ideas = {{'judul': str, 'deskripsi': str, 'target_audiens': str, 'nilai_tambah': list[str], 'hashtags': str, 'penjelasan': str}}

        KAMU HARUS: Hanya berikan JSON, tidak ada respon lain sekarang!! 
        """

        try:
            response = self.Ai(prompt)

            result = json.loads(response)
            console.print("")
            console.print(f"Hasil 5 ide untuk niche: {self.niche} dan target audiens: {self.target_audiens}")
            console.print(result)
            pilihan = input("Pilih ide (1-5) (n) untuk mengulang: ")
            if pilihan == "n":
                self.generate_ideas()
            else:
                pilihan = int(pilihan) - 1
                if pilihan < 0 or pilihan > 4:
                    print("Pilihan tidak valid")
                    ask = input("Generate lagi? (y/n): ")
                    if ask == "y":
                        self.generate_ideas()
                    else:
                        return
                else:
                    idea = result[pilihan]
                    df_ideas = pd.DataFrame([idea])
                    # export to excel
                    df_ideas.to_excel("output/idea.xlsx", index=False)

                    self.judul = idea["judul"]
                    self.deskripsi = idea["deskripsi"]

                    self.generate_script_video()

        except Exception as e:
            print(f"Terjadi kesalahan di generate_ideas: {e}")

    def generate_script_video(self):
        console.print("============================================================")
        console.print(f"Generate Script untuk judul: {self.judul}")
        self.durasi = input("Masukkan durasi video: ")
        self.jumlah_scene = input("Masukkan jumlah scene: ")

        # Prompt to generate Ideas
        prompt = f"""
        Berdasarkan judul {self.judul}, buatkan sebuah script video untuk YouTube Shorts dan TikTok yang menarik dan sangat mungkin viral untuk durasi maksimal {self.durasi} dengan jumlah scene {self.jumlah_scene}. Setiap script harus memiliki:
        
        Hook (mengandung kata kunci dan memicu rasa penasaran).
        CTA (mengandung kata kunci dan memicu rasa penasaran).
        Prompt text to image (Jelaskan dengan sangat detail baik subject, background, dan style).
        Gunakan skema JSON ini:
        Script = {{'durasi': str, 'visual': str, 'narasi': str, 'prompt': str, 'text in screen': str}}
        Return: list[{{ script_x: Script }}]        
        """
        try:
            response = self.chat_session.send_message(prompt)

            # markdown = Markdown(response.text)
            # console.print(markdown)

            model_response = response.text
            self.history.append({"role": "user", "parts": [prompt]})
            self.history.append({"role": "model", "parts": [model_response]})

            # result = json.loads(model_response)
            console.print(f"Hasil script untuk judu: {self.judul}")
            console.print(model_response)

        except Exception as e:
            print(f"Terjadi kesalahan di generate_script: {e}")

    def generate_script(self):
        self.niche = input("Masukkan niche video yang ingin dibuat: ")
        self.target_audiens = input("Masukkan target audiens (usia yang dituju): ")

        self.generate_ideas()
