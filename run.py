from models.connection_options import DBConnectionHandler
from models.repository import MinhaCollectionRepository

db_handle = DBConnectionHandler()
db_handle.connect_to_db()
conn = db_handle.get_db_connection()
collection = MinhaCollectionRepository(conn)

filtro = {"profissao": "desenvolvedor"}

prop = {"CEP": "55028071"}
response5 = collection.edit_many_increment("idade", 10)
print(response5)
