# Script histogramas número de turnos en una muestra de partidas de ajedrez.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_name = "games.csv"
df = pd.read_csv(file_name, parse_dates=True, sep=',',decimal='.')

dfturns = pd.DataFrame(df["turns"])
df.turns.hist(bins = 20)
plt.show()
