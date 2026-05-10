import streamlit as st

name = st.text_input("Enter your Name: ", placeholder="Enter Your name here...")
age = st.number_input("Enter your Age: ", value=None, placeholder="Enter your Age here...")
occupation = st.selectbox("Choose Your Occupation", ("Student","Employee", "Businessman","Freelancer"), index=None, accept_new_options=True)
submit = st.button("Submit", type="primary")

if submit:
    if not name or age is None or occupation is None:
        st.warning("Please fill in all the fields.")
    else:
        st.success("✅ Form submitted successfully!")
        st.write(f"Hello, {name}!  Your Age Is: {age} and Your Occupation is {occupation}")