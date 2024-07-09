# app/main.py

import streamlit as st
from sidebar import sidebar

def run_app():
    st.title("Simple Streamlit App")

    # Sidebar navigation
    selected_option = sidebar()

    # Display selected option
    st.write(f"You selected: {selected_option}")