import sqlite3

class DB:
  
  def __init__(self, db):
    self.db = db

  def __enter__(self):
    self.cn = sqlite3.connect(self.db)
    self.cr = self.cn.cursor()
    return self.cr

  def __exit__(self, exec_type, exec_value, exec_trace):
    self.cn.commit()
    self.cr.close()
    self.cn.close()

