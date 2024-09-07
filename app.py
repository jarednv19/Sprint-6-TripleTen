# Importo las librerias necesarias
import streamlit as st
import pandas as pd
import plotly_express as px

# Leo el archivo y lo defino como un DataFrame de Pandas
df_vehicles = pd.read_csv("vehicles_us.csv")

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

st.header("Vehiculos en Estados Unidos")
st.write("El objetivo de este sitio es compartir los hallazgos adquiridos posterior al análisis estadístico del set de información, a través de la visualización de gráficas que demuestran de manera visual la relación entre la información")

histogram = st.checkbox("Construir histograma") # crear un botón //// puede ser checkbox o button
        
if histogram: # al hacer clic en el botón
            # escribir un mensaje
            st.write("Histograma que demuestra la cantidad de vehiculos analizados según su año de salida")
            st.write("Podemos observar que la mayoría de los vehiculos considerados para este análisis cuentan con un año de fabricación del 2000 al presente, dejando en la minoría a aquellos de 1900")
            
            # crear un histograma
            fig = px.histogram(df_vehicles, x="model_year", range_x=[1960, 2024])
        
            # mostrar un gráfico Plotly interactivo
            st.plotly_chart(fig, use_container_width=True)

dispersion_graph = st.button("Construir gráfico de dispersión") # crear un botón //// puede ser checkbox o button
        
if dispersion_graph: # al hacer clic en el botón
            # escribir un mensaje
            st.write("Gráfico de dispersión que compara el rango de precios de los vehiculos listados con su condición actual")
            st.write("Gracias a las ventajas que nos ofrece este tipo de gráficos, encontramos que, a pesar de que todos pueden tener un valor promedio alrededor 50k, los puntos más altos se encuentran en las categorías EXCELLENT y GOOD, llegando a sobrepasar los 300k")
            
            # crear un gráfico de dispersión
            fig = px.scatter(df_vehicles, x="price", y="condition")
        
            # mostrar un gráfico Plotly interactivotr
            st.plotly_chart(fig, use_container_width=True)