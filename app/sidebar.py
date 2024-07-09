import streamlit as st
from constants import SIDEBAR_OPTIONS

def sidebar():
    st.sidebar.title("Navigation")
    selected_option = st.sidebar.selectbox("Choose an option", SIDEBAR_OPTIONS)
    return selected_option