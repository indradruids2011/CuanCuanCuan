# Prompt to generate Script
prompt = f"""
Berdasarkan judul {self.judul}, buatkan sebuah script video untuk YouTube Shorts dan TikTok yang menarik dan sangat mungkin viral untuk durasi maksimal {self.durasi} dengan jumlah scene {self.jumlah_scene}. 
Script harus memperhatikan hal-hal dibawah ini:

- Menentukan Tujuan Video
    Sebelum mulai menulis naskah, pahami tujuan yang ingin dicapai. Misalnya, tujuan kami adalah menampilkan latihan perut efektif yang bisa dilakukan di rumah. Target audiensnya adalah orang yang ingin meningkatkan kebugaran fisik dan mencari latihan cepat serta efektif.

- Struktur Naskah
    Naskah untuk video pendek harus terdiri dari tiga komponen utama:

    Pengantar yang Menarik (0-5 detik): Tujuan bagian ini adalah memikat perhatian penonton sejak detik pertama. Contoh: judul menarik, pertanyaan menggelitik, atau pernyataan kuat.

    Konten Utama (5-50 detik): Sajikan informasi utama dengan jelas dan singkat. Gunakan visual untuk memperkuat penjelasan teknik latihan.

    Penutup yang Kuat (50-60 detik): Akhiri dengan ajakan bertindak (misalnya, ajakan berlangganan, memberi like, atau berkomentar).

- Pengantar yang Menarik
    Contoh kalimat pembuka:
    "Ingin perut rata hanya dalam 10 menit sehari? Ini tiga latihan perut paling efektif!"

    Tips Memikat Perhatian:
        Visual Mencolok: Gunakan gambar dinamis dan berwarna.
        Awal yang Energik: Mulai dengan musik atau efek suara yang semangat.
        Pertanyaan Provokatif: Misalnya, "Siap membentuk perut ideal?"
        
- Konten Utama
    Contoh konten untuk video latihan:
        Plank (5-20 detik): "Posisi plank! Jaga punggung lurus, kencangkan perut. Tahan 30 detik."
        Crunches (20-35 detik): "Telentang, angkat tubuh atas tanpa mengangkat punggung bawah. Lakukan 15 kali."
        Gerakan Sepeda (35-50 detik): "Angkat kaki dan gerakkan seperti mengayuh sepeda. Lakukan 30 detik."
        
    Tips Menjaga Perhatian:
        - Instruksi jelas dan demonstrasi dari berbagai sudut.
        - Tambahkan timer atau hitungan mundur.
        
- Penutup yang Kuat
    Contoh:
        "Jika latihan ini bermanfaat, tekan tombol suka dan subscribe untuk konten serupa!"

    Tips Penutup:
        - Sertakan ajakan bertindak spesifik.
        - Ucapkan terima kasih.
        - Rekomendasikan video lain.

- Gaya dan Nada
    Gunakan gaya energik dan motivasional untuk video latihan. Contoh:
    "Siap bekerja keras? Ayo mulai sekarang!"

    Tips:
        - Bicaralah dengan antusias.
        - Pertahankan nada positif.
        - Sapa penonton secara langsung (misalnya, "Kalian pasti bisa!").

- Storyboard
    Contoh alur visual:
        1. Pembawa acara memperkenalkan diri dan melontarkan pertanyaan.
        2. Demonstrasi plank.
        3. Demonstrasi crunches.
        4. Demonstrasi gerakan sepeda.
        5. Ajakan berlangganan.

    Tips Storyboard:
        - Gunakan sudut kamera berbeda untuk dinamika.
        - Tambahkan teks atau grafik penjelas.

- Menambahkan Emosi dan Interaktivitas
    Contoh:
        "Rasakan ototmu bekerja! Latihan rutin akan membuahkan hasil."

    Tips:
        - Ekspresi wajah dan gestur yang ekspresif.
        - Libatkan penonton dengan pertanyaan (misalnya, "Sudah coba latihan ini?").


Setiap script harus memiliki:        
Hook (mengandung kata kunci dan memicu rasa penasaran).
CTA (mengandung kata kunci dan memicu rasa penasaran).
Prompt text to image (Jelaskan dengan sangat detail baik subject, background, dan style).

Gunakan skema JSON ini:
Script = {{'durasi': str, 'visual': str, 'narasi': str, 'prompt': str, 'text in screen': str}}
Return: list[{{ scene_x: Script }}]

KAMU HARUS: Hanya berikan JSON, tidak ada respon lain sekarang!! 
"""


