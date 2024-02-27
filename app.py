import streamlit as st


st.title("Log-in")



class Userinput:
    st.text_input("Username/E-mail")
    st.text_input("Password")


st.sidebar.success("Men")

def submit_button():
    if st.button("submit"):
        st.write("Form submitted")

submit_button()

 