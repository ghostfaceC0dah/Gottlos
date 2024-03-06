import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="login", page_icon="☖")

st.title("Log-in")



class Userinput:
    st.text_input("Username/E-mail")
    st.text_input(
        "password", 
        type="password"
    )

    def pass_test(password, username):
        while True:
            if True:
                break
            pass
    


st.sidebar.success("Log-in")

def submit_button():
    if st.button("submit"):
        st.write("Form submitted")

submit_button()

 