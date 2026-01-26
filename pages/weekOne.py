import streamlit as st
import pandas as pd
import altair as alt

# Data Preparation
df = pd.read_csv('data\weekSatuClean.csv')

st.title("Week One Data Overview")
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
    
    # Tambahkan :O (Ordinal) atau :N (Nominal) setelah nama kolom 'Angkatan'
    # Ini akan menghilangkan koma dan menganggap tahun sebagai teks/label
    chart_angkatan = alt.Chart(df_angkatan).mark_bar().encode(
        x=alt.X('Angkatan:O', axis=alt.Axis(labelAngle=-45)), 
        y='Total'
    )
    st.altair_chart(chart_angkatan, use_container_width=True)

with ch4:
    st.subheader("Information")
    angkatan_field = df.columns[5]
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
    benefit_field = df.columns[7]
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
Ekspetasi dari responden meliputi 2 poin berikut
1. **Dahaga Ilmu dan Insight Baru (Mayoritas Responden = Hampir Semua)**
2. **Pengalaman Baru dan Kelas yang Seru (Cukup Banyak Responden = Sekitar 3 dari 8)**
    
Dengan tinggi dan positifnya ekspetasi member, hal yang bisa kita jadikan acuan:
1. **Kedalaman dan Relevansi Materi**: 

    Karena semua pengen ilmu yang bermanfaat dan insight baru, kita perlu pastikan materi ke depannya nggak cuma "kulitnya" aja. Usahakan materinya mendalam, aplikatif, dan relevan sama kebutuhan mereka di Product Management. Mungkin bisa diperbanyak studi kasus atau contoh konkret yang bisa langsung mereka terapkan.
2. **Interaktivitas dan Cara Penyampaian**: 

    Mengingat ada yang berharap kelasnya seru dan fun, kita bisa eksplor lebih banyak cara penyampaian materi yang interaktif. Mungkin sesi Q&A yang lebih panjang, diskusi kelompok kecil, atau format lain yang bikin peserta lebih engage dan nggak cuma jadi pendengar pasif.
3. **Kejelasan Output/Outcome**: 

    Ekspektasi untuk tahu "apa saja yang diperlukan dan dihasilkan" bisa jadi sinyal kalau mereka butuh gambaran yang jelas dari setiap topik. Pastikan setiap sesi punya tujuan belajar yang transparan dan hasil yang bisa langsung mereka terapkan di pekerjaan atau proyek mereka.

Secara keseluruhan, para member memiliki antusias yang besar dan berharap dapat ilmu serta pengalaman positif. 
'''
st.markdown(expectation)

# Improve
st.subheader("Improvment")
improve = '''
**Poin-poin yang dinilai bagus dari respon member**
1. **Banyak yang Puas dan Nggak Ada Komplain!**

    Gambaran Jumlah: Ini lumayan banyak nih, dari sampel yang terlihat, beberapa member cuma bilang "Tidak ada, sudah bagus", "Nothing", "none", atau "tidak ada" pas ditanya soal improvement. 
    Bahkan ada yang saking serunya sampai "eum bingung seru semua". Ini sinyal bagus, artinya banyak yang udah happy dengan format dan materi kelas kita!
2. **Kahoot Jadi Favorit!**

    Gambaran Jumlah: Ada member yang request spesifik banget: "mau kahoot terus soalnya seruwww"! 
    Ini nunjukkin kalau elemen interaktif kayak Kahoot itu super engaging dan bikin suasana kelas jadi hidup banget. Mantap!

**Poin-Poin yang Perlu Di-improve/Jadi Catatan**:
1. Kapasitas Zoom Perlu Ditingkatkan!
2. Keinginan untuk Konten Lebih Menarik/Bervariasi (meski belum detail):
   
**Kesimpulan Sementara**: 
Overall, Weekly Class kita udah diterima dengan baik dan banyak yang enjoy. 
Yang paling urgent untuk di tindak lanjuti sepertinya masalah kapasitas Zoom biar semua yang antusias bisa ikutan. 
Selain itu, Kahoot terbukti jadi game changer buat engagement, sehingga bisa dipertahankan kreativitas untuk membuat pertanyaan yang sifatnya menghibur juga!
'''
st.markdown(improve)

# Value
st.subheader("Value")
value = '''
Terdapat beberapa benefit value yang dirasakan member selama berjalannya weekly class:
1. Insight & Pengetahuan
2. Kualitas Narasumber & Sharing Pengalaman
3. Materi Relevan, Mudah Dipahami, dan Detail
4. Materi Praktis, Studi Kasus & Problem Solving
5. Peluang Diskusi & Q&A Interaktif
6. Cocok untuk Pemula

**Gambaran Umum**: 
Secara keseluruhan, member sangat menghargai konten yang memberikan insight baru, disampaikan oleh narasumber yang menarik dengan sharing pengalaman relevan, 
serta materi yang mudah dicerna dan aplikatif. Ini adalah formula sukses yang bisa kita pertahankan dan kembangkan untuk weekly class selanjutnya.
'''
st.markdown(value)


st.subheader("Question")
question = '''
**Poin-Poin yang Bisa Kita Tingkatkan (Saran/Kritik Konstruktif):**

* **Materi Kurang Interaktif & Kurang Mendalam:** Beberapa member (10-15 orang) merasa materi bisa lebih seru lagi, kurang interaktif, atau pembahasannya kurang "deep".
* **Butuh Lebih Banyak Studi Kasus:** Banyak request untuk contoh kasus nyata di lapangan agar lebih paham aplikasi teorinya.
* **Durasi Kelas:** Ada sinyal bahwa durasi kelas terasa terlalu pendek untuk topik yang kompleks.

**Potensi Topik Kelas Baru (Deeper Dive):**

1. **User Research & User Testing:** Paling menonjol (5-7 pertanyaan). Peserta ingin tahu best practice melakukannya di perusahaan.
2. **Pengelolaan Produk dari Awal:** (3-5 pertanyaan). Butuh guidance soal pembuatan PRD dan validasi ide.
3. **Strategi & Karir PM:** (3-5 pertanyaan). Insight tentang karir di startup vs corporate.
4. **Skill Teknis Tambahan:** Request materi tentang prototyping dan wireframing.

**Kesimpulan untuk Next Plan:** Member mencari ilmu yang **praktis, mendalam, dan applicable**. Fokus selanjutnya adalah memperbanyak studi kasus nyata dan mempertimbangkan durasi yang lebih pas untuk topik berat.
'''
st.markdown(question)