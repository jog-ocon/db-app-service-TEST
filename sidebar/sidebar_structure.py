import streamlit as st
from sidebar.content import sidebar_choices

# Sidebar for navigation
st.sidebar.title("Sommaire")
choice = sidebar_choices
sidebar_choice = st.sidebar.radio("Aller vers la page", choice)

