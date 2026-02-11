import pickle
import pandas as pd
import streamlit as st
import os
import pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'model_files', 'best_diabetes_model.pkl')

with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

# Streamlit App
def run():

    st.title('Diabetes Risk Prediction')
    st.markdown('Aplikasi ini digunakan untuk memprediksi resiko diabetes berdasarkan indikator kesehatan individu.')

    with st.form('diabetes_form'):
        High_BP = st.selectbox('High Blood Pressure', [0, 1])
        High_Chol = st.selectbox('High Cholesterol', [0, 1])
        Chol_Check = st.selectbox('Cholesterol Check (Last 5 Years)', [0, 1])
        BMI = st.number_input('BMI', min_value=10.0, max_value=60.0, value=25.0)

        Smoker = st.selectbox('Smoker', [0, 1])
        Stroke = st.selectbox('History of Stroke', [0, 1])
        Heart_Disease = st.selectbox('Heart Disease', [0, 1])
        Physical_Activity = st.selectbox('Physical Activity', [0, 1])

        Fruits = st.selectbox('Consume Fruits Regularly', [0, 1])
        Veggies = st.selectbox('Consume Vegetables Regularly', [0, 1])
        Alcoholic = st.selectbox('Alcohol Consumption (Heavy)', [0, 1])
        Healthcare = st.selectbox('Have Healthcare Access', [0, 1])

        No_Doctor_Because_Cost = st.selectbox('Cannot See Doctor Due to Cost', [0, 1])
        General_Health = st.slider('General Health (1 = Excellent, 5 = Poor)', 1, 5, 3)
        Mental_Health = st.slider('Mental Health Days (0–30)', 0, 30, 0)
        Physical_Health = st.slider('Physical Health Days (0–30)', 0, 30, 0)

        Difficulty_Walking = st.selectbox('Difficulty Walking', [0, 1])
        Sex = st.selectbox('Sex (0 = Female, 1 = Male)', [0, 1])
        Age = st.slider('Age Category (1–13)', 1, 13, 8)
        Education = st.slider('Education Level (1–6)', 1, 6, 4)
        Income = st.slider('Income Level (1–8)', 1, 8, 5)

        submit = st.form_submit_button('Predict')


    # Prediction

    if submit:
        data_inf = {
            'High_BP': High_BP,
            'High_Chol': High_Chol,
            'Chol_Check': Chol_Check,
            'BMI': BMI,
            'Smoker': Smoker,
            'Stroke': Stroke,
            'Heart_Disease': Heart_Disease,
            'Physical_Activity': Physical_Activity,
            'Fruits': Fruits,
            'Veggies': Veggies,
            'Alcoholic': Alcoholic,
            'Healthcare': Healthcare,
            'No_Doctor_Because_Cost': No_Doctor_Because_Cost,
            'General_Health': General_Health,
            'Mental_Health': Mental_Health,
            'Physical_Health': Physical_Health,
            'Difficulty_Walking': Difficulty_Walking,
            'Sex': Sex,
            'Age': Age,
            'Education': Education,
            'Income': Income
        }

        df_inf = pd.DataFrame([data_inf])
        st.subheader('Input Data')
        st.dataframe(df_inf)

        pred = model.predict(df_inf)[0]
        prob = model.predict_proba(df_inf)[0][1]

        st.subheader('Prediction Result')

        if pred == 1:
            st.error(f'Model memprediksi individu BERESIKO diabetes')
        else:
            st.success(f'Model memprediksi individu TIDAK berisiko diabetes')

        st.write(f'Probabilitas diabetes: **{prob:.2f}**')

if __name__ == '__main__':
    run()
