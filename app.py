import pandas as pd
import plotly.express as px
import straemlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_checkbox = st.button('Construir histograma')
disp_checkbox = st.button('Construir grafico de dispersion')

# Checkbox histograma
if hist_checkbox: 
  st.write('Creacion de un histograma para el conjunto de datos de anuncios de ventas de coches')
  fig = px.histogram(car_data, x='odometer')
  st.plotly_chart(fig, use_container_width=True)
  
# Checkbox grafico de dispersion
if disp_checkbox: 
  st.write('Creacion de un grafico de dispersion para el conjunto de datos de anuncios de ventas de coches')
  fig = px.scatter(car_data, x='odometer')
  st.plotly_chart(fig, use_container_width=True)