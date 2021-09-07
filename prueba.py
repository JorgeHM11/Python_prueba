# Cargamos librerías
import pandas as pd

# Importamos datos
datos_1 = pd.read_excel("E:\\Scripts Python\\BD_TESIS (VF).xlsx", sheet_name="2018")
datos_2 = pd.read_excel("E:\\Scripts Python\\BD_TESIS (VF).xlsx", sheet_name="2019")
datos_3 = pd.read_excel("E:\\Scripts Python\\BD_TESIS (VF).xlsx", sheet_name="2020")

# Visualizamos los datos
datos_1.head()
datos_1.shape

# Seleccionamos una variable
datos_1["UNIV"]

# Seleccionamos dos o más variables
datos_1[["ACCESO","TIPO_INV"]]

# Seleccionamos datos con "loc" (selección por etiqueta)
(datos_1.loc[1:11,["ACCESO","TIPO_INV"]])

# Seleccionamos datos con "iloc" (selección por posición)
(datos_1.iloc[1:10,0:7])

# Filtrar datos 
datos_1[datos_1["UNIV"] == "UNMSM"]         # Tesis de San Marcos
datos_1[datos_1["ACCESO"] == "RESTRINGIDO"] # Tesis restringidas
datos_1[datos_1["#AUT"] > 1]                # Tesis con más de un autor
datos_1[datos_1["#AUT"].isin([1,2])]        # Tesis con uno y dos autoress

# Exportamos los datos en formato csv
datos_1.to_csv("E:\\Scripts Python\\BD_TESIS.csv")


