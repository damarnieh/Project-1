# Prediksi Resiko Diabetes Menggunakan 5 Model Machine Learning

## Repository Outline

Repository ini berisi seluruh file yang digunakan dalam proses analisis, pemodelan, hingga deployment model machine learning untuk memprediksi resiko diabetes.  
description.md - Deskripsi singkat dan ringkasan project  
README.md - Dokumentasi utama project  
P1M2_Muhammad_Damar.ipynb - Notebook training dan evaluasi model  
P1M2_Muhammad_Damar_inf.ipynb - Notebook inference menggunakan model terbaik  

```
deployment/
├── src/
│ ├── streamlit_app.py - Entry point aplikasi Streamlit
│ ├── eda.py - Halaman eksplorasi data (EDA)
│ └── predict.py - Halaman prediksi resiko diabetes
├── model_files/
│ └── best_diabetes_model.pkl - Model terbaik hasil training
├── data/
│ └── diabetes_binary_health_indicators_BRFSS2015.csv
├── requirements.txt - Daftar library yang digunakan
└── Dockerfile - Konfigurasi deployment menggunakan Docker
```
url.txt - URL dataset, model, dan deployment

## Problem Background
Diabetes merupakan salah satu penyakit kronis yang prevalensinya terus meningkat dan dapat menyebabkan berbagai komplikasi serius apabila tidak terdeteksi sejak dini. Oleh karena itu, dibutuhkan suatu pendekatan berbasis data untuk membantu mengidentifikasi individu yang memiliki resiko diabetes secara lebih awal.

Project ini bertujuan untuk membangun model machine learning yang mampu memprediksi resiko diabetes berdasarkan indikator kesehatan dan gaya hidup individu, sehingga dapat digunakan sebagai alat skrining awal dalam konteks kesehatan masyarakat.

## Project Output
- Model machine learning untuk klasifikasi resiko diabetes
- Aplikasi web berbasis Streamlit yang menampilkan:
  - Exploratory Data Analysis (EDA)
  - Fitur prediksi resiko diabetes untuk data individu baru
- Model deployment yang dapat diakses melalui platform HuggingFace

## Data
Dataset yang digunakan berasal dari Behavioral Risk Factor Surveillance System (BRFSS) 2015, yang berisi indikator kesehatan terkait diabetes.
Karakteristik dataset:
- Jumlah observasi: lebih dari 200.000 baris
- Jumlah fitur: 21 fitur input dan 1 target
- Target: status diabetes (binary classification)
- Mayoritas fitur berbentuk numerik dan kategorikal diskrit
- Dataset bersifat **imbalanced**, dengan proporsi kelas non-diabetes lebih dominan
- Data duplikat dihapus untuk menjaga kualitas dan keunikan observasi

## Method
Project ini menggunakan pendekatan Supervised Learning dengan tujuan klasifikasi.

Tahapan utama yang dilakukan:
1. Exploratory Data Analysis (EDA)
2. Feature Engineering:
   - Train-test split dengan stratifikasi
   - Penanganan outlier menggunakan Winsorization
   - Scaling menggunakan RobustScaler
3. Pemodelan menggunakan beberapa algoritma:
   - K-Nearest Neighbors (KNN)
   - Support Vector Machine (SVM)
   - Decision Tree
   - Random Forest
   - Gradient Boosting
4. Evaluasi model menggunakan Cross Validation
5. Hyperparameter tuning pada model terbaik
6. Model inference menggunakan data baru
7. Model deployment menggunakan Streamlit dan Docker

Metrik utama yang digunakan adalah Recall, mengingat pentingnya meminimalkan kesalahan false negative dalam konteks kesehatan.

## Stacks
- Bahasa Pemrograman: Python
- Library:
  - pandas
  - numpy
  - scikit-learn
  - imbalanced-learn
  - matplotlib
  - seaborn
  - plotly
  - streamlit
- Tools & Platform:
  - Jupyter Notebook
  - Docker
  - HuggingFace Spaces

## Reference
- Dataset BRFSS 2015
- Deployment Docs: https://docs.streamlit.io/develop/api-reference
- Pandas Docs: https://pandas.pydata.org/docs/user_guide/index.html
- Scikit-Learn Docs: https://scikit-learn.org/stable/index.html
- Imbalanced-Learn Docs: https://imbalanced-learn.org/stable/
- Url Deployment: https://huggingface.co/spaces/J1nTomank/P1M2_Muhammad_Damar_Model
- Url Dataset: https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset/data?select=diabetes_binary_health_indicators_BRFSS2015.csv
- Url File Model: https://drive.google.com/drive/folders/1_7nywyeDbhK7r0lvdCKXTNzOolk2APgc?usp=drive_link

---

**Notes**
Untuk file deploy, mohon buka pada folder P1M2_Muhammad_Damar_ModelNew ya. Terima Kasih.