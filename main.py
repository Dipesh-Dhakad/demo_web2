import streamlit as st

name = st.text_input("Enter Your Name : ")
fname = st.text_input("Enter a Father Name : ")
ads = st.text_area("Enter a Address : ")
classdata = st.selectbox("Enter Your Class :",(1,2,3,4,5))

button = st.button("OK")
if button :
    st.markdown(f"Name :{name} Father:{fname} Address:{ads} class:{classdata}")

