
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

df = pd.read_csv('ambient_temperature_system_failure.csv')
#df.info()

df['timestamp'] = pd.to_datetime(df['timestamp'])
#df.plot(x = 'timestamp', y = 'value')

df['time'] = (df['timestamp'].astype(np.int64))
data = df[['value', 'time']]
min_max_scaler = preprocessing.StandardScaler()
scaled_data = min_max_scaler.fit_transform(data)
data = pd.DataFrame(scaled_data)

pca = PCA()
data = pca.fit(data)

n = pca.n_components_
var_ratio = pca.explained_variance_ratio_
pve = pca.explained_variance_
sing_val = pca.singular_values_
components = pca.components_

grid = np.arange(0, n)
plt.bar(grid, var_ratio)
plt.ylabel('PVE')        #percent variance explained
plt.xlabel('PCs')
plt.ylim([0, 1])
plt.xticks([0,1])

fig, ax = plt.subplots(figsize = [6, 4])
ax.plot(sing_val)
ax.set_title("Singular Values")      #relative strength of each PC 
ax.set_xticks([0, 1])
ax.set_xlabel("PCs")
#ax.grid(True)

cum_pve = np.cumsum(var_ratio)
fig, ax = plt.subplots(figsize = [6, 4])

ax.plot(cum_pve, 'o-')
#ax.set_title("")
#ax.set_xlim([0, 2])
ax.set_xticks([0, 1])
#ax.set_ylim([0.5, 1.1])
plt.xlabel('PCs')
plt.ylabel('Cumulative PVE')

print(pd.DataFrame(components, index = [f'PC{i}' for i in range(0, n)]))


