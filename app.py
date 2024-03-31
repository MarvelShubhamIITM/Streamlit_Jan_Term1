import streamlit as st

def addition(a,b):
  return(a+b)
st.title("Little Calculator")
a = st.number_input("Input your first number : ")
b = st.number_input("Input your second number : ")

st.write(addition(a,b))
st.write(answer)
