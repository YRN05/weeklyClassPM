import streamlit as st
import pandas as pd
import altair as alt

# Data Preparation
df = pd.read_csv('data\weekDuaClean.csv')

st.title("Week Two Data Overview")
st.dataframe(df)

st.divider()

# Layout
st.header("About Member")
ch1, ch2 = st.columns(2, border=True)
ch3, ch4 = st.columns(2, border=True)

# University

with ch1:
   
    st.subheader("University")
    df_univ = df['Which university do you attend?'].value_counts().reset_index()
    df_univ.columns = ['University', 'Total']
    
    # Menggunakan Altair untuk memiringkan label X
    chart_univ = alt.Chart(df_univ).mark_bar().encode(
        x=alt.X('University', axis=alt.Axis(labelAngle=-45)),
        y='Total',
        color='University'
    )
    st.altair_chart(chart_univ, use_container_width=True)

with ch2:
    st.subheader("Major")
    df_major = df['What is your field of study or major?'].value_counts().reset_index()
    df_major.columns = ['Major', 'Total']
    
    chart_major = alt.Chart(df_major).mark_bar().encode(
        x=alt.X('Major', axis=alt.Axis(labelAngle=-45)),
        y='Total',
        color='Major'
    )
    st.altair_chart(chart_major, use_container_width=True)

with ch3:
    st.subheader("Angkatan")
    df_angkatan = df['Please enter your year of entry (e.g., 2025).'].value_counts().reset_index()
    df_angkatan.columns = ["Angkatan", "Total"]
    
    # Untuk Angkatan mungkin tidak perlu terlalu miring, tapi tetap diterapkan agar konsisten
    chart_angkatan = alt.Chart(df_angkatan).mark_bar().encode(
        x=alt.X('Angkatan:O', axis=alt.Axis(labelAngle=-45)),
        y='Total'
    )
    st.altair_chart(chart_angkatan, use_container_width=True)

with ch4:
    st.subheader("Information")
    angkatan_field = df.columns[6]
    df_info = df[angkatan_field].value_counts().reset_index()
    df_info.columns = ["From", "Total"]
    
    chart_info = alt.Chart(df_info).mark_bar().encode(
        x=alt.X('From', axis=alt.Axis(labelAngle=-45)),
        y='Total',
        color='From'
    )
    st.altair_chart(chart_info, use_container_width=True)


st.divider()
st.header("Weekly Class")

materi, benefit, join = st.columns(3, border=True)

with materi:
    st.subheader("Jalannya Materi")
    rating_field = df.columns[8]
    df_rating = df[rating_field].value_counts().reset_index()
    df_rating.columns = ["Rating", "Total"]
    st.bar_chart(df_rating, x='Rating', y='Total', horizontal=True)

with benefit:
    st.subheader("Benefit")
    benefit_field = df.columns[9]
    df_rating = df[benefit_field].value_counts().reset_index()
    df_rating.columns = ["Benefit", "Total"]
    st.bar_chart(df_rating, x='Benefit', y='Total', horizontal=True)

with join:
    st.subheader("Keinginan untuk join next weekly class")
    df_join = df['How likely are you to join the future weekly class based on this weekly class?'].value_counts().reset_index()
    df_join.columns = ['Join', 'Total']
    st.bar_chart(df_join, x='Join', y='Total', horizontal=True)

