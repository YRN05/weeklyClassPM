import streamlit as st
import pandas as pd

# Data Preparation
df = pd.read_csv('weekDuaClean.csv')

st.title("Week Two Data Overview")
st.dataframe(df)