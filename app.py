import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

st.title("Predicción de diabetes en mujeres de 21 años o mas.")
st.sidebar.title("Predicción de diabetes en mujeres de 21 años o mas.")

st.markdown("Esta aplicación es un Streamlit dashboard el cual analiza la informacion de prediccion de la enfermedad de diabetes en mujeres mayores a 21 años.")
st.sidebar.markdown("Esta aplicación es un Streamlit dashboard el cual analiza la informacion de prediccion de la enfermedad de diabetes en mujeres mayores a 21 años.")

st.image("img/diabetes.jpg")
st.markdown("La diabetes es una enfermedad en la que los niveles de glucosa (azúcar) de la sangre están muy altos. La glucosa proviene de los alimentos que consume. La insulina es una hormona que ayuda a que la glucosa entre a las células para suministrarles energía. En la diabetes tipo 1, el cuerpo no produce insulina. En la diabetes tipo 2, la más común, el cuerpo no produce o no usa la insulina de manera adecuada. Sin suficiente insulina, la glucosa permanece en la sangre.")



DATA_URL = ("Dataset/diabetes2.csv")

@st.cache(persist = True)
def load_data():
    data = pd.read_csv(DATA_URL)
    return data

data = load_data()


select = st.sidebar.selectbox('Tipo de visualizacion', ['Histograma', 'Grafica de pastel','Tabla de datos','Mapa coronavirus'], key = '1')
diagnostico_count = data['Outcome'].value_counts()
diagnostico_count = pd.DataFrame({'Negativo(0)/Positivo(1)': diagnostico_count.index, 'Cantidad de personas': diagnostico_count.values})

if not st.sidebar.checkbox("Mostrar", True):
    if select == 'Histograma':
        st.markdown("### Numero de personas diagnosticada y no con diabetes.")
        fig = px.bar(diagnostico_count, x = 'Negativo(0)/Positivo(1)', y = 'Cantidad de personas', color = 'Cantidad de personas', height = 500)
        st.plotly_chart(fig)
    elif select == 'Grafica de pastel':
        st.markdown("### Numero de personas diagnosticada y no con diabetes.")
        fig = px.pie(diagnostico_count, values = 'Cantidad de personas', names = 'Negativo(0)/Positivo(1)')
        st.plotly_chart(fig)
    elif select == 'Tabla de datos':
        st.subheader("A continuación se muestran todos nuestros datos en una tabla.")
        data
        st.subheader("¿Que significa cada atributo?")
        st.text("A continuación les explico un poco del nombre de las columnas de mi dataset:")
        st.text("1.   Embarazos (Pregnancies)")
        st.text("2.   Glucosa (Glucose)")
        st.text("3.   Presión arterial (BloodPressure)")
        st.text("4.   Grosor de la piel (SkinThickness)")
        st.text("5.   Insulina (Insulin)")
        st.text("6.   Índice de masa corporal (BMI)")
        st.text("7.   DiabetesPedigreeFunction")
        st.text("8.   Edad (Age)")
        st.text("9.   Resultado (Outcome)")
    elif select == 'Mapa coronavirus':
        DATA_URL2 = ("Dataset/coronavirus.csv")

        @st.cache(persist = True)
        def load_data():
            data2 = pd.read_csv(DATA_URL2)
            return data2

        data2 = load_data()

        dataChido = data2.rename(columns={'Lat':'lat','Long':'lon'})
        st.subheader("A continuación se muestran todos nuestros datos de un pequeño dataset que encontramos para poder visualizar donde han sucedido las muertes por coronavirus.")
        dataChido
        st.subheader('Mostramos un mapa de todos los paises donde hubo muertes por coronavirus')
        st.map(dataChido)
