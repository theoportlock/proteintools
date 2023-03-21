import sqlite3 as sl
import pandas as pd

df = pd.read_csv("Proteins.csv")
conn = sl.connect('sbdata.db')
df.to_sql("proteins", con=conn, if_exists='append', index=True)
#c = conn.cursor()
#c.execute("SELECT * from proteins;").fetchall()
