import streamlit as st
import pandas as pd
import plotly.express as px

GV_df = pd.read_csv('GV_citas_medicas.csv')

st.title('GV - Dashboard de Gestión de Citas Médicas')

st.subheader('GV - Citas por Especialidad')
GV_fig1 = px.bar(
    GV_df['especialidad'].value_counts(),
    labels={'value': 'Cantidad'}
)
st.plotly_chart(GV_fig1)

st.subheader('GV - Estado de las Citas')
GV_fig2 = px.pie(
    GV_df,
    names='estado'
)
st.plotly_chart(GV_fig2)

GV_df['fecha'] = pd.to_datetime(GV_df['fecha'])
GV_df['mes'] = GV_df['fecha'].dt.month

GV_citas_mes = GV_df.groupby('mes').size().reset_index(name='cantidad')

st.subheader('GV - Citas por Mes')
GV_fig3 = px.line(
    GV_citas_mes,
    x='mes',
    y='cantidad',
    markers=True
)
st.plotly_chart(GV_fig3)