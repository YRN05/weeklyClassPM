import streamlit as st
import pandas as pd

# Data Preparation
dfOne = pd.read_csv('weekSatuClean.csv')
dfTwo = pd.read_csv('weekDuaClean.csv')

st.title("Hello World")

st.dataframe(dfOne)
st.dataframe(dfTwo)