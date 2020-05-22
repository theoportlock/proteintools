import sqlite3
import pandas as pd

df = pd.read_csv("Proteins.csv")
df.to_sql("Proteins.db")
conn = sqlite3.connect('sbdata.db')
df.to_sql(con=conn, name="proteins", if_exists='append', index=True)
c = conn.cursor()
c.execute("SELECT * from proteins;").fetchall()
