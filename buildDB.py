from src.db import build

db.build()

db.execute('insert into Pagamento values (\'Cartao\'),(\'Dinheiro\'),(\'Cheque\'),(\'Pix\')')