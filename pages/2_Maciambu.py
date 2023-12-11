
import time
import numpy as np
import streamlit as st
from streamlit.hello.utils import show_code
from matplotlib import pyplot as plt
import requests
import pandas as pd

key='4c09891a71d24ce289891a71d29ce27f'

station='IPALHO4'
data='20231211'

reqc = requests.get('https://api.weather.com/v2/pws/history/hourly?stationId='+station+'&format=json&units=m&date='+data+'&apiKey='+key)

#Converter em dataframe e salvar em csv
df=pd.DataFrame(reqc.json()['observations']);
df2=pd.json_normalize(df['metric'])

fig, ax = plt.subplots()
ax.plot(2*df2['windspeedAvg']/3.6)

def plotting_demo():
    st.pyplot(fig)
    st.button("Re-run")


st.set_page_config(page_title="Kitezone - Maciambu 2 - IPALHO4", page_icon="📈")
st.markdown("# Maciambu2")
st.sidebar.header("Maciambu2")
st.write(
    """Monitoramento das condições meteorológicas em Maciambú!"""
)

plotting_demo()

show_code(plotting_demo)
