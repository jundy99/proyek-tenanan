import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

# --- Load data ---
file_path = r"C:\Python\Proyek Lomba Tenanan\data.csv"
df = pd.read_csv(file_path)

st.title("📚 Katalog/Menu Aplikasi")

# --- Menu ---
selected = option_menu(
    menu_title=None,
    options=["Home", "Data", "Visualisasi", "Pengaturan"],
    icons=["house", "table", "bar-chart", "gear"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

# --- Konten sesuai pilihan ---
if selected == "Home":
    st.header("📊 Dashboard Data Siswa")
    st.markdown("""
    Selamat datang di **Dashboard Data Siswa**.  
    Aplikasi ini menampilkan identitas serta perkembangan siswa sepanjang tahun.
    """)

    # Info dasar dataset
    st.subheader("📌 Informasi Dataset")
    st.write(f"Jumlah siswa: **{df.shape[0]}**")
    st.write(f"Jumlah kolom: **{df.shape[1]}**")

    # Distribusi gender
    gender_count = df['JK'].value_counts()

    col1, col2 = st.columns(2)
    with col1:
        st.metric("👦 Laki-laki", gender_count.get("L", 0))
        st.metric("👧 Perempuan", gender_count.get("P", 0))

    with col2:
        fig, ax = plt.subplots()
        ax.pie(gender_count, labels=gender_count.index, autopct="%1.1f%%", startangle=90)
        ax.set_title("Distribusi Jenis Kelamin")
        st.pyplot(fig)

    # Preview data
    st.subheader("📝 Contoh Data Siswa")
    st.dataframe(df.head(10))

elif selected == "Data":
    st.subheader("📂 Data Lengkap")
    st.dataframe(df)

elif selected == "Visualisasi":
    st.subheader("📈 Visualisasi")
    st.line_chart(df[['JULI_TB']])

elif selected == "Pengaturan":
    st.subheader("⚙️ Pengaturan")
    st.write("Halaman untuk konfigurasi aplikasi.")
