import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def run():
    st.title("Exploratory Data Analysis")
    st.markdown("Analisis eksploratif dataset resiko diabetes")

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(
        BASE_DIR,
        "data",
        "diabetes_binary_health_indicators_BRFSS2015.csv"
    )

    df = pd.read_csv(DATA_PATH)
    nama_kolom = {
    'Diabetes_binary': 'Diabetes',
    'HighBP': 'High_BP',
    'HighChol': 'High_Chol',
    'CholCheck': 'Chol_Check',
    'BMI': 'BMI',
    'Smoker': 'Smoker',
    'Stroke': 'Stroke',
    'HeartDiseaseorAttack': 'Heart_Disease',
    'PhysActivity': 'Physical_Activity',
    'Fruits': 'Fruits',
    'Veggies': 'Veggies',
    'HvyAlcoholConsump': 'Alcoholic',
    'AnyHealthcare': 'Healthcare',
    'NoDocbcCost': 'No_Doctor_Because_Cost',
    'GenHlth': 'General_Health',
    'MentHlth': 'Mental_Health',
    'PhysHlth': 'Physical_Health',
    'DiffWalk': 'Difficulty_Walking',
    'Sex': 'Sex',
    'Age': 'Age',
    'Education': 'Education',
    'Income': 'Income'
    }

    df.rename(columns = nama_kolom, inplace=True) # Mengganti nama-nama kolom

    st.write(f"Jumlah data: {df.shape[0]} baris")
    st.write(f"Jumlah fitur: {df.shape[1]} kolom")

    st.dataframe(df.head())

    # Distribusi Target
    st.markdown("## Distribusi Target (Diabetes)")

    fig, ax = plt.subplots()
    sns.countplot(x='Diabetes', data=df, ax=ax)
    ax.set_xticklabels(['Tidak Diabetes', 'Diabetes'])
    ax.set_title("Distribusi Kelas Target")
    st.pyplot(fig)

    st.markdown("""
    Terlihat bahwa distribusi kelas target tidak seimbang, 
    di mana jumlah individu tanpa diabetes lebih dominan dibandingkan individu dengan diabetes.
    Kondisi ini menunjukkan bahwa dataset bersifat imbalanced.
    """)

    # Distribusi BMI
    st.markdown("## Distribusi BMI")

    st.subheader('Distribusi BMI berdasarkan Status Diabetes')

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.boxplot(x='Diabetes', y='BMI', data=df, ax=ax)
    ax.set_xlabel('Status Diabetes')
    ax.set_ylabel('BMI')
    ax.set_title('Distribusi BMI berdasarkan Status Diabetes')

    st.pyplot(fig)

    st.markdown("""
    Boxplot ini menunjukkan perbedaan distribusi nilai BMI antara individu dengan dan tanpa diabetes. 
    Terlihat bahwa kelompok dengan diabetes cenderung memiliki nilai median BMI yang lebih tinggi serta sebaran yang lebih lebar. 
    Hal ini mengindikasikan bahwa BMI merupakan salah satu faktor yang berkaitan dengan resiko diabetes, meskipun terdapat tumpang tindih distribusi antar kedua kelompok.
    """)

    # Distribusi Usia
    st.markdown("## Distribusi Kelompok Usia")

    fig, ax = plt.subplots()
    sns.countplot(x='Age', data=df, ax=ax)
    ax.set_title("Distribusi Kategori Usia")
    st.pyplot(fig)

    st.markdown("""
    Variabel usia disajikan dalam bentuk kategori.
    Terlihat bahwa mayoritas data berada pada kelompok usia menengah hingga lanjut,
    yang secara umum memiliki resiko diabetes lebih tinggi.
    """)

    # Korelasi Fitur Numerik
    st.markdown("## Korelasi Antar Fitur")

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(), cmap='coolwarm', linewidths=0.5, ax=ax)
    ax.set_title("Heatmap Korelasi Fitur")
    st.pyplot(fig)

    st.markdown("""
    Heatmap korelasi digunakan untuk melihat hubungan antar fitur numerik.
    Tidak ditemukan korelasi yang sangat tinggi antar fitur, 
    sehingga resiko multikolinearitas terbilang rendah.
    """)

if __name__ == "__main__":
    run()
