import streamlit as st

def addition(a,b):
  return(a+b)
st.title("Little Calculator")
a = st.number_input()
b = st.number_input()

