import streamlit as st
from streamlit_lottie import st_lottie
import requests

#st.title('About us')

def load_lottieur(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return  r.json()
lottie_coding_network = load_lottieur("https://assets6.lottiefiles.com/packages/lf20_uatosho5.json")

with st.container():
    #st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header(" Our 🖱 Services")
        st.write("##")
    with right_column:
        st.empty()

lottie_coding_outdoor = load_lottieur("https://assets3.lottiefiles.com/packages/lf20_daupuwdu.json")
lottie_coding_fiber = load_lottieur("https://assets9.lottiefiles.com/packages/lf20_1ygUTe.json")
lottie_coding_cable = load_lottieur("https://assets10.lottiefiles.com/packages/lf20_ndlvehgz.json")
lottie_coding_indoor = load_lottieur("https://assets4.lottiefiles.com/packages/lf20_wEt2nn.json")
lottie_coding_it = load_lottieur("https://assets4.lottiefiles.com/packages/lf20_COamaylcrm.json")
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader('''
            - Installation  Network
            ''')
    with right_column:
        st_lottie(lottie_coding_network,height=300)


with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader('''
            - It Services''')
    with right_column:
        st_lottie(lottie_coding_it,height=300)

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader('''
            - CCTV system''')
    with right_column:
        st.empty()

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st_lottie(lottie_coding_indoor, height=300)
    with right_column:
        st_lottie(lottie_coding_outdoor, height=300)


with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader('''
        - Fiber & UTP
        ''')
    with right_column:
        st.empty()

with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st_lottie(lottie_coding_fiber, height=300)
    with right_column:
        st_lottie(lottie_coding_cable, height=300)