
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

df = pd.read_csv('ambient_temperature_system_failure.csv')
#df.info()
df['timestamp'] = pd.to_datetime(df['timestamp'])
#df.plot(x = 'timestamp', y = 'value')

