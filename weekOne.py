import streamlit as st
import pandas as pd

# Data Preparation
df = pd.read_csv('weekSatuClean.csv')

st.title("Week One Data Overview")
st.dataframe(df)