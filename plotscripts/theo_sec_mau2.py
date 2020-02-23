#!/usr/bin/env python3
import pandas as pd
import plotnine as p9
import numpy as np

df = pd.read_csv("test.csv",header=[1,2])
a = df.columns.get_level_values(0)
b = df.columns.get_level_values(1)
df.columns = [a.to_series().mask(lambda x: x.str.startswith('Unnamed')).ffill(), b]

print(df.head())
'''
plot = (p9.ggplot(data=df, mapping=p9.aes(x="(UV,ml)",y="(UV,mAU)"))
    + p9.geom_line()
    + p9.theme_classic()
)

plot.save("test.png", dpi=600)
'''
