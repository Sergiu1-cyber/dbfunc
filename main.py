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
  info = read(db, tab)
  print(info)
    
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
  info = one(db, tab, id)
  print(info)
  
def main():
  ex = input('Execut:\n 1) Insert\n 2) Citesc\n 3) Sterg\n 4) Reînnoiesc\n 5) Un element\n 6) Creez db, tab\n\n')
  if ex == '1':
    insert_data(db, tab, col)
  elif ex == '2':
    citesc_data(db, tab)
  elif ex == '3':
   sterg_data(db, tab)
  elif ex == '4':
    reinnoesc_data(db)
  elif ex == '5':
    un_element(db, tab)
  elif ex == '6':
    create_table(db, col_tip)
  else:
    citesc_data(db, tab)
  
if __name__ == '__main__':
  main()
  


