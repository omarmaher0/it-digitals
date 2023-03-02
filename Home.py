import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="it-digitals",page_icon=":computer:",layout="wide")



st.subheader("Welcome to IT-DIGITALS! ")

img_center = Image.open("seredited.jpg")
st.image(img_center)

st.sidebar.success("Select a page above.")


#with st.container():
    #st.write("[Learn More >](https://it-digitals.com/)")


def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return  r.json()
#---animmation---
lottie_coding = load_lottieur("https://assets10.lottiefiles.com/packages/lf20_ndlvehgz.json")

st.write('##')
st.write('##')

st.header("""
we're glad to see you here we're here to lend you a hand to get perfect quality at less cost. 
so why are you waiting for? contact with us.
""")



