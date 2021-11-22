# %%
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

aux=pd.read_parquet('./study_001/da.parquet')
aux.index.name=None
aux['q1']=aux['q1'].apply(lambda x: np.round(x,decimals=4))
aux['q2']=aux['q2'].apply(lambda x: np.round(x,decimals=4))
aux

# %%
ax=sns.heatmap(aux.pivot('q2','q1','normalized amplitude in xy-plane'),cmap='coolwarm_r');
ax.invert_yaxis()

# %%
