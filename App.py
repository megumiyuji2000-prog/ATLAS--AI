import streamlit as st

st.set_page_config(page_title="ATLAS AI v5", page_icon="⚙️")
st.title("ATLAS AI v5 - BENGKEL UNIVERSAL")
st.caption("By ALANTIQ | PAK AA")

menu = st.selectbox("Pilih fitur R [1-7]:", [
    "1. Ngobrol sama ATLAS",
    "2. Tanya Wikipedia langsung", 
    "3. Liat isi Database.txt",
    "4. Hitung MTK Dasar + Bagi",
    "5. Kalkulator Nabung PAK AA",
    "6. Tutorial Benerin Sesuatu",
    "7. Tentang ATLAS AI"
])

if menu.startswith("1"):
    st.subheader("Ngobrol sama ATLAS")
    prompt = st.text_input("Tanya ATLAS AI:")  
    if st.button("Kirim"):
        st.info(f"ATLAS AI: Jawaban buat '{prompt}' masih dummy R 😂 Nanti sambungin ke AI beneran")

elif menu.startswith("2"):
    st.subheader("Wikipedia")
    query = st.text_input("Cari apa di Wikipedia:")  
    if st.button("Cari"):
        st.warning("Fitur Wikipedia belum disambungin R. Butuh library `wikipedia`")

elif menu.startswith("3"):
    st.subheader("Database.txt")
    st.error("File Database.txt belum ada di repo R. Upload dulu")

elif menu.startswith("4"):
    st.subheader("Hitung MTK Dasar")
    a = st.number_input("Angka 1:", 0)
    b = st.number_input("Angka 2:", 0)
    op = st.selectbox("Operasi:", ["Tambah","Kurang","Kali","Bagi"])
    if st.button("Hitung"):
        if op=="Tambah": st.success(f"Hasil: {a+b}")
        elif op=="Kurang": st.success(f"Hasil: {a-b}")
        elif op=="Kali": st.success(f"Hasil: {a*b}")
        elif op=="Bagi": 
            if b!=0: st.success(f"Hasil: {a/b}")
            else: st.error("Gak bisa bagi 0 R")

elif menu.startswith("5"):
    st.subheader("Kalkulator Nabung PAK AA")
    target = st.number_input("Target nabung:", 0)
    hari = st.number_input("Berapa hari:", 1, value=30)
    if st.button("Hitung"):
        st.success(f"Nabung Rp{target/hari:,.0f} per hari R. Biar gak boncos")

elif menu.startswith("6"):
    st.subheader("Tutorial Benerin")
    rusak = st.text_input("Apa yg rusak R?")  
    if st.button("Kasih Tutorial"):
        st.info(f"Tutorial benerin '{rusak}': 1. Matikan dulu 2. Banting 3. Beli baru 😂")

elif menu.startswith("7"):
    st.subheader("Tentang ATLAS AI")
    st.write("ATLAS AI v5 dibuat PAK AA pake Streamlit. Masih tahap belajar R ✌️")
