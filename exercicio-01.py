import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

transferencias_df = pd.read_csv("transferencias-05_2023.csv", decimal=",")
print(transferencias_df)
print(transferencias_df.columns.values.tolist())

# Remove "ANO / MÊS" column by label
transferencias_df = transferencias_df.drop(["ANO / MÊS"], axis=1)
print(transferencias_df)
print(transferencias_df.columns.values.tolist())

# Change column "VALOR TRANSFERIDO" to float
transferencias_df = transferencias_df.astype({"VALOR TRANSFERIDO": "float32"})
print(transferencias_df)

# We'll work only with the "VALOR TRANSFERIDO" column
valores_transferidos = transferencias_df["VALOR TRANSFERIDO"].to_numpy()
print(valores_transferidos)

max_valores_transferidos = valores_transferidos.max()
print(max_valores_transferidos)

min_valores_transferidos = valores_transferidos.min()
print(min_valores_transferidos)

avg_valores_transferidos = np.average(valores_transferidos)
print(avg_valores_transferidos)

# Find unique types of money receivers
favorecidos = pd.unique(transferencias_df["TIPO FAVORECIDO"])
print(favorecidos)

# Group values by money receivers
favorecidos_valores = (
    transferencias_df[["VALOR TRANSFERIDO", "TIPO FAVORECIDO"]]
    .groupby("TIPO FAVORECIDO")
    .sum()
)
print(favorecidos_valores)
print(favorecidos_valores.columns.values)

# Get row labels as a numpy array
favorecidos = favorecidos_valores.index.values
# Get transfered money as a numpy array
valores = favorecidos_valores["VALOR TRANSFERIDO"].to_numpy()
valores_milhoes = valores / 1e6
max_valores_milhoes = valores_milhoes.max()
print(favorecidos)
print(valores)

# Plot bars
fig = plt.figure(figsize=[12, 6], dpi=300, layout="constrained")
fig.suptitle("Relação entre tipos de favorecidos e valores recebidos")
ax = fig.subplots()
ax.set_xlabel("Valores recebidos em milhões de reais")
ax.set_ylabel("Tipos de favorecidos")
ax.set(xlim=[0, max_valores_milhoes + 0.1 * max_valores_milhoes])
ax.barh(favorecidos, valores_milhoes)
fig.savefig("graf2")
