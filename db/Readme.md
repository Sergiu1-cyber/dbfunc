
from db import create, insert, read, delete, update, one

db = 'databaza.db'
tab = 'tab1'
col = ['a', 'b']
col_tip = 'a TXT, b TXT'

def create_table(db, col_tip):
  val = col_tip
  create(db, tab, val)
    
def insert_data(db, tab, col):
  a = input('Valoarea "a": ')
  b = input('Valoarea "b": ')
  val = (a, b)
  insert(db, tab, col, val)
  
def citesc_data(db, tab):
  read(db, tab)
    
def sterg_data(db, tab):
  id = int(input('Id: '))
  delete(db, tab, id)
    
def reinnoesc_data(db):
  id = int(input('Id: '))
  a = input('Valoarea "a": ')
  b = input('Valoarea "b": ')
  val = (a, b, id)
  update(db, tab, col, val)
  
def un_element(db, tab):
  id = int(input('Id: '))
  one(db, tab, id)
