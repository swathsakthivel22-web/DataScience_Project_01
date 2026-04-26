import streamlit as st
import pandas as pd

st.title("EDA Project")

st.write("Upload your dataset")

file = st.file_uploader("Choose CSV file")

if file:
    df = pd.read_csv(file)
    
    st.write("### Data Preview")
    st.write(df.head())
    
    st.write("### Data Info")
    st.write(df.describe())
    
    st.write("### Columns")
    st.write(df.columns)
