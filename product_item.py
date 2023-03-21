import sqlite3
import os

# File and path for database
db_folder = os.path.join(os.path.dirname(__file__), "product.db")

def get_products():
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT name, category, price, instock
        FROM product 
        ORDER BY name
    """
    cursor = conn.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        record = {
            'name': row[0],
            'category': row[1],
            'price': row[2],
            'instock': row[3]
            }
        data.append(record)
    
    conn.close()
    return data

def find_product(name):
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT name, category, price, instock
        FROM product 
        WHERE name=?
    """
    val = (name,)
    cursor = conn.execute(sql,val)
    row = cursor.fetchone()

    if row:
        record = {
            'name': row[0],
            'category': row[1],
            'price': row[2],
            'instock': row[3]
            }
        data.append(record)
    else:
        record = {}
    
    conn.close()
    return record

def add_product(name, category, price, instock):
    conn = sqlite3.connect(db_folder)
    sql = """
        INSERT INTO product(name, category, price, instock)
        VALUES(?,?,?,?)
    """
    val = (name, category, price, instock)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Product added successfully"
    
def delete_product(name):
    conn = sqlite3.connect(db_folder)
    sql = """
        DELETE FROM product
        WHERE name=?
    """
    val = (name,)
    conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Product deleted successfully"

def update_product(name, category, price, instock):
    conn = sqlite3.connect(db_folder)
    sql = """
        UPDATE product
        SET category=?, price=?, instock=?
        WHERE name=?
    """
    val = (category, price, instock, name)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Product updated successfully"
