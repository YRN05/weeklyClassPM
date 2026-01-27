import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

pages = {
    "Weekly Class PM":[
        st.Page('pages/weekOne.py', title='Week One'),
        st.Page('pages/weekTwo.py', title='Week Two'),
        st.Page('pages/TechTalk.py', title='Tech Talk')
    ]
}

pg = st.navigation(pages)
pg.run()