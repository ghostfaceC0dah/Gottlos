import streamlit as st

st.set_page_config(page_title="login", page_icon="🤢")

st.title("Log-in")



class Userinput:
    st.text_input("Username/E-mail")
    st.text_input("Password")


st.sidebar.success("Log-in")

def submit_button():
    if st.button("submit"):
        st.write("Form submitted")

submit_button()

 