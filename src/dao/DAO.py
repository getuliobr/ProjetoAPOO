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
    return db.records(f'SELECT * from {self.__name} WHERE {self.__pkName} = ?', ID)[0]

  def deleteByID(self, ID = None):
    if not ID:
      return

    db.execute(f'DELETE FROM {self.__name} WHERE {self.__pkName} = \'{ID}\'')
    db.commit()

  def getAll(self):
    return self.select()