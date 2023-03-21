from db_utils import db_connect, create_customer, create_order, create_lineitem
con = db_connect()
try:
    update_sql = "UPDATE products SET price = ? WHERE id = ?"
    cur.execute(update_sql, (10.99, 2))
    con.commit()
except:
    con.rollback()
    raise RuntimeError("Uh oh, an error occurred ...")
