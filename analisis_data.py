import numpy as np

import pandas as pd

"""**1**"""

df = pd.read_csv('estudiantes.csv')

print (df.head(10))

print (df.tail(5))

"""**2**"""

df.shape

df.columns

df.dtypes

df.info()

"""**3**"""

df.describe().round(2)

"""**4**"""

conteo = df['Departamento'].value_counts()

print(conteo)

print((df['Departamento'].nunique()))

"""**5**"""

faltantes = df.isna().sum()
porcentaje = df.isna().sum() / len(df) * 100

print(faltantes)
print(porcentaje)

filas_afectadas = df[df.isna().any(axis=1)]
print(filas_afectadas)

"""**6**"""

df_limpio = df.dropna(subset=["Nota"]).copy()

mediana_edad = df_limpio["Edad"].median()

df_limpio["Edad"] = df_limpio["Edad"].fillna(mediana_edad)

print(df_limpio.isna().sum())
print(df_limpio.shape)

"""**7**"""

notas = df_limpio["Nota"].to_numpy()
edades = df_limpio["Edad"].to_numpy()

print("NOTA")
print(np.mean(notas).round(2))
print(np.median(notas).round(2))
print(np.std(notas).round(2))
print(np.var(notas).round(2))

print("EDAD")
print(np.mean(edades).round(2))
print(np.median(edades).round(2))
print(np.std(edades).round(2))
print(np.var(edades).round(2))

"""**8**"""

print("NOTAS")
print("Mínimo:", np.min(notas))
print("Máximo:", np.max(notas))
print("Rango:", np.ptp(notas))
print("Q1:", np.percentile(notas, 25))
print("Q2:", np.percentile(notas, 50))
print("Q3:", np.percentile(notas, 75))

print("EDADES")
print("Mínimo:", np.min(edades))
print("Máximo:", np.max(edades))
print("Rango:", np.ptp(edades))
print("Q1:", np.percentile(edades, 25))
print("Q2:", np.percentile(edades, 50))
print("Q3:", np.percentile(edades, 75))

df_limpio["Nota"].mean().round(2)

np.nanmean(df["Nota"].to_numpy())

"""**9**"""

maximo = np.max(notas)
minimo = np.min(notas)

mejores = df_limpio[
    df_limpio["Nota"] == maximo
][["Nombre", "Edad", "Nota", "Departamento"]]

peores = df_limpio[
    df_limpio["Nota"] == minimo
][["Nombre", "Edad", "Nota", "Departamento"]]

print(mejores)
print(peores)

"""**10**"""

aprobados = df_limpio[df_limpio["Nota"] >= 11]
desaprobados = df_limpio[df_limpio["Nota"] < 11]

tasa = round(len(aprobados) / len(df_limpio) * 100,2)

print("Aprobados:", len(aprobados))
print("Desaprobados:", len(desaprobados))
print("Tasa:", tasa)

"""**11**"""

df_limpio["Aprobado"] = np.where(
    df_limpio["Nota"] >= 11,
    "Sí",
    "No"
)

print(df_limpio["Aprobado"].value_counts())

"""**12**"""

seleccion = df_limpio[
    (df_limpio["Edad"] < 20) &
    (df_limpio["Nota"] >= 15)
]

print(seleccion)

"""**13**"""

top10 = df_limpio.sort_values ("Nota", ascending=False).head(10)

print(top10)

"""**14**"""

promedios = (df_limpio.groupby("Departamento")["Nota"].mean().round(2).sort_values(ascending=False))

print(promedios)

"""**15**"""

tabla = pd.crosstab(
    df_limpio["Departamento"],
    df_limpio["Aprobado"]
)

tabla["Total"] = tabla["Sí"] + tabla["No"]

tabla["Tasa"] = (tabla["Sí"] / tabla["Total"] * 100).round(2)

tabla = tabla.sort_values(
    "Tasa",
    ascending=False
)

print(tabla)

"""**16**"""

df_limpio["GrupoEtario"] = pd.cut(
    df_limpio["Edad"],
    bins=[15, 19, 22, 25, np.inf],
    labels=["16-19", "20-22", "23-25", "26+"]
)

resumen_edad = df_limpio.groupby(
    "GrupoEtario",
    observed=False
)["Nota"].agg(
    Cantidad="count",
    Promedio="mean",
    Mediana="median"
)

print(resumen_edad)

"""**17**"""

condiciones = [
    df_limpio["Nota"] >= 18,
    df_limpio["Nota"] >= 14,
    df_limpio["Nota"] >= 11,
    df_limpio["Nota"] >= 0
]

categorias = ["AD", "A", "B", "C"]

df_limpio["Escala"] = np.select(
    condiciones,
    categorias,
    default="C"
)

conteo = df_limpio["Escala"].value_counts()
porcentaje = conteo / len(df_limpio) * 100

print(conteo)
print(porcentaje)

"""**18**"""

tabla_cruzada = pd.crosstab(
    df_limpio["GrupoEtario"],
    df_limpio["Aprobado"],
    margins=True
)

print(tabla_cruzada)

porcentajes = pd.crosstab(
    df_limpio["GrupoEtario"],
    df_limpio["Aprobado"],
    normalize="index"
) * 100

print(porcentajes)

"""**19**"""

minimo = df_limpio["Nota"].min()
maximo = df_limpio["Nota"].max()

df_limpio["Nota_minmax"] = (
    (df_limpio["Nota"] - minimo)
    /
    (maximo - minimo)
)
print(df_limpio["Nota_minmax"].round(2))

media = np.mean(df_limpio["Nota"])
desviacion = np.std(df_limpio["Nota"])

df_limpio["Nota_z"] = (
    (df_limpio["Nota"] - media)
    /
    desviacion
)
print(df_limpio["Nota_z"].round(2))

atipicos = df_limpio[
    np.abs(df_limpio["Nota_z"]) > 2
]

print(atipicos[
    ["Nombre", "Nota", "Departamento", "Nota_z"]
].round(2))

"""**20**"""

reporte = (
    df_limpio.groupby("Departamento")
    .agg(
        Estudiantes=("Nota", "size"),
        Nota_promedio=("Nota", "mean"),
        Mediana=("Nota", "median"),
        Desviacion_estandar=("Nota", "std"),
        Minimo=("Nota", "min"),
        Maximo=("Nota", "max"),
        Aprobados=("Aprobado", lambda x: (x == "Sí").sum()),
        Desaprobados=("Aprobado", lambda x: (x == "No").sum())
    )
)

reporte["Tasa_aprobacion"] = (
    reporte["Aprobados"]
    / reporte["Estudiantes"]
    * 100
)

reporte = reporte[
    reporte["Estudiantes"] >= 5
]

reporte = reporte.sort_values(
    "Tasa_aprobacion",
    ascending=False
)

reporte = reporte.round(2)

reporte = reporte.reset_index()

print(reporte)

reporte.to_csv(
    "reporte.csv",
    index=False,
    encoding="utf-8"
)

verificacion = pd.read_csv("reporte.csv")

print(verificacion.head())