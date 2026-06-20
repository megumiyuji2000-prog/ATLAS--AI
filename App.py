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
    prompt = st.text_input("Tanya ATLAS AI:")
    if st.button("Kirim"):
        st.write(f"ATLAS AI: Belum disambungin API R, sabar 😂 Jawaban buat: {prompt}")

elif menu.startswith("5"):
    st.subheader("Kalkulator Nabung PAK AA")
    target = st.number_input("Target nabung:", 0)
    hari = st.number_input("Berapa hari:", 1)
    if st.button("Hitung"):
        st.success(f"Nabung Rp{target/hari:,.0f} per hari R. Biar gak boncos beli kredit Manus")


st.image("https://contoh.com/logo-atlas.png", width=200)
