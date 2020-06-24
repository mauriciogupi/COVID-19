# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # Gráficas COVID-19 Municipios PDET

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# ## INS - Instituro Nacional de Salud

# %%
# CARGAMOS EL DATASET DE COVID-19 COLOMBIA Y LA LISTA CON MUNICIPIOS PDET
url = 'https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD'
pdet = pd.read_csv('data/MunicipiosPDET.csv')
censo = pd.read_csv('data/censo_municipal2018.csv')
datos = pd.read_csv(url)


# %%
datos.head()


# %%
casos = datos.groupby(['Fecha diagnostico','Ciudad de ubicación'])['Ciudad de ubicación'].count().unstack().fillna(0)
casos_acumulados = casos.cumsum()
casos.head()


# %%


casos['Santa Marta'].rolling(7, win_type='gaussian').mean(std=3).plot()


# %%



