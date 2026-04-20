import pandas as pd
import itertools

def generar_tabla(expresion):
    variables = sorted(set(filter(str.isalpha, expresion)))
    
    combinaciones = list(itertools.product([False, True], repeat=len(variables)))
    
    tabla = []
    
    for valores in combinaciones:
        contexto = dict(zip(variables, valores))
        try:
            resultado = eval(expresion, {}, contexto)
        except:
            resultado = "Error"
        
        fila = list(valores) + [resultado]
        tabla.append(fila)
    
    columnas = variables + ["Resultado"]
    return pd.DataFrame(tabla, columns=columnas)