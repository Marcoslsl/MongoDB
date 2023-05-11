from models.connection_options import DBConnectionHandler
from models.repository import MinhaCollectionRepository

db_handle = DBConnectionHandler()
db_handle.connect_to_db()
conn = db_handle.get_db_connection()
collection = MinhaCollectionRepository(conn)

filtros = {"name": "marcos"}

op = {"name": 0}

# response = collection.select_many(filtros, op)
# response2 = collection.select_one(filtros)
# response3 = collection.select_if_property_exists()
# response4 = collection.select_many_order()
response5 = collection.select_by_object_id()
print(response5)
