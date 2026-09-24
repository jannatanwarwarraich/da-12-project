import streamlit as st
import pickle

st.set_page_config(page_title="da-12-project", page_icon= "💎")
st.header("DA-12-Project")


with open("model.pkl", "rb") as file:
  model = pickle.load(file)

  yoe = st.number_input("Year Of Experience", min_value=0.0, max_value=10.0, step=0.5, value=2.0)
  if st.button("Predict"):
    predication = model.predict([[yoe]])  
    st.success(predication)     
