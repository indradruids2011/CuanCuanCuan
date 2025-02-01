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
    # "response_mime_type": "application/json",
    "response_mime_type": "text/plain",
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

    def generate_ideas(self):
        console.print(f"Menemukan ide untuk niche: {self.niche}")

        # Prompt to generate Ideas
        prompt = f"""
        Berdasarkan niche {self.niche}), buatkan 5 ide video yang menarik dan sangat mungkin viral. Setiap ide harus memiliki:

        Judul yang menarik (mengandung kata kunci dan memicu rasa penasaran).

        Deskripsi singkat (1-2 kalimat yang menjelaskan isi video).

        Target audiens (usia anak-anak yang dituju).

        Nilai tambah (apa yang akan dipelajari atau didapatkan oleh penonton).

        Pastikan ide video tersebut belum banyak dibahas oleh kompetitor dan memiliki potensi viral.
        """
        try:
            response = self.chat_session.send_message(prompt)

            markdown = Markdown(response.text)
            console.print(markdown)

            model_response = response.text
            self.history.append({"role": "user", "parts": [prompt]})
            self.history.append({"role": "model", "parts": [model_response]})

            console.print(model_response)
        except Exception as e:
            print(f"Terjadi kesalahan di generate_ideas: {e}")

    def generate_script(self, niche: str):
        self.niche = niche
        ideas = self.generate_ideas()
