#Importo las librerias necesarias
import streamlit as st
import pandas as pd
import plotly_express as px

#Leo el archivo y lo defino como un DataFrame de Pandas
df_vehicles = pd.read_csv("C:/Users/Usuario/Downloads/vehicles_us.csv")

# print(df_vehicles.head(5))
# print()
# df.vehicles.info()

st.header("Prueba Encabezado")