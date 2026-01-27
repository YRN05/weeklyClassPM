import streamlit as st
import pandas as pd
import altair as alt

# Data Preparation
df = pd.read_csv('data/TechTalkClean.csv')

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
    rating_field = df.columns[9]
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
    df_join = df['How likely are you to join the future Tech Talk based on this Tech Talk?'].value_counts().reset_index()
    df_join.columns = ['Join', 'Total']
    st.bar_chart(df_join, x='Join', y='Total', horizontal=True)

# Ekspetasi
st.subheader("Ekspetasi")
expectation = '''
1. Haus akan ilmu Product Management (12 Responden)
2. Hal-hal yang bersifat praktikal (3 Responden)
3. Insight dari narasumber (2 Responden)
4. Pengalaman baru serta update teknologi (2 Responden)
5. Acara yang seru (1 Responden)
'''
st.markdown(expectation)

# Improve
st.subheader("Improvment")
improve = '''
**Already Good**
1. Kualitas Konten
2. Kepuasan Umum (banyak yang bilang 'tidak ada')

**Need to Improve**
1. Format acara (banyak yang ingin acaranya offline)
2. Interaksi & Engagement (ada 4 responden yang meminta lebih interaktif, kuis dan ice breaking di sela sesi)
3. Frekuensi Acara (banyak yang ingin lebih sering diadakan tech talk/antusias tinggi)
4. Management Waktu (durasi acara lebih fleksible, waktu untuk QnA lebih lama)
5. Variasi topik yang up to date

**Kesimpulan**
Jadi, intinya, feedback paling menonjol itu soal keinginan offline dan banget-banget pengen acara yang lebih interaktif. Sementara itu, frekuensi acara, manajemen waktu, dan variasi topik juga jadi masukan berharga yang bisa kita pertimbangkan.
'''
st.markdown(improve)

# Value
st.subheader("Value")
value = '''
1. Ilmu dan pengetahuan baru yang bermanfaat
2. Insight dan pengalaman langsung dari praktisi/expert
3. Materi yang spesifik dan up to date
4. Kesempatan networking dan inspirasi
5. Adanya interaksi, seperti sesi tanya jawab
'''
st.markdown(value)


st.subheader("Question")
question = '''
1. Skill & Pengembangan Karier PM (3 orang):
    - Beberapa member penasaran banget soal skill apa aja sih yang wajib dipunya Product Manager?
    - Mereka juga pengen tau gimana sih cara mulai dan ngembangin skill jadi PM?
    - Ada juga yang nanya gimana PM itu bisa "membangun" sesuatu dari awal.
    - Intinya: Mereka butuh panduan lebih lanjut soal perjalanan karier dan skill esensial seorang PM.
2. Implementasi Praktis / Integrasi di Lapangan (2 orang):
    - Dua orang member pengen banget tau gimana sih PM itu bisa melakukan integrasi secara praktis di dunia kerja nyata.
    - Intinya: Member butuh contoh atau studi kasus konkret tentang aplikasi teori di lapangan.
3. Dampak AI Terhadap Peran PM & IT (1 orang):
    - Ada satu member yang kepikiran banget, "Apakah AI bakal ngegantiin peran PM sama IT?"
    - Intinya: Ini topik hangat dan penting yang bisa jadi diskusi seru tentang masa depan profesi.
4. Tantangan & Keseimbangan Kerja PM (1 orang):
    - Satu member penasaran, "Gimana sih Product Manager itu nge-balance berbagai hal dalam pekerjaannya?"
    - Intinya: Mereka pengen tau tips dan trik manajemen waktu atau prioritas untuk PM.
'''
st.markdown(question)