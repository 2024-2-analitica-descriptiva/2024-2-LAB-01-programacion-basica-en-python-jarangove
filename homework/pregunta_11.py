"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    conteo_letras = {}
    with open("files/input/data.csv", "r", encoding="utf-8") as file:
        for line in file:
            valor_col_2 = int(line.strip().split("\t")[1])
            letras_col_4 = line.strip().split("\t")[3].split(",")
            for letra in letras_col_4:
                if letra in conteo_letras:
                    conteo_letras[letra] += valor_col_2
                else:
                    conteo_letras[letra] = valor_col_2

    conteo_letras_ordenado = dict(sorted(conteo_letras.items()))
    return conteo_letras_ordenado

resultado = pregunta_11()
print(f"{resultado}")
