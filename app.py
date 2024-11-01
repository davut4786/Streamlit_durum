import streamlit as st
import pickle
import pandas as pd

# Model loading (rf_model.pkl file path)
model_path = "rf_model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Streamlit title
st.title("Hastalık Durumu Tahmin Uygulaması")

# Function to clear all inputs
def clear_inputs():
    # Reset all session state values for input fields
    for key in [
        "tur", "GRAN", "GRAN_A", "LYM", "LYM_A", "MON",
        "HCT", "MCH", "MCHC", "MCV", "RDW", "WBC",
        "inkordinasyon", "ishal", "istahsizlik", "kusma", "solunum_guclugu"
    ]:
        if key in st.session_state:
            del st.session_state[key]  # Remove the key from session state

# Input fields for user data
tur = st.radio("Tür", options=[1, 0], format_func=lambda x: "Köpek" if x == 1 else "Kedi", key='tur')
GRAN = st.number_input("GRAN", value=None, format="%.2f", key='GRAN')
GRAN_A = st.number_input("GRAN_A", value=None, format="%.2f", key='GRAN_A')
LYM = st.number_input("LYM", value=None, format="%.2f", key='LYM')
LYM_A = st.number_input("LYM_A", value=None, format="%.2f", key='LYM_A')
MON = st.number_input("MON", value=None, format="%.2f", key='MON')
HCT = st.number_input("HCT", value=None, format="%.2f", key='HCT')
MCH = st.number_input("MCH", value=None, format="%.2f", key='MCH')
MCHC = st.number_input("MCHC", value=None, format="%.2f", key='MCHC')
MCV = st.number_input("MCV", value=None, format="%.2f", key='MCV')
RDW = st.number_input("RDW", value=None, format="%.2f", key='RDW')
WBC = st.number_input("WBC", value=None, format="%.2f", key='WBC')

# Radio button inputs with 'None' as default (no selection)
inkordinasyon = st.radio("İnkordinasyon", options=[None, 1, 0], format_func=lambda x: "Seçiniz" if x is None else ("Evet" if x == 1 else "Hayır"), key='inkordinasyon')
ishal = st.radio("İshal", options=[None, 1, 0], format_func=lambda x: "Seçiniz" if x is None else ("Evet" if x == 1 else "Hayır"), key='ishal')
istahsizlik = st.radio("İştahsızlık", options=[None, 1, 0], format_func=lambda x: "Seçiniz" if x is None else ("Evet" if x == 1 else "Hayır"), key='istahsizlik')
kusma = st.radio("Kusma", options=[None, 1, 0], format_func=lambda x: "Seçiniz" if x is None else ("Evet" if x == 1 else "Hayır"), key='kusma')
solunum_guclugu = st.radio("Solunum Güçlüğü", options=[None, 1, 0], format_func=lambda x: "Seçiniz" if x is None else ("Evet" if x == 1 else "Hayır"), key='solunum_guclugu')

# Prediction button and validation check
if st.button("Tahmin Et"):
    # Validate input fields for empty values
    numeric_inputs = {
        "GRAN": GRAN, "GRAN_A": GRAN_A, "LYM": LYM, "LYM_A": LYM_A, "MON": MON,
        "HCT": HCT, "MCH": MCH, "MCHC": MCHC, "MCV": MCV, "RDW": RDW, "WBC": WBC
    }
    categorical_inputs = {
        "Tür": tur, "İnkordinasyon": inkordinasyon, "İshal": ishal,
        "İştahsızlık": istahsizlik, "Kusma": kusma, "Solunum Güçlüğü": solunum_guclugu
    }

    # Check for missing numeric values
    missing_numeric_values = [name for name, value in numeric_inputs.items() if value is None]
    # Check for missing categorical selections
    missing_categorical_values = [name for name, value in categorical_inputs.items() if value is None]

    # Display warnings for missing values
    if missing_numeric_values or missing_categorical_values:
        if missing_numeric_values:
            st.warning(f"Lütfen {', '.join(missing_numeric_values)} değerlerini doldurunuz.")
        if missing_categorical_values:
            st.warning(f"Lütfen {', '.join(missing_categorical_values)} seçeneklerini seçiniz.")
    else:
        # Prepare data for model prediction
        data = [[tur, GRAN, GRAN_A, LYM, LYM_A, MON, HCT, MCH, MCHC, MCV, RDW, WBC, inkordinasyon, ishal, istahsizlik, kusma, solunum_guclugu]]
        prediction = model.predict(data)[0]

        # Display the prediction result
        st.write(f"Tahmin Sonucu: {prediction}")

# Clear button
if st.button("Temizle"):
    clear_inputs()