# Ekspetasi
st.subheader("Ekspetasi")
expectation = '''
### **Poin-Poin Positif yang Perlu Kita Pertahankan & Kembangkan:**
* **Haus Ilmu PM & MVP (Hampir semua responden, sekitar 30+ orang):** Mayoritas peserta (nyaris semua, sekitar 30an lebih dari 38 responden!) pengen banget nambah ilmu, wawasan, atau mendalami lagi seputar Product Management dan MVP. Ini menunjukkan topik kita relevan dan diminati. Mereka datang dengan ekspektasi tinggi untuk dapat ilmu baru, insight menarik, dan pemahaman yang lebih baik tentang PM dan MVP.
* **Penekanan ke MVP Spesifik (Sekitar 9-10 orang):** Cukup banyak yang secara spesifik pengen paham banget apa itu MVP, scopenya, sampai gimana cara membangunnya. Ini penting banget karena jadi inti dari kelas kita.
* **Pengen yang Praktikal (Sekitar 3-4 orang):** Ada beberapa yang pengen ilmunya bisa langsung dipraktekkin, kayak gimana sih cara nentuin fitur utama buat MVP atau mempelajari PM secara lebih praktis. Ini bisa jadi fokus ke depan biar materi nggak cuma teori.
* **Kelas yang Seru & Insightful (Sekitar 3 orang):** Beberapa peserta juga berharap kelasnya dibawakan secara insightful, nggak monoton, dan bisa nyambungin topik dari kelas sebelumnya. Ini feedback bagus buat kita jaga kualitas penyampaian materi.

### **Poin yang Bisa Kita Improve:**
* **Penguatan Konsep Dasar (Muncul dari 1 responden):** Ada satu respon yang nunjukkin kalau masih ada miskonsepsi soal MVP (dia kira 'Most Valuable Person'). Ini jadi sinyal buat kita, di awal atau pas diskusi, mungkin perlu re-emphasize lagi definisi-definisi kunci biar semua peserta punya pemahaman dasar yang sama, apalagi kalau pesertanya dari berbagai latar belakang. Ini bukan masalah, tapi peluang biar nggak ada yang salah paham dari awal.

**Overall**, vibes-nya positif banget! Member sangat eager buat belajar PM dan MVP lebih dalam. Kita tinggal fokus buat nyediain konten yang insightful, praktikal, dan memastikan konsep dasarnya nyampe ke semua orang.
'''
st.markdown(expectation)

# Improve
st.subheader("Improvment")
improve = '''
**Poin-Poin Positif yang Bisa Kita Tingkatkan atau Tambahkan**:

1. Interaktivitas Kelas:
    * Terdapat 3 responden yang ingin kelasnya lebih interaktif lagi. Mereka saranin biar ada game atau kuis untuk mencairkan suasana dan bikin materi lebih mudah dicerna.
    * Ada juga yang minta sesi Q&A-nya bisa diperpanjang atau slot pesertanya dibanyakin biar semua kebagian nanya. Ini bagus banget buat bikin suasana kelas makin hidup dan peserta makin engage!

2. Eksplorasi Platform Presentasi:
    * Gambaran: Satu responden sempat nyaranin buat coba pakai platform presentasi berbasis web yang mungkin bisa memberikan pengalaman berbeda. Ini bisa jadi opsi menarik kalau kita mau explore hal baru ke depannya.

    
**Poin-Poin Negatif yang Perlu Kita Perbaiki atau Tingkatkan**:

1. Informasi Jadwal Kelas:
    * Gambaran: Lumayan ada 2 responden yang mengeluh info jadwalnya sering H-1 atau terlalu mendadak. Jadi, usahakan ke depannya info jadwal bisa lebih awal ya, mungkin H-2 atau H-3 biar peserta bisa siap-siap dan punya waktu untuk mengatur jadwal mereka.

2. Waktu dan Durasi Kelas:
    * Gambaran: Ini cukup banyak yang request (sekitar 5 responden). Ada yang minta jadwalnya lebih fleksibel, durasi kelasnya agak diperlama dikit, bahkan ada juga yang pengen kelasnya dimulai lebih awal atau setidaknya selalu tepat waktu agar tidak molor. Jadi, kita perlu evaluasi lagi nih soal jadwal dan durasi biar makin pas buat semua dan menjaga komitmen waktu.

3. Kualitas Materi & Contoh Praktis:
    * Gambaran: Sekitar 5 responden juga kasih masukan buat materi kita. Mereka pengen penjelasan materinya bisa sedikit lebih detail atau bahkan diperbanyak teori. Paling banyak sih yang minta lebih banyak contoh langsung dalam praktik, terutama langkah-langkah membuat MVP biar lebih mudah diaplikasikan. Terus, sesi feedback juga ada yang saranin buat diperdalam. Ini penting banget biar ilmunya makin nempel dan langsung bisa dipraktikkan!
'''
st.markdown(improve)

