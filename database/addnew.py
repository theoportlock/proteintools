from db_utils import db_connect, create_customer, create_order, create_lineitem
con = db_connect()
try:
    codd_id = create_customer(con, 'Edgar', 'Codd')
    codd_order = create_order(con, codd_id, '1969-01-12')
    codd_li = create_lineitem(con, codd_order, 4, 1, 16.99)
    con.commit()
except:
    con.rollback()
    raise RuntimeError("Uh oh, an error occurred ...")
