from models.connection_options import DBConnectionHandler
from models.repository import MinhaCollectionRepository
from datetime import timedelta, datetime

db_handle = DBConnectionHandler()
db_handle.connect_to_db()
conn = db_handle.get_db_connection()
collection = MinhaCollectionRepository(conn)

collection.create_index_ttl()
document = {
    "nome": "arnaldo",
    "idade": 32,
    "data_de_criacao": datetime.utcnow() - timedelta(hours=3),
}
collection.insert_document(document)
