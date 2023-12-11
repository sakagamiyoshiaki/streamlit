import time
import numpy as np
import streamlit as st
from streamlit.hello.utils import show_code
from matplotlib import pyplot as plt
import requests
import pandas as pd

dd=pd.date_range(start='9/16/2022', freq='H', periods=1000000)

key='4c09891a71d24ce289891a71d29ce27f'
station='IPALHO4'
df3=pd.DataFrame([])

for i in range(0,24):
  data=dd.year.astype(str)[i*24]+dd.month.map("{:02}".format)[i*24]+dd.day.map("{:02}".format)[i*24]
  reqc = requests.get('https://api.weather.com/v2/pws/history/hourly?stationId='+station+'&format=json&units=m&date='+data+'&apiKey='+key)

  df=pd.DataFrame(reqc.json()['observations']);
  df2=pd.json_normalize(df['metric'])
  df3=pd.concat([df3,df2],axis=0)

df3.index=dd[:len(df3)]

fig, ax = plt.subplots()
ax.plot(2*df3['windspeedAvg']/3.6)

def plotting_demo():
    st.pyplot(fig)
    st.button("Re-run")


st.set_page_config(page_title="Kitezone - Maciambu - IPALHO4", page_icon="📈")
st.markdown("# Maciambu")
st.sidebar.header("Maciambu")
st.write(
    """Monitoramento das condições meteorológicas em Maciambú!"""
)

plotting_demo()

show_code(plotting_demo)

