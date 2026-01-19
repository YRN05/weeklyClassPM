import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

pages = {
    "Weekly Class PM":[
        st.Page('weekOne.py', title='Week One'),
        st.Page('weekTwo.py', title='Week Two')
    ]
}

pg = st.navigation(pages)
pg.run()