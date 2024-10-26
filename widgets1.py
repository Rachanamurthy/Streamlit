import streamlit as st
import pandas as pd

st.title("Streamlit input statement.")

## TEXT_INPUT FIELD

name= st.text_input("Enter your name")
if name:
    st.write(f"Hello {name} ! Please select your age.")

## SLIDER FIELD

age= st.slider("select your age:",0,25,15)
st.write(f"your age is {age}.")

## SELECTBOX FIELD


options= ["English","Kannada","Hindi","Tamil"]
choice= st.selectbox("Choose your fav lang",options)
st.write(f"You selected {choice}")

## UPLOAD CSV FILE

data = {
    "Name": ['jack','jill','rach','hash'],
    "Age" : [45,26,21,25]
}
df= pd.DataFrame(data)
st.write(df)
df.to_csv("sample.csv")
uploaded_file = st.file_uploader("Choose your csv file",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)