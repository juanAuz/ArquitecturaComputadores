import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Ajusta la ruta a tu CSV real
df = pd.read_csv("clima-barcelona-hoy.csv")

cols = ['main_temp', 'main_feels_like', 'main_humidity', 'main_pressure',
        'wind_speed', 'wind_gust', 'clouds_all', 'visibility']

corr = df[cols].corr()

fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)

ax.set_xticks(np.arange(len(cols)))
ax.set_yticks(np.arange(len(cols)))
ax.set_xticklabels(cols, rotation=45, ha="right")
ax.set_yticklabels(cols)

for i in range(len(cols)):
    for j in range(len(cols)):
        ax.text(j, i, f"{corr.iloc[i, j]:.2f}",
                 ha="center", va="center", color="black", fontsize=8)

ax.set_title("Matriz de correlación - variables climáticas Barcelona")
fig.colorbar(im, ax=ax, label="Coeficiente de correlación")
plt.tight_layout()
plt.savefig("heatmap_correlacion.png")
print("Listo, revisa heatmap_correlacion.png")
