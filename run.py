from models.connection_options import DBConnectionHandler 
from models.repository import MinhaCollectionRepository

db_handle = DBConnectionHandler()
db_handle.connect_to_db()
conn = db_handle.get_db_connection()
collection = MinhaCollectionRepository(conn)


order = {
    "name": "victor",
    "endereco": "santa rosa",
    "pedidos": {
        "pizza": "10",
        "docinho": "2",
        "pao": "4"
    }
}

order2 = {
    "name": "lucas",
    "endereco": "rua maria 2",
    "pedidos": {
        "hamburger": "1",
        "refrigerante": "2",
        "pizza doce": "1"
    }
}
list_of_d = [order, order2]
collection.insert_list_of_documents(list_of_d)