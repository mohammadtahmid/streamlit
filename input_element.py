import streamlit as st

st.title("Input Your Information", anchor=False)
st.divider()

name = st.text_input("Enter Your Name: ",placeholder="Enter your Name")

age = st.number_input("Enter your Age: ", min_value=0, step=1, value=None, placeholder="Enter Your Age: ")

password = st.text_input("Enter Your Password: ",placeholder="Enter your password", type="password")

pressed = st.button("Enter to Confirm",type="primary")

if pressed:
    st.write(f"Your Name Is {name} and Your Age Is: {age}")