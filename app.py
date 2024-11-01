import streamlit as st
import pickle
import pandas as pd

# Model loading (rf_model.pkl file path)
model_path = "rf_model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Streamlit title
st.title("Hastalık Durumu Tahmin Uygulaması")

# Define function to reset all inputs
def reset_inputs():
    st.session_state["tur"] = None
    st.session_state["GRAN"] = None
    st.session_state["GRAN_A"] = None
    st.session_state["LYM"] = None
    st.session_state["LYM_A"] = None
    st.session_state["MON"] = None
    st.session_state["HCT"] = None
    st.session_state["MCH"] = None
    st.session_state["MCHC"] = None
    st.session_state["MCV"] = None
    st.session_state["RDW"] = None
    st.session_state["WBC"] = None
    st.session_state["inkordinasyon"] = None
    st.session_state["ishal"] = None
    st.session_state["istahsizlik"] = None
    st.session_state["kusma"] = None
    st.session_state["solunum_guclugu"] = None

# Input fields for user data
tur = st.radio("Tür", options=[1, 0], format_func=lambda x: "Köpek" if x == 1 else "Kedi", key="tur")
GRAN = st.number_input("GRAN", value=st.session_state.get("GRAN", None), format="%.2f", key="GRAN")
GRAN_A = st.number_input("GRAN_A", value=st.session_state.get("GRAN_A", None), format="%.2f", key="GRAN_A")
LYM = st.number_input("LYM", value=st.session_state.get("LYM", None), format="%.2f", key="LYM")
LYM_A = st.number_input("LYM_A", value=st.session_state.get("LYM_A", None), format="%.2f", key="LYM_A")
MON = st.number_input("MON", value=st.session_state.get("MON", None), format="%.2f", key="MON")
HCT = st.number_input("HCT", value=st.session_state.get("HCT", None), format="%.2f", key="HCT")
MCH = st.number_input("MCH", value=st.session_state.get("MCH", None), format="%.2f", key="MCH")
MCHC = st.number_input("MCHC", value=st.session_state.get("MCHC", None), format="%.2f", key="MCHC")
MCV = st.number_input("MCV", value=st.session_state.get("MCV", None), format="%.2f", key="MCV")
RDW = st.number_input("RDW", value=st.session_state.get("RDW", None), format="%.2f", key="RDW")
WBC = st.number_input("WBC", value=st.session_state.get("WBC", None), format="%.2f", key="WBC")

# Radio button inputs with 'None' as default (no selection)
inkordinasyon = st.radio("İnkordinasyon", options=[None, 1, 0], format_func=lambda x: "Evet" if x == 1 else "Hayır" if x == 0 else "Seçiniz", key="inkordinasyon")
ishal = st.radio("İshal", options=[None, 1, 0], format_func=lambda x: "Evet" if x == 1 else "Hayır" if x == 0 else "Seçiniz", key="ishal")
istahsizlik = st.radio("İştahsızlık", options=[None, 1, 0], format_func=lambda x: "Evet" if x == 1 else "Hayır" if x == 0 else "Seçiniz", key="istahsizlik")
kusma = st.radio("Kusma", options=[None, 1, 0], format_func=lambda x: "Evet" if x == 1 else "Hayır" if x == 0 else "Seçiniz", key="kusma")
solunum_guclugu = st.radio("Solunum Güçlüğü", options=[None, 1, 0], format_func=lambda x: "Evet" if x == 1 else "Hayır" if x == 0 else "Seçiniz", key="solunum_guclugu")

# Button columns for "Tahmin Et" and "Temizle"
col1, col2 = st.columns(2)

with col1:
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

with col2:
    if st.button("Temizle"):
        reset_inputs()

