import pandas as pd
import re

df = pd.read_csv("sortedpeaks.csv")

#df["ajustf1"]=re.findall(r'^-?\d+',df["Assign F1"])
for i in df["Assign F1"]:
    print(int(re.findall(r'\d+',i)[0]))