# Value
st.subheader("Value")
value = '''
### **Poin-Poin Positif yang Berharga (Apa yang Disukai Peserta):**

1. **Materi PM & MVP Nampol Banget! (Total 13 responden)**
    * Banyak banget yang bilang mereka jadi **lebih paham soal Product Management secara mendalam**, termasuk insight-insight menarik tentang PM. Kira-kira ada **8 orang** yang nge-highlight ini.
    * Nggak cuma PM, **pemahaman soal MVP juga bikin mereka "ngeh" banget**, mulai dari pentingnya sampai jenis-jenisnya. Ada **5 orang** yang merasakan benefit ini. Ini nunjukkin kalau materi inti kita sudah *on point* dan relevan!

2. **Dapat Ilmu & Wawasan Baru (7 responden)**
    * Responden merasa dapat banyak ilmu dan wawasan baru yang bermanfaat secara umum dari kelas ini. Ini nunjukkin kalau setiap kelas kita selalu berhasil kasih nilai tambah.

3. **Pemateri & Pembawa Acara Top Banget! (2 responden)**
    * Ada juga yang muji pemateri dan pembawa acara kita **bagus dan keren dalam penyampaian**. Ini penting banget biar suasana kelas tetap asyik dan informatif.

### **Poin-Poin yang Bisa Kita Tingkatkan (Bukan Negatif, tapi Saran yang Berharga!):**

1. **Pengembangan Materi yang Lebih Mendalam & Aplikatif (Total 6 responden)**
    * Beberapa responden, sekitar **1 orang**, ngasih sinyal kalau mereka pengen materi PM yang **lebih mendalam lagi** dari yang sudah ada. Ini nunjukkin antusiasme mereka untuk eksplorasi lebih lanjut.
    * Selain itu, ada juga permintaan atau ketertarikan pada topik-topik yang **lebih aplikatif dan praktis mengenai skill set seorang PM**. Contohnya: gimana PM memimpin tim, metode komunikasi yang efektif, sampai identifikasi produk. Ada sekitar **5 orang** yang menunjukkan minat ke arah sana. Ini bisa jadi ide emas buat topik kelas selanjutnya yang lebih ke 'how-to' atau 'deep dive' skill PM.

**Kesimpulan Umum:** Secara keseluruhan, kelas kita sudah berjalan baik dan memberikan banyak manfaat buat peserta. Kita bisa terus pertahankan kualitas materi inti dan pemateri, sambil mulai mikirin buat eksplorasi topik yang lebih mendalam atau aplikatif di sesi-sesi berikutnya.
'''
st.markdown(value)


st.subheader("Question")
question = '''
### **Ringkasan Feedback dari Member Weekly Class**

**Poin-Poin Positif:**
* **Materi dan Kelas Secara Umum Sudah Bagus:** Ada member yang bilang "semua sudah bagus". Ini nunjukkin kalau secara keseluruhan, materi yang kita bawakan sudah on track dan cukup disukai. Keep up the good work!

### **Poin-Poin yang Perlu Di-improve/Ditinjau (biar Weekly Class makin kece badai!):**

**1. Koneksi Jaringan/Sinyal (Negatif – Teknis):**
* **Gambaran Jumlah:** Sekitar 2 member mengalami kendala ini.
* **Detail Feedback:** Ada yang menyebut "signal connection" dan "masalah jaringan". Ini penting banget buat kita perhatikan karena bisa mengganggu pengalaman belajar mereka. Mungkin bisa diimbau ke peserta untuk mengecek koneksi, atau kita bisa cek lagi stabilitas platform yang digunakan.

**2. Pendalaman Materi Teknis/Praktis MVP (Perbaikan Konten):**
* **Gambaran Jumlah:** Ini jadi perhatian lumayan banyak member, sekitar **7 orang**.
* **Detail Feedback:** Banyak pertanyaan yang mengarah ke implementasi dan detail teknis di lapangan, seperti:
    * "Bagaimana membuat MVP yang baik dalam praktik lapangan?"
    * "Agak bingung tentang langkah-langkah membuat MVP."
    * "Bagaimana cara menyelesaikan konflik saat diskusi antar tim terkait MVP?"
'''
st.markdown(question)