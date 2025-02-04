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
        Berdasarkan niche {self.niche}, buatkan 5 ide video singkat 1 menit dalam bahasa Indonesia untuk YouTube Shorts dan TikTok yang menarik, kreatif, inovatif, edukatif, serta mudah di mengerti dan sangat mungkin viral untuk audiens {self.target_audiens} dalam format JSON.
                
        Judul harus:
        - sesuai denganj niche yang Akurat, menarik, dan memberikan rasa penasaran. Judul harus memberi gambaran singkat tentang niche. jangan berikan Judul yang menyesatkan .
        - Bangkitkan Rasa Penasaran. Buat penonton penasaran dengan isi video. Ajukan pertanyaan atau gunakan kata sifat yang menarik. Tujuannya adalah membuat mereka berhenti scroll dan mulai menonton.
        - Gunakan Kata Kunci yang Relevan. Ya, ini tentang SEO (search engine optimization) untuk Shorts youtube dan tiktok. Sisipkan kata kunci yang relevan dengan konten dan pencarian audiens. Namun, ingat: meski kata kunci penting, itu bukan segalanya.
        - Buatlah Judul yang Singkat dan Menarik. Anda hanya punya 50 - 100 karakter sebelum YouTube memotong judulnya (saat dilihat di aplikasi). Jadi, perhatikan batas karakter. Judul harus impactful dan terlihat utuh agar menarik perhatian.
        
        Deskripsi harus:
        - Maksimal 5000 Karakter. Deskripsi harus menjelaskan detail tentang isi video berdasarkan niche.
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
                    if not isinstance(result, list):
                        idea = result["Ideas"][pilihan]
                    else:
                        idea = result[pilihan]

                    df_ideas = pd.DataFrame([idea])
                    # export to excel
                    df_ideas.to_excel("output/idea.xlsx", index=False)

                    self.judul = idea["judul"]
                    self.deskripsi = idea["deskripsi"]

                    self.durasi = input("Masukkan durasi video: ")
                    self.jumlah_scene = input("Masukkan jumlah scene: ")

                    self.generate_script_video(pilihan + 1)

        except Exception as e:
            print(f"Terjadi kesalahan di generate_ideas: {e}")

    def generate_script_video(self, pilihan):
        console.print("============================================================")
        console.print(f"Generate Script untuk judul: {self.judul}")

        # Prompt to generate Script
        prompt = f"""
        Berdasarkan nomor {pilihan}, buatkan sebuah script video untuk YouTube Shorts dan TikTok yang menarik, kreatif, inovatif, edukatif, serta mudah di mengerti dan sangat mungkin viral untuk audiens {self.durasi} dengan jumlah scene {self.jumlah_scene}. 
        
        Script harus memperhatikan hal-hal dibawah ini:
        1. Kenali Audiens Anda
        Sebelum mulai menulis, penting untuk mengetahui siapa audiens target Anda. Pertimbangkan faktor-faktor seperti usia, minat, dan kebiasaan menonton mereka. Dengan memahami audiens Anda, Anda dapat menyesuaikan gaya bahasa dan konten agar lebih relevan dan menarik perhatian mereka.

        2. Tentukan Tujuan Video
        Setiap video harus memiliki tujuan dan penjelasan yang jelas, apakah itu untuk mengedukasi, menghibur, atau mempromosikan produk tertentu. Tentukan apa yang ingin Anda capai melalui video tersebut sehingga semua elemen dalam script mendukung tujuan tersebut.
    
        3. Buat Outline Awal
        Sebelum menulis detailnya, buatlah outline awal dari isi video Anda. Ini bisa berupa poin-poin utama atau alur cerita sederhana. Outline ini akan membantu menjaga fokus saat menulis dan memastikan bahwa semua informasi penting tersampaikan.

        4. Buat Detail Tujuan beserta detail deskripsi script
        beruikan tujuan detail tentang script yang akan dibuat, serta desktipsi lengkap tentang isi script secara menarik, komunikatif, edukatif dan mudah dimengerti, untuk menarik minat audience.

        5. Mulai dengan Hook Menarik
        Awali script dengan kalimat pembuka atau hook (3-5 detik) yang mampu menarik perhatian penonton sejak detik pertama. Hook ini bisa berupa pertanyaan provokatif, fakta mengejutkan, atau pernyataan menarik lainnya yang mendorong penonton untuk terus menonton.

        6. Sertakan Konten Utama
        Setelah hook, lanjutkan dengan menyampaikan konten utama secara ringkas namun padat informasi. Usahakan setiap kalimat memiliki nilai tambah bagi penonton tanpa membuang waktu pada hal-hal tidak perlu. Cantumkan juga beberapa fakta dan source mengenai isi konten secara singkat dan detail.

        7. Gunakan Bahasa Sederhana dan Jelas
        Karena durasi terbatas pada YouTube Shorts, penggunaan bahasa sederhana sangat dianjurkan agar pesan tersampaikan dengan jelas dan cepat dipahami oleh audiens dari berbagai latar belakang.

        8. Akhiri dengan Call to Action (CTA)
        Tutup video dengan call to action (CTA) yang kuat sehingga mendorong penonton melakukan sesuatu setelah menonton—baik itu like video, subscribe channel Anda, atau berkomentar di bawah video.
        
        Scene terdiri dari:
        1. Durasi
            Durasi harus sesuai dengan durasi video. Memperlihatkan dari detik ke detik.
        2. Visual
            Visual harus menggambarkan secara detail dari tiap scene. visual Hanya berupa gambar yang sesuai dengan scene yang telah ditentukan dan bisa terdiri dari beberapa visual yang menggambarkan scene. Hindari visual yang terlalu berlebih dan melenceng dari scene. Berikan visual dalam bentuk ilustrasi terbaik, sesuai dengan detail scene.
        3. Narasi
            Panjang narasi harus menyesuaikan dengan durasi scene, harus sesuai dengan detail scene, dan sesuaikan waktu narasi dengan waktu scene. buat dengan sangat detail.
        4. Prompt text to image
            Prompt text to image harus sesuai dengan seluruh scene visual. Prompt ini menjelaskan gambar dengan sangat detail, berupa subject ilustrasi, detail background yang sesuai dengan scene, serta tambahan beberapa ornamen menarik sesuai dengan scene. buatkan image dalam bentuk ilustrasi 3d, atau ilustrasi 4d yang sesuai dengan detail setiap scene.
        5. Text in screen
            buatkan text sesuai dengan detail narasi per scene atau sesuai dengan isi narasi per secene. buatkan dalam font yang sesuai dengan scene, berikan sedikit efek agar tulisan lebih menarik untuk dibaca oleh audience. Jika perlu, berikan huruf kapital dalam salah satu kalimat jika terdapat kalimat yang mengandung unsur edukasi.
        
        Gunakan skema JSON ini:
        Script = {{'durasi': str, 'visual': list[str], 'narasi': str, 'prompt text to image': list[str], 'text in screen': str}}
        Return: list[{{ scene_x: Script }}]
        
        KAMU HARUS: Hanya berikan JSON, tidak ada respon lain sekarang!!
        """
        try:
            response = self.Ai(prompt)
            result = json.loads(response)
            console.print("")
            console.print(f"Hasil script untuk judul: {self.judul}")
            console.print(result)

            pilihan = input("Apakah script ini sesuai? (y/n): ")
            if pilihan == "n":
                self.generate_script_video()
            else:
                script = result
                df_script = pd.DataFrame(script)
                # export to excel
                df_script.to_excel("output/script.xlsx", index=False)

        except Exception as e:
            print(f"Terjadi kesalahan di generate_script: {e}")

    def generate_script(self):
        self.niche = input("Masukkan niche video yang ingin dibuat: ")
        self.target_audiens = input("Masukkan target audiens: ")

        self.generate_ideas()
