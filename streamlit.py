# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 15:23:11 2020

@author: alexa
"""
#Creating data visualizations with the streamlit package in python

#Packages
import streamlit as st

import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import time
import altair as alt

@st.cache
def load_hospitals():
    df_hospital_2 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_hospital_2.csv')
    return df_hospital_2

@st.cache
def load_inatpatient():
    df_inpatient_2 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_inpatient_2.csv')
    return df_inpatient_2

@st.cache
def load_outpatient():
    df_outpatient_2 = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/AHI_STATS_507/main/Week13_Summary/output/df_outpatient_2.csv')
    return df_outpatient_2


#Things that's going on in streamlit browser page
st.title('Hospital Data Analysis and Visualization')

df_hospital_2=load_hospitals()
df_inpatient_2=load_inatpatient()
df_outpatient_2=load_outpatient()


###New York Hospitals
hospitals_ny=df_hospital_2[df_hospital_2['state']=='NY']

st.header('New York Hospitals')
st.markdown('Here are some quick visualizations from New York Hospitals')

st.subheader('Hospital Types')
bar1=hospitals_ny['hospital_type'].value_counts().reset_index()
st.dataframe(bar1)
st.markdown('As you can see, there are many more hospitals in New York that cater to acute care and psychiatry versus hospitals that are catered specifically for children.')

fig2 = px.bar(bar1, x='index', y='hospital_type')
st.plotly_chart(fig2)

st.subheader('Hospital Ownership')
bar2=hospitals_ny['hospital_ownership'].value_counts().reset_index()
st.dataframe(bar2)

fig = px.pie(bar2, values='hospital_ownership', names='index')
st.plotly_chart(fig)
st.markdown('The most common hospital ownership is from voluntary private hospitals that are non-profit, while the least common in New York hospitals are owned by the Department of Defense with just a singular hospital.')

hospitals_gps = hospitals_ny['location'].str.strip('()').str.split(' ', expand=True).rename(columns={0: 'Point', 1:'lon', 2:'lat'})
hospitals_gps['lon'] = hospitals_gps['lon'].str.strip('(')
hospitals_gps = hospitals_gps.dropna()
hospitals_gps['lon'] = pd.to_numeric(hospitals_gps['lon'])
hospitals_gps['lat'] = pd.to_numeric(hospitals_gps['lat'])

st.map(hospitals_gps)


##Nationwide Hospitals
st.header('US Hospitals')
st.markdown('Here are some quick visualizations from United States Hospitals')

st.subheader('Hospital Types')
bar3=df_hospital_2['hospital_type'].value_counts().reset_index()
st.dataframe(bar3)
st.markdown('Similar to New York hospitals, acute care hospitals are the most common hospital type nationwide, but we can also see that critical care access hospitals take the second most common place spot instead of psychiatric hospitals. There is also the additional field of acute care hospitals that are under the jurisdiction of the Department of Defense, which is not present in New York.')

fig2 = px.bar(bar3, x='index', y='hospital_type')
st.plotly_chart(fig2)

st.subheader('Hospital Ownership')
bar4=df_hospital_2['hospital_ownership'].value_counts().reset_index()
st.dataframe(bar4)

fig = px.pie(bar4, values='hospital_ownership', names='index')
st.plotly_chart(fig)
st.markdown('Voluntary non-profit private hospitals are the most common type of hospital ownership, similarly to that of New York, but nationwide we see additional fields not present in New York hospitals like Tribal and Physician owned hospitals.')

hospitals_gps = df_hospital_2['location'].str.strip('()').str.split(' ', expand=True).rename(columns={0: 'Point', 1:'lon', 2:'lat'})
hospitals_gps['lon'] = hospitals_gps['lon'].str.strip('(')
hospitals_gps = hospitals_gps.dropna()
hospitals_gps['lon'] = pd.to_numeric(hospitals_gps['lon'])
hospitals_gps['lat'] = pd.to_numeric(hospitals_gps['lat'])
st.map(hospitals_gps)