# Prompt to generate Script
prompt = f"""
Berdasarkan nomor {pilihan}, buatkan sebuah script video untuk YouTube Shorts dan TikTok yang menarik dan sangat mungkin viral untuk durasi maksimal {self.durasi} dengan jumlah scene {self.jumlah_scene}. 

Script harus memperhatikan hal-hal dibawah ini:
1. Kenali Audiens Anda
Sebelum mulai menulis, penting untuk mengetahui siapa audiens target Anda. Pertimbangkan faktor-faktor seperti usia, minat, dan kebiasaan menonton mereka. Dengan memahami audiens Anda, Anda dapat menyesuaikan gaya bahasa dan konten agar lebih relevan dan menarik perhatian mereka.

2. Tentukan Tujuan Video
Setiap video harus memiliki tujuan yang jelas, apakah itu untuk mengedukasi, menghibur, atau mempromosikan produk tertentu. Tentukan apa yang ingin Anda capai melalui video tersebut sehingga semua elemen dalam script mendukung tujuan tersebut.

3. Buat Outline Awal
Sebelum menulis detailnya, buatlah outline awal dari isi video Anda. Ini bisa berupa poin-poin utama atau alur cerita sederhana. Outline ini akan membantu menjaga fokus saat menulis dan memastikan bahwa semua informasi penting tersampaikan.

4. Mulai dengan Hook Menarik
Awali script dengan kalimat pembuka atau hook yang mampu menarik perhatian penonton sejak detik pertama. Hook ini bisa berupa pertanyaan provokatif, fakta mengejutkan, atau pernyataan menarik lainnya yang mendorong penonton untuk terus menonton.

5. Sertakan Konten Utama
Setelah hook, lanjutkan dengan menyampaikan konten utama secara ringkas namun padat informasi. Usahakan setiap kalimat memiliki nilai tambah bagi penonton tanpa membuang waktu pada hal-hal tidak perlu.       

6. Gunakan Bahasa Sederhana dan Jelas
Karena durasi terbatas pada YouTube Shorts, penggunaan bahasa sederhana sangat dianjurkan agar pesan tersampaikan dengan jelas dan cepat dipahami oleh audiens dari berbagai latar belakang.

7. Akhiri dengan Call to Action (CTA)
Tutup video dengan call to action (CTA) yang kuat sehingga mendorong penonton melakukan sesuatu setelah menonton—baik itu like video, subscribe channel Anda, atau berkomentar di bawah video.

Scene terdiri dari:
1. Durasi
    Durasi harus sesuai dengan durasi video. Memperlihatkan dari detik ke detik.
2. Visual
    Visual harus menggambarkan secara detail scene tersebut. Hanya berupa gambar dan bisa terdiri dari beberapa visual yang menggambarkan scene.
3. Narasi
    Panjang narasi harus menyesuaikan dengan durasi scene tersebut.
4. Prompt text to image
    Prompt text to image mengikuti visual, bila visual berupa teks maka tidak diperlukan prompt. Prompt text to image terdiri dari satu kalimat dan bisa lebih dari satu prompt per scene. Prompt ini menjelaskan gambar dengan sangat detail baik subject, background, dan style. Prompt harus sesuai dengan waktu dan lokasi dari script. Untuk style buat agar konsistensi untuk semua scene.
5. Text in screen
    Teks harus menggambarkan scene tersebut.

Gunakan skema JSON ini:
Script = {{'durasi': str, 'visual': list[str], 'narasi': str, 'prompt text to image': list[str], 'text in screen': str}}
Return: list[{{ scene_x: Script }}]

KAMU HARUS: Hanya berikan JSON, tidak ada respon lain sekarang!! 
"""
