import streamlit as st
import pickle
import pandas as pd

# CSS to center-align the title, style the button, and frame each input section
st.markdown("""
    <style>
        .title {
            text-align: center;
        }
        .button {
            display: flex;
            justify-content: center;
            margin-top: 30px;
            font-size: 20px;
            padding: 10px 24px;
        }
        .stRadio label {
            font-weight: bold;
        }
        .stNumberInput, .stSelectbox {
            margin-right: 10px;
        }
        input[type="number"]::-webkit-inner-spin-button,
        input[type="number"]::-webkit-outer-spin-button,
        input[type="number"] {
            -webkit-appearance: none;
            -moz-appearance: textfield;
            margin: 0;
        }
        .input-frame {
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 10px;
        }
        .input-frame label {
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit title with center alignment
st.markdown('<h1 class="title">Hastalık Durumu Tahmin Uygulaması</h1>', unsafe_allow_html=True)

# Model loading (rf_model.pkl file path)
model_path = "rf_model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Input fields for user data
tur = st.selectbox("Tür", options=[1, 0], format_func=lambda x: "Köpek" if x == 1 else "Kedi")

# Arrange inputs in rows of four with spacing using st.columns and frame each input
col1, col2, col3, col4 = st.columns(4, gap="large")
with col1:
    st.markdown('<div class="input-frame">', unsafe_allow_html=True)
    GRAN = st.number_input("GRAN", value=None, format="%.2f", step=None)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-frame">', unsafe_allow_html=True)
    HCT = st.number_input("HCT", value=None, format="%.2f", step=None)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-frame">', unsafe_allow_html=True)
    MCV = st.number_input("MCV", value=None, format="%.2f", step=None)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-frame">', unsafe_allow_html=True)
    inkordinasyon = st.selectbox("İnkordinasyon", options=[None, 1, 0], format_func=lambda x: "Seçiniz" if x is None else ("Var" if x == 1 else "Yok"))
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="input-frame">', unsafe_allow_html=True)
    GRAN_A = st.number_input("GRAN_A", value=None, format="%.2f", step=None)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-frame">', unsafe_allow_html=True)
    MCH = st.number_input("MCH", value=None, format="%.2f", step=None)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-frame">', unsafe_allow_html=True)
    RDW = st.number_input("RDW", value=None, format="%.2f", step=None)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-frame">', unsafe_allow_html=True)
    ishal = st.selectbox("İshal", options=[None, 1, 0], format_func=lambda x: "Seçiniz" if x is None else ("Var" if x == 1 else "Yok"))
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="input-frame">', unsafe_allow_html=True)
    LYM = st.number_input("LYM", value=None, format="%.2f", step=None)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-frame">', unsafe_allow_html=True)
    MCHC = st.number_input("MCHC", value=None, format="%.2f", step=None)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-frame">', unsafe_allow_html=True)
    WBC = st.number_input("WBC", value=None, format="%.2f", step=None)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-frame">', unsafe_allow_html=True)
    istahsizlik = st.selectbox("İştahsızlık", options=[None, 1, 0], format_func=lambda x: "Seçiniz" if x is None else ("Var" if x == 1 else "Yok"))
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="input-frame">', unsafe_allow_html=True)
    LYM_A = st.number_input("LYM_A", value=None, format="%.2f", step=None)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-frame">', unsafe_allow_html=True)
    MON = st.number_input("MON", value=None, format="%.2f", step=None)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-frame">', unsafe_allow_html=True)
    kusma = st.selectbox("Kusma", options=[None, 1, 0], format_func=lambda x: "Seçiniz" if x is None else ("Evet" if x == 1 else "Hayır"))
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="input-frame">', unsafe_allow_html=True)
    solunum_guclugu = st.selectbox("Solunum Güçlüğü", options=[None, 1, 0], format_func=lambda x: "Seçiniz" if x is None else ("Var" if x == 1 else "Yok"))
    st.markdown('</div>', unsafe_allow_html=True)

# Prediction button and validation check
button_clicked = st.button("Tahmin Et", key="predict_button")

if button_clicked:
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
