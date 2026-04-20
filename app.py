import streamlit as st
from truth_table import generar_tabla

st.set_page_config(page_title="Calculadora Lógica", page_icon="🧮")

st.title("🧮 Calculadora Lógica")

# Estado de la expresión
if "expresion" not in st.session_state:
    st.session_state.expresion = ""

# Mostrar pantalla
st.session_state.expresion = st.text_input("Pantalla", st.session_state.expresion)

# FUNCIONES
def agregar(valor):
    st.session_state.expresion += valor

def limpiar():
    st.session_state.expresion = ""

def borrar():
    st.session_state.expresion = st.session_state.expresion[:-1]

# FILA 1
c1, c2, c3, c4 = st.columns(4)
c1.button("p", on_click=agregar, args=("p",))
c2.button("q", on_click=agregar, args=("q",))
c3.button("r", on_click=agregar, args=("r",))
c4.button("C", on_click=limpiar)

# FILA 2
c5, c6, c7, c8 = st.columns(4)
c5.button("(", on_click=agregar, args=("(",))
c6.button(")", on_click=agregar, args=(")",))
c7.button("NOT", on_click=agregar, args=(" not ",))
c8.button("⌫", on_click=borrar)

# FILA 3
c9, c10, c11, c12 = st.columns(4)
c9.button("AND", on_click=agregar, args=(" and ",))
c10.button("OR", on_click=agregar, args=(" or ",))
c11.button("True", on_click=agregar, args=("1",))
c12.button("False", on_click=agregar, args=("0",))

# BOTÓN CALCULAR
st.markdown("---")
if st.button("🔍 CALCULAR", use_container_width=True):
    if st.session_state.expresion:
        try:
            tabla = generar_tabla(st.session_state.expresion)
            st.success("Resultado generado ✅")
            st.dataframe(tabla, use_container_width=True)
        except:
            st.error("Expresión inválida ❌")
    else:
        st.warning("Ingresa una expresión ⚠️")