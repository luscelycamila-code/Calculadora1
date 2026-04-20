import streamlit as st
from truth_table import generar_tabla

st.title("Tabla de Verdad - Lógica Booleana")

expresion = st.text_input("Ejemplo: (p and q) or not r")
if st.button("Generar tabla"):
    if expresion:
        tabla = generar_tabla(expresion)
        st.dataframe(tabla)
    else:
        st.warning("Ingresa una expresión")