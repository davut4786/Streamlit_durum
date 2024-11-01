import streamlit as st
import pickle
import pandas as pd

# Model loading (rf_model.pkl file path)
model_path = "rf_model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Streamlit title
st.title("Hastalık Durumu Tahmin Uygulaması")

# Input fields for user data
tur = st.radio("Tür", options=[1, 0], format_func=lambda x: "1 (seçili)" if x == 1 else "0 (seçili)")
GRAN = st.number_input("GRAN", value=None)
GRAN_A = st.number_input("GRAN_A", value=None)
LYM = st.number_input("LYM", value=None)
LYM_A = st.number_input("LYM_A", value=None)
MON = st.number_input("MON", value=None)
HCT = st.number_input("HCT", value=None)
MCH = st.number_input("MCH", value=None)
MCHC = st.number_input("MCHC", value=None)
MCV = st.number_input("MCV", value=None)
RDW = st.number_input("RDW", value=None)
WBC = st.number_input("WBC", value=None)

# Radio button inputs
inkordinasyon = st.radio("İnkordinasyon", options=[1, 0], format_func=lambda x: "Evet" if x == 1 else "Hayır")
ishal = st.radio("İshal", options=[1, 0], format_func=lambda x: "Evet" if x == 1 else "Hayır")
istahsizlik = st.radio("İştahsızlık", options=[1, 0], format_func=lambda x: "Evet" if x == 1 else "Hayır")
kusma = st.radio("Kusma", options=[1, 0], format_func=lambda x: "Evet" if x == 1 else "Hayır")
solunum_guclugu = st.radio("Solunum Güçlüğü", options=[1, 0], format_func=lambda x: "Evet" if x == 1 else "Hayır")

# Prediction button and validation check
if st.button("Tahmin Et"):
    # Validate input fields for empty values
    inputs = {
        "GRAN": GRAN, "GRAN_A": GRAN_A, "LYM": LYM, "LYM_A": LYM_A, "MON": MON,
        "HCT": HCT, "MCH": MCH, "MCHC": MCHC, "MCV": MCV, "RDW": RDW, "WBC": WBC
    }
    
    # Check for missing values and prompt warning
    missing_values = [name for name, value in inputs.items() if value is None]
    if missing_values:
        st.warning(f"Lütfen {', '.join(missing_values)} değerlerini doldurunuz.")
    else:
        # Prepare data for model prediction
        data = [[tur, GRAN, GRAN_A, LYM, LYM_A, MON, HCT, MCH, MCHC, MCV, RDW, WBC, inkordinasyon, ishal, istahsizlik, kusma, solunum_guclugu]]
        prediction = model.predict(data)[0]

        # Display the prediction result
        st.write(f"Tahmin Sonucu: {prediction}")
