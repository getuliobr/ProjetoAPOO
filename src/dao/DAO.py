from src.db import db

class DAO:
  def __init__(self, name, primaryKeyName):
    self.__name = name
    self.__pkName = primaryKeyName

  def select(self, selection = ('*'), where = False):
    whereStatement = f'WHERE {where};' if where else ';'
    query = f'SELECT {selection} from {self.__name} {whereStatement}'
    return db.records(query)

  def getByID(self, ID):
    return self.select('*', f'{self.__pkName} = {ID}')

  def deleteByID(self, ID = False):
    if not ID:
      return

    db.execute(f'DELETE FROM {self.__name} WHERE {self.__pkName} = ?', ID)
    db.commit()

  def getAll(self):
    return self.select()