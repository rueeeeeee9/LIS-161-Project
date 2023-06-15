import sqlite3

db_path = "Database.db"

def connect_to_db(path):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

def read_smartphones_by_brand(brand):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM smartphones WHERE brand = ?'
    value = brand
    results = cur.execute(query,(value,)).fetchall()
    conn.close()
    return results

def read_smartphone_by_id(id):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM smartphones WHERE id = ?'
    value = id
    results = cur.execute(query,(value,)).fetchone()
    conn.close()
    return results

def insert_smartphone(smartphone_data):
    conn, cur = connect_to_db(db_path)
    query = 'INSERT INTO smartphones (brand, model, chipset, main_camera, selfie_camera, internal_memory, battery, color, price, condition, reason_for_selling, url) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'
    values = (smartphone_data['brand'], smartphone_data['model'],
              smartphone_data['chipset'], smartphone_data['main_camera'],
              smartphone_data['selfie_camera'], smartphone_data['internal_memory'],
              smartphone_data['battery'], smartphone_data['color'],
              smartphone_data['price'], smartphone_data['condition'],
              smartphone_data['reason_for_selling'], smartphone_data['url'])
    cur.execute(query,values)
    conn.commit()
    conn.close()

def update_smartphone(smartphone_data):
    conn, cur = connect_to_db(db_path)
    query = "UPDATE smartphones SET brand=?, model=?, chipset=?, main_camera=?, selfie_camera=?, internal_memory=?, battery=?, color=?, price=?, condition=?, reason_for_selling=?, url=? WHERE id=?"
    values = (smartphone_data['brand'], smartphone_data['model'],
              smartphone_data['chipset'], smartphone_data['main_camera'],
              smartphone_data['selfie_camera'], smartphone_data['internal_memory'],
              smartphone_data['battery'], smartphone_data['color'],
              smartphone_data['price'], smartphone_data['condition'],
              smartphone_data['reason_for_selling'], smartphone_data['url'],
              smartphone_data['id'])
    cur.execute(query,values)
    conn.commit()
    conn.close()

def delete_smartphone(smartphone_id):
    conn, cur = connect_to_db(db_path)
    query = "DELETE FROM smartphones WHERE id = ?"
    values = (smartphone_id)
    cur.execute(query, values)
    conn.commit()
    conn.close()

def search_smartphones(query):
    conn, cur = connect_to_db(db_path)
    sql_query = "SELECT * FROM smartphones WHERE brand LIKE ? OR model LIKE ?"
    value = "%{}%".format(query)
    results = cur.execute(sql_query, (value, value)).fetchall()
    conn.close()
    return results