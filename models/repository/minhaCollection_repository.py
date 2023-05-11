from typing import Dict, List, Type

class MinhaCollectionRepository:

    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
        self.__collection_name = "minhaCollection"

    def insert_document(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document
    
    def insert_list_of_documents(self, documents: List[Dict]) -> List:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(documents)
        return documents