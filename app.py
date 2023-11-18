import streamlit as st
import pandas as pd
import requests,json
st.title("Predict churn student")
st.text("")
df=pd.read_csv('UnivData1.csv')
st.dataframe(df.sample(30))
st.text("")
st.text("")
df_chart = df.sample(50)
st.bar_chart(data=df_chart.iloc[:,:1],use_container_width=True)

id_input=st.text_input("ID")
age_input=st.text_input("Age")
data={"Inputs":{"data":[{"id":id_input,"age":age_input}]}}
button = st.button('Predict')
if id_input!="" and age_input!="":
    url="http://6c3f0a36-b3d1-4754-81ee-cbf7ba003f0a.southeastasia.azurecontainer.io/score"
    response= requests.post(url,json=data)
    result = json.loads(response.content.decode('utf-8'))
    st.text(result['Results'][0])