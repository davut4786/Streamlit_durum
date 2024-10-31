import streamlit as st
import pickle
import pandas as pd

# Modeli yükleme (rf_model.pkl dosyasının yolu)
model_path = "rf_model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Streamlit başlık
st.title("Hastalık Tahmin Uygulaması")

# Kullanıcıdan verileri almak için giriş alanları
tur = st.radio("Tür", options=[1, 0], format_func=lambda x: "1 (seçili)" if x == 1 else "0 (seçili)")
GRAN = st.number_input("GRAN", value=0.0)
GRAN_A = st.number_input("GRAN_A", value=0.0)
LYM = st.number_input("LYM", value=0.0)
LYM_A = st.number_input("LYM_A", value=0.0)
MON = st.number_input("MON", value=0.0)
HCT = st.number_input("HCT", value=0.0)
MCH = st.number_input("MCH", value=0.0)
MCHC = st.number_input("MCHC", value=0.0)
MCV = st.number_input("MCV", value=0.0)
RDW = st.number_input("RDW", value=0.0)
WBC = st.number_input("WBC", value=0.0)

# Radio button tarzında girişler
inkordinasyon = st.radio("İnkordinasyon", options=[1, 0], format_func=lambda x: "Evet" if x == 1 else "Hayır")
ishal = st.radio("İshal", options=[1, 0], format_func=lambda x: "Evet" if x == 1 else "Hayır")
istahsizlik = st.radio("İştahsızlık", options=[1, 0], format_func=lambda x: "Evet" if x == 1 else "Hayır")
kusma = st.radio("Kusma", options=[1, 0], format_func=lambda x: "Evet" if x == 1 else "Hayır")
solunum_guclugu = st.radio("Solunum Güçlüğü", options=[1, 0], format_func=lambda x: "Evet" if x == 1 else "Hayır")

# Tahmin butonu ve tahmin işlemi
if st.button("Tahmin Et"):
    # Verileri modele uygun hale getirme
    veriler = [[tur, GRAN, GRAN_A, LYM, LYM_A, MON, HCT, MCH, MCHC, MCV, RDW, WBC, inkordinasyon, ishal, istahsizlik, kusma, solunum_guclugu]]
    tahmin = model.predict(veriler)[0]
    
    # Sonucu gösterme
    st.write(f"Tahmin Sonucu: {tahmin}")
