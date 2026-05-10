import streamlit as st

st.title("Hello Streamlit!")

profession = st.selectbox("Enter your Profession", ("Student","Employee","Businessman"),
                          index=None,
                          accept_new_options = True)
print(type(profession))
st.write(f"Your Profession Is: {profession}")

st.divider()


video_file = st.file_uploader("Upload Your Video", type=['mp4','mkv'])
print(type(video_file))
if video_file:
    st.video(video_file)
    st.success("Video Uploaded Successfully!")
else:
    st.warning("Please upload a video file.")


st.divider()
image = st.file_uploader("upload your file", type=['jpg','png', 'jpeg'],accept_multiple_files=True)
print(type(image))
if image:
    col = st.columns(len(image))
    for i, image in enumerate(image):
        col[i].image(image)