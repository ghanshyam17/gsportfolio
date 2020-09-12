
import streamlit as st

#Text/TItle
st.title("Ghanshyam's Portfolio")

# Header/subheader
st.sidebar.header("Data Science Projects")
st.sidebar.subheader("Stock Market Analysis")
st.sidebar.subheader("Geospatial Analysis")
st.sidebar.subheader("Market Basket Analysis")
st.sidebar.subheader("COVID-19 Tracker")

#Text
st.text("Stock Market Analysis and Insights")
st.write("Description of Stock market")
st.write(range(10))


#Selecions
st.selectbox("Choose the proeject to display",['Stock Market Analysis',
    'Geospatial Analysis','Market Basket Analysis','COVID-19 Tracker'])
viztype=st.multiselect("Choose the data to be used",['Bar Plot','Histogram','Line Graph'])


level = st.slider("what is your level",1,5)

if st.button("About"):
    st.text("Data Science Consultant")

review = st.text_input("Send your review", "type here")

if st.button("Submit"):
    feedback = review.title()

