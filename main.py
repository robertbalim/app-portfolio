import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Roberto Alim")
    content = """
        Hi! I am Roberto Alim. I graduated in 2006 with a Bachelor of Science in Computer Science degree from 
        the STI College Parañaque Philippines. I am a Software Developer who excels in Python programming, 
        specializes in the Django framework, and possesses extensive experience in database management. 
        My diverse portfolio showcases my ability to develop tailored solutions for various business needs, 
        making me a valuable asset in the field of software development.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me! 
You can also find me on different social media platform
"""
st.write(content2)