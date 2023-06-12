import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

transferencias_df = pd.read_csv("transferencias-05_2023.csv", decimal=",")
print(transferencias_df)

# Remove "ANO / MÊS" column by label
transferencias_df = transferencias_df.drop(["ANO / MÊS"], axis=1)
print(transferencias_df)

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

# Visualising data
fig = plt.figure()
ax = fig.subplots()
ax.plot(valores_transferidos)
fig.savefig("graf")
