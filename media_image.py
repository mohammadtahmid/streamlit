import streamlit as st 
image = st.file_uploader("Upload your Image at most 3 images", type=['jpg','png','jpeg'], accept_multiple_files=True)
if image and len(image) > 3:
    st.error("Please upload at most 3 images.")
elif image and len(image) == 3:
    st.success("✅ Images Uploaded Successfully!")
    col = st.columns(3)
    for i, img in enumerate(image):
        col[i].image(img)
    