import streamlit as st

<<<<<<< HEAD
st.title("Input your Information", anchor=False)
st.divider()

name = st.text_input("Enter your Name: ", placeholder="Enter your name here...")

print(type(name))
st.write(f"Hello, {name}!")

st.divider()

age = st.number_input("Enter Your Age", value=None, placeholder="Enter your Age here...")
print(type(age))
st.write(f"Your Age is: {age}")

password = st.text_input("Enter Your Password: ",type="password", placeholder="Enter your password here...")
print(type(password))
st.write(f"Your Password Is: {password}")

st.header("Enter your another section")



profession = st.selectbox("Choose Your Profession",("Student", "Employee", "Businessman") )
st.write(f"Select Your Profession: {profession}")
print(type(profession))
=======
st.title("Input Your Information", anchor=False)
st.divider()

name = st.text_input("Enter Your Name: ",placeholder="Enter your Name")

age = st.number_input("Enter your Age: ", min_value=0, step=1, value=None, placeholder="Enter Your Age: ")

password = st.text_input("Enter Your Password: ",placeholder="Enter your password", type="password")

pressed = st.button("Enter to Confirm",type="primary")

if pressed:
    st.write(f"Your Name Is {name} and Your Age Is: {age}")
>>>>>>> 90f47943f8a7448eff8b4365654f60cfa92133fb
