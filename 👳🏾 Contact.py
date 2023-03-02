import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

image = Image.open('concat.png')

st.image(image,use_column_width='auto')


def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return  r.json()
#---animmation---
lottie_coding = load_lottieur("https://assets7.lottiefiles.com/private_files/lf30_7z3j6ycb.json")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Giza, Egypt")
        st.write("##")
        st.write("📍 : Hadayek October")
        st.write("📱 : 01001470404 ")
        st.write("📧 : info@it-digitals.com")
    with right_column:
        st_lottie(lottie_coding,height=300)





def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("style/style.css")

#----Contact----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    #--space--
    st.write("##")

    #Documention
    contact_form = """
    <form action="https://formsubmit.co/info@it-digitals.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column,right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()


