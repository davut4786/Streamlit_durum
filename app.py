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
tur = st.selectbox("Tür", options=[1, 0], format_func=lambda x: "Köpek" if x == 1 else "Kedi")

# Arrange inputs in rows of four with spacing using st.columns
col1, col2, col3, col4 = st.columns(4, gap="large")
with col1:
    GRAN = st.number_input("GRAN", value=None, format="%.2f", step=None)
    HCT = st.number_input("HCT", value=None, format="%.2f", step=None)
    MCV = st.number_input("MCV", value=None, format="%.2f", step=None)

with col2:
    GRAN_A = st.number_input("GRAN_A", value=None, format="%.2f", step=None)
    MCH = st.number_input("MCH", value=None, format="%.2f", step=None)
    RDW = st.number_input("RDW", value=None, format="%.2f", step=None)

with col3:
    LYM = st.number_input("LYM", value=None, format="%.2f", step=None)
    MCHC = st.number_input("MCHC", value=None, format="%.2f", step=None)
    WBC = st.number_input("WBC", value=None, format="%.2f", step=None)

with col4:
    LYM_A = st.number_input("LYM_A", value=None, format="%.2f", step=None)
    MON = st.number_input("MON", value=None, format="%.2f", step=None)

# Dropdown inputs with 'None' as default (no selection)
inkordinasyon = st.selectbox("İnkordinasyon", options=[None, 1, 0], format_func=lambda x: "Seçiniz" if x is None else ("Evet" if x == 1 else "Hayır"))
ishal = st.selectbox("İshal", options=[None, 1, 0], format_func=lambda x: "Seçiniz" if x is None else ("Evet" if x is 1 else "Hayır"))
istahsizlik = st.selectbox("İştahsızlık", options=[None, 1, 0], format_func=lambda x: "Seçiniz" if x is None else ("Evet" if x is 1 else "Hayır"))
kusma = st.selectbox("Kusma", options=[None, 1, 0], format_func=lambda x: "Seçiniz" if x is None else ("Evet" if x is 1 else "Hayır"))
solunum_guclugu = st.selectbox("Solunum Güçlüğü", options=[None, 1, 0], format_func=lambda x: "Seçiniz" if x is None else ("Evet" if x is 1 else "Hayır"))

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
