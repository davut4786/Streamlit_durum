import streamlit as st
import pickle
import pandas as pd

# CSS to center-align the title and style the button
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
    </style>
""", unsafe_allow_html=True)

# Streamlit title with center alignment
st.markdown('<h1 class="title">Hastalık Durumu Tahmin Uygulaması</h1>', unsafe_allow_html=True)

# Model loading (rf_model.pkl file path)
model_path = "rf_model.pkl"
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Input fields for user data
tur = st.selectbox("**Tür**", options=[1, 0], format_func=lambda x: "Köpek" if x == 1 else "Kedi")

# Arrange inputs in rows of four with spacing using st.columns
col1, col2, col3, col4 = st.columns(4, gap="large")
with col1:
    GRAN = st.number_input("**GRAN**", value=None, format="%.2f", step=None)
    HCT = st.number_input("**HCT**", value=None, format="%.2f", step=None)
    MCV = st.number_input("**MCV**", value=None, format="%.2f", step=None)
    inkordinasyon = st.selectbox("**İnkordinasyon**", options=[None, 1, 0], format_func=lambda x: "Seçiniz" if x is None else ("Var" if x == 1 else "Yok"))

with col2:
    GRAN_A = st.number_input("**GRAN_A**", value=None, format="%.2f", step=None)
    MCH = st.number_input("**MCH**", value=None, format="%.2f", step=None)
    RDW = st.number_input("**RDW**", value=None, format="%.2f
