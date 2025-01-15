"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    valores_por_clave = {}
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            columns = line.strip().split("\t")
            if len(columns) < 5:
                continue  
            diccionario_str = columns[4]
            pares = diccionario_str.split(",")
            for par in pares:
                clave_actual, valor = par.split(":")
                valor = int(valor)
                if clave_actual in valores_por_clave:
                    valores_por_clave[clave_actual][0] = min(
                        valores_por_clave[clave_actual][0], valor)
                    valores_por_clave[clave_actual][1] = max(
                        valores_por_clave[clave_actual][1], valor)
                else:
                    valores_por_clave[clave_actual] = [valor, valor]
   
    resultado = [
        (clave, valores[0], valores[1])
        for clave, valores in sorted(valores_por_clave.items())
    ]
    return resultado

print("[")
for clave, min_val, max_val in pregunta_06():
    print(f"('{clave}', {min_val}, {max_val}),")
print("]")
