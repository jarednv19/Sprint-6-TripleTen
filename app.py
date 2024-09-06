#Importo las librerias necesarias
import streamlit as st
import pandas as pd
import plotly_express as px

#Leo el archivo y lo defino como un DataFrame de Pandas
df_vehicles = pd.read_csv("C:/Users/Usuario/Downloads/vehicles_us.csv")

# Corrección de datos
df_vehicles["model_year"] = df_vehicles["model_year"].fillna(0).astype(int)
df_vehicles["cylinders"] = df_vehicles["cylinders"].fillna(0).astype(int)
df_vehicles["odometer"] = df_vehicles["odometer"].fillna(0).astype(int)
df_vehicles["paint_color"] = df_vehicles["paint_color"].fillna("Unknown")
df_vehicles["is_4wd"] = df_vehicles["is_4wd"].fillna(0).astype(int)

df_vehicles["model_year"] = df_vehicles["model_year"].astype(int)
df_vehicles["cylinders"] = df_vehicles["cylinders"].astype(int)
df_vehicles["odometer"] = df_vehicles["odometer"].astype(int)
df_vehicles["date_posted"] = pd.to_datetime(df_vehicles["date_posted"], format = "%Y-%m-%d")

print("Información General de Archivo")
print()
df_vehicles.info()
print()
print("Valores duplicados: ", df_vehicles.duplicated().sum())
print()
print("Valores ausentes: ", df_vehicles.isna().sum())
print()
print(df_vehicles.sample(5))

# st.header("Prueba Encabezado")
# histogram = st.checkbox('Construir histograma') # crear un botón //// puede ser checkbox o button
        
# if histogram: # al hacer clic en el botón
#             # escribir un mensaje
#             st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
#             # crear un histograma
#             fig = px.histogram(df_vehicles, x="odometer")
        
#             # mostrar un gráfico Plotly interactivo
#             st.plotly_chart(fig, use_container_width=True)

# dispersion_graph = st.button('Construir gráfico de dispersión') # crear un botón //// puede ser checkbox o button
        
# if dispersion_graph: # al hacer clic en el botón
#             # escribir un mensaje
#             st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
#             # crear un gráfico de dispersión
#             fig = px.scatter(df_vehicles, x="odometer")
        
#             # mostrar un gráfico Plotly interactivo
#             st.plotly_chart(fig, use_container_width=True)