import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.decomposition import PCA

df = pd.read_csv("CALCULATOR.csv",na_filter=True).dropna()
df["Hydrophobicity"].astype("float64")
df["Aliphatic index"].astype("float64")
df["PI"].astype("float64")
df["MW"].astype("float64")
df["Ext"].astype("float64")
filtereddf = df.loc[:,["Hydrophobicity","Aliphatic index","PI"]]
pca = PCA(n_components=2)
pca.fit(filtereddf)
#print(pca.explained_variance_ratio_)
#print(pca.singular_values_)
transformeddf = pca.transform(filtereddf)
print(transformeddf)
plt.scatter(transformeddf[:,0],transformeddf[:,1])
plt.show()
