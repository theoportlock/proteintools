import sqlite3
from db_utils import db_connect, create_customer, create_order, create_lineitem

con = db_connect()
con.row_factory = sqlite3.Row
cur = con.cursor()
cur.execute("SELECT id, first_name, last_name FROM customers WHERE id = 2")
result = cur.fetchone()
id, first_name, last_name = result['id'], result['first_name'], result['last_name']
print(f"Customer: {first_name} {last_name}'s id is {id}")
