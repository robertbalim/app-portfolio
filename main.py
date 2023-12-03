import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Roberto Alim")
    content = "Hi! I am Roberto Alim. I graduated in 2006 with a Bachelor of Science in Computer Science degree on my sleeves. I am a Software Developer who excels in Python programming, specializes in the Django framework, and possesses extensive experience in database management. My diverse portfolio showcases my ability to develop tailored solutions for various business needs, making me a valuable asset in the field of software development."
    st.info(content)
