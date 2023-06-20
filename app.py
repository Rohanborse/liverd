"""
@author: Rohan Borse & Vikas Prajapati (#Arjun)
"""

import streamlit as st
import pickle
import pandas as pd
import warnings

warnings.filterwarnings('ignore')

model = pickle.load(open('random_forest_model.pkl', 'rb'))


def preprocess_input(age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase,
                     alamine_aminotransferase, aspartate_aminotransferase, total_proteins, albumin,
                     albumin_and_globulin_ratio):
    # Perform any preprocessing steps here
    data = [[age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase,
             alamine_aminotransferase, aspartate_aminotransferase, total_proteins, albumin,
             albumin_and_globulin_ratio]]
    values = data
    return values


def predict(values):
    prediction = model.predict(values)
    return prediction


def main():
    html_back = """
          <style>
    body {
        background-image: url('https://as1.ftcdn.net/v2/jpg/04/40/94/86/1000_F_440948657_qUH8MHiLNIkhXnbv7TAc1M2A7rVwc9KT.jpg');
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-size: 100% 100%;
    }
    </style>"""
    st.markdown(html_back, unsafe_allow_html=True)
  
    html_title = """
    <h1 style="color:red;"><b><u>LIVER DISEASE PREDICTION</u></b></h1>
    """
  
    st.markdown(html_title, unsafe_allow_html=True)
  
  
   



    age = st.number_input("Age", min_value=0, step=1)
    gender = st.radio("Gender", ['Male', 'Female'])
    total_bilirubin = st.number_input("Total Bilirubin", min_value=0.0, step=0.1)
    direct_bilirubin = st.number_input("Direct Bilirubin", min_value=0.0, step=0.1)
    alkaline_phosphotase = st.number_input("Alkaline Phosphotase", min_value=0, step=1)
    alamine_aminotransferase = st.number_input("Alamine Aminotransferase", min_value=0, step=1)
    aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase", min_value=0, step=1)
    total_proteins = st.number_input("Total Proteins", min_value=0.0, step=0.1)
    albumin = st.number_input("Albumin", min_value=0.0, step=0.1)
    albumin_and_globulin_ratio = st.number_input("Albumin and Globulin Ratio", min_value=0.0, step=0.1)

    if st.button("Predict"):
        values = preprocess_input(age, 1 if gender == "Male" else 0, total_bilirubin, direct_bilirubin,
                                  alkaline_phosphotase, alamine_aminotransferase, aspartate_aminotransferase,
                                  total_proteins, albumin, albumin_and_globulin_ratio)

        prediction = predict(values)
        if prediction[0]==1.0:
          liver = "You have Liver Disease. 😟"
        else:
          liver = "You don't have Liver Disease. 😃"

        st.success(liver)


if __name__ == '__main__':
    main()
