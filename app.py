import streamlit as st
import pickle
import pandas as pd

# Load model
model_path = "rf_model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Streamlit title centered
st.markdown("<h1 style='text-align: center;'>Hastalık Durumu Tahmin Uygulaması</h1>", unsafe_allow_html=True)

# Section for categorical inputs (3 per row)
st.markdown("**Anamnez Bilgileri**")
cat_col1, cat_col2, cat_col3 = st.columns(3)
with cat_col1:
    tur = st.selectbox("Tür", options=[1, 0], format_func=lambda x: "Köpek" if x == 1 else "Kedi")
with cat_col2:
    inkordinasyon = st.selectbox("İnkordinasyon", options=[None, 1, 0], format_func=lambda x: "Seçiniz" if x is None else ("Var" if x == 1 else "Yok"))
with cat_col3:
    ishal = st.selectbox("İshal", options=[None, 1, 0], format_func=lambda x: "Seçiniz" if x is None else ("Var" if x == 1 else "Yok"))

# Second row of categorical inputs
cat_col4, cat_col5, cat_col6 = st.columns(3)
with cat_col4:
    istahsızlık = st.selectbox("İştahsızlık", options=[None, 1, 0], format_func=lambda x: "Seçiniz" if x is None else ("Var" if x == 1 else "Yok"))
with cat_col5:
    kusma = st.selectbox("Kusma", options=[None, 1, 0], format_func=lambda x: "Seçiniz" if x is None else ("Var" if x == 1 else "Yok"))
with cat_col6:
    solunum_guclugu = st.selectbox("Solunum Güçlüğü", options=[None, 1, 0], format_func=lambda x: "Seçiniz" if x is None else ("Var" if x == 1 else "Yok"))

# Add extra space between sections
st.markdown("<br><br>", unsafe_allow_html=True)

# Section for numeric inputs (3 per row)
st.markdown("**Hemogram Değerleri**")
num_col1, num_col2, num_col3 = st.columns(3)
with num_col1:
    GRAN = st.number_input("GRAN", format="%.2f")
    LYM = st.number_input("LYM", format="%.2f")
    MCH = st.number_input("MCH", format="%.2f")
with num_col2:
    GRAN_A = st.number_input("GRAN_A", format="%.2f")
    LYM_A = st.number_input("LYM_A", format="%.2f")
    MCHC = st.number_input("MCHC", format="%.2f")
with num_col3:
    MON = st.number_input("MON", format="%.2f")
    HCT = st.number_input("HCT", format="%.2f")
    MCV = st.number_input("MCV", format="%.2f")

# Another row for remaining numeric inputs
num_col4, num_col5, num_col6 = st.columns(3)
with num_col4:
    RDW = st.number_input("RDW", format="%.2f")
with num_col5:
    WBC = st.number_input("WBC", format="%.2f")

# Centered prediction button
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
if st.button("Tahmin Et"):
    # Validate input fields for empty values
    numeric_inputs = {
        "GRAN": GRAN, "GRAN_A": GRAN_A, "LYM": LYM, "LYM_A": LYM_A, "MON": MON,
        "HCT": HCT, "MCH": MCH, "MCHC": MCHC, "MCV": MCV, "RDW": RDW, "WBC": WBC
    }
    categorical_inputs = {
        "Tür": tur, "İnkordinasyon": inkordinasyon, "İshal": ishal,
        "İştahsızlık": istahsızlık, "Kusma": kusma, "Solunum Güçlüğü": solunum_guclugu
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
        data = [[tur, GRAN, GRAN_A, LYM, LYM_A, MON, HCT, MCH, MCHC, MCV, RDW, WBC, inkordinasyon, ishal, istahsızlık, kusma, solunum_guclugu]]
        prediction = model.predict(data)[0]

        # Display the prediction result centered
        st.markdown("<h2 style='text-align: center;'>Tahmin Sonucu: {}</h2>".format(prediction), unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
