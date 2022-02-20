from .cursor import DB

def create(db, tab, val):
  with DB(db) as cr:
    sql = f'CREATE TABLE IF NOT EXISTS {tab}({val})'
    cr.execute(sql)

def insert(db, tab, col, val):
  with DB(db) as cr:
    a = ''
    for n in range(len(col)):
      if n <= len(col) - 2:
        a += col[n] + ','
      else:
        a += col[n]
    col_str = f'({a})'
    b = ''
    for n in range(len(col)):
      if n <= len(col) - 2:
        b += '?' + ','
      else:
        b += '?'
    int_str = f'({b})'
    sql = f'INSERT INTO {tab}{col_str} VALUES {int_str}'
    cr.execute(sql, val)
    
def read(db, tab):
  with DB(db) as cr:
    sql = f'SELECT rowid, * FROM {tab}'
    cr.execute(sql)
    data = cr.fetchall()
  return data
  
def delete(db, tab, id):
  with DB(db) as cr:
    sql = f'DELETE FROM {tab} WHERE rowid = ?'
    cr.execute(sql, (id,))
  
def update(db, tab, col, var):
  with DB(db) as cr:
    col_str = ''
    for n in range(len(col)):
      if n <= len(col) - 2:
        col_str += col[n] + ' = ?, '
      else:
        col_str += col[n] + ' = ?'
    sql = f'UPDATE {tab} SET {col_str} WHERE rowid = ?'
    cr.execute(sql, var)
  
def one(db, tab, id):
  with DB(db) as cr:
    sql = f'SELECT rowid, * FROM {tab} WHERE rowid = ?'
    cr.execute(sql, (id,))
    data = cr.fetchall()
  return data
    
    
    