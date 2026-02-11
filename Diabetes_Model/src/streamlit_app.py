import streamlit as st
import eda, predict

with st.sidebar:
    st.title('Navigation')
    selection = st.radio('Go to Page', ['EDA', 'Prediction'])
    st.markdown('About')
    st.markdown('This page is useful for predicting whether you are at risk of diabetes or not.')
    
if selection == 'EDA':
    eda.run()
elif selection == 'Prediction':
    predict.run()