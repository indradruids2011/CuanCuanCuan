import json
import os

import google.generativeai as genai
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
        self.judul = ""

    def generate_ideas(self):
        console.print(f"Menemukan ide untuk niche: {self.niche}")

        # Prompt to generate Ideas
        prompt = f"""
        Berdasarkan niche {self.niche}), buatkan 5 ide video untuk YouTube Shorts dan TikTok yang menarik dan sangat mungkin viral. Setiap ide harus memiliki:

        Judul yang menarik (mengandung kata kunci dan memicu rasa penasaran).

        Deskripsi singkat (1-2 kalimat yang menjelaskan isi video).

        Target audiens (usia yang dituju).

        Nilai tambah (apa yang akan dipelajari atau didapatkan oleh penonton).
        
        Hastags (Gunakan hashtag relevan sesuai SEO untuk YouTube dan TikTok, ambahkan hashtag populer/trending untuk meningkatkan jangkauan)

        Pastikan ide video tersebut belum banyak dibahas oleh kompetitor dan memiliki potensi viral.
        
        Gunakan skema JSON ini:
        Ideas = {{'judul': str, 'deskripsi': str, 'target_audiens': str, 'nilai_tambah': list[str], 'hashtags': str}}
        Return: list[Ideas]
        """
        try:
            response = self.chat_session.send_message(prompt)

            # markdown = Markdown(response.text)
            # console.print(markdown)

            model_response = response.text
            self.history.append({"role": "user", "parts": [prompt]})
            self.history.append({"role": "model", "parts": [model_response]})

            result = json.loads(model_response)
            console.print(f"Hasil 5 ide untuk niche: {self.niche}")
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
                    self.judul = idea["judul"]
                    # deskripsi = idea["deskripsi"]
                    # target_audiens = idea["target_audiens"]
                    # nilai_tambah = idea["nilai_tambah"]
                    # hashtags = idea["hashtags"]

                    # console.print(f"Judul: {self.judul}")
                    # console.print(f"Deskripsi: {deskripsi}")
                    # console.print(f"Target Audiens: {target_audiens}")
                    # console.print(f"Nilai Tambah: {nilai_tambah}")
                    # console.print(f"Hastags: {hashtags}")

                    self.generate_script_video()

        except Exception as e:
            print(f"Terjadi kesalahan di generate_ideas: {e}")

    def generate_script_video(self):
        console.print(f"Menemukan Script untuk judul: {self.judul}")

        # Prompt to generate Ideas
        prompt = f"""
        Berdasarkan judul {self.judul}, buatkan sebuah script video untuk YouTube Shorts dan TikTok yang menarik dan sangat mungkin viral untuk durasi maksimal 3 menit. Setiap script harus memiliki:
        
        Hook (mengandung kata kunci dan memicu rasa penasaran).
        CTA (mengandung kata kunci dan memicu rasa penasaran).
        Prompt text to image (Jelaskan dengan sangat detail baik subject, background, dan style).
        Gunakan skema JSON ini:
        Script = {{'durasi': str, 'visual': str, 'narasi': str, 'prompt': str, 'text in screen': str}}
        Return: list[Script]        
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

    def generate_script(self, niche: str):
        self.niche = niche
        judul = self.generate_ideas()
