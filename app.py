import streamlit as st
import os
import sys
from src.exception import CustomException
st.set_page_config(layout="wide")
st.markdown(
    """
    <style>
    body {
        zoom: 90%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
from PIL import Image
import os
from src.Main import customerchurn

with open('style/final.css') as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
imcol1, imcol2, imcol3 = st.columns((4,5,3))
with imcol1:
    st.write("")
with imcol2:
    st.image('image/ds.png')

with imcol3:
    st.write("")
st.markdown("<p style='text-align: center; color: black; font-size:23px;'><span style='font-weight: bold'>Learn to Build Industry Standard Data Science Applications</span></p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: blue;margin-top: -10px ;font-size:20px;'><span style='font-weight: bold'>MLOPS Built On Google Cloud and Streamlit</span></p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: black; font-size:20px;'><span style='font-weight: bold'>Problem Statement:</span>Develop a Retail Machine Learning Applications (MLOPS): Customer Churn: Who is Going to Churn, When the Churn will Occur, Why it Occurs, and How to Prevent?</p>", unsafe_allow_html=True)
st.markdown("<hr style=height:2.5px;margin-top:0px;background-color:gray;>",unsafe_allow_html=True)

#---------Side bar-------#
with st.sidebar:
    selected = st.selectbox("",['Machine Learning'],key='text')
    Library = st.selectbox("",
                     ["Library Used","Streamlit","Image","Pandas","Requests"],key='text1')
    Gcp_cloud = st.selectbox("",
                     ["GCP Services Used","VM Instance","Computer Engine","Cloud Storage"],key='text2')
    st.markdown("## ")
    href = """<form action="#">
            <input type="submit" value="Clear/Reset" />
            </form>"""
    st.sidebar.markdown(href, unsafe_allow_html=True)
    st.markdown("# ")
    st.markdown("# ")
    st.markdown("# ")
    st.markdown("# ")
    st.markdown("# ")
    st.markdown("<p style='text-align: center; color: White; font-size:20px;'>Build & Deployed on<span style='font-weight: bold'></span></p>", unsafe_allow_html=True)
    s1,s2=st.columns((2,2))
    with s1:
        st.markdown("### ")
        st.image('image/002.png')
    with s2:    
        st.markdown("### ")
        st.image("image/oie_png.png")

#--------------function calling-----------#
if __name__ == "__main__":
    try:
        if selected == 'Machine Learning':
            customerchurn()
    except BaseException as e:
        pass