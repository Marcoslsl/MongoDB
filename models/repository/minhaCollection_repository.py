from typing import Dict, List, Type
from bson.objectid import ObjectId


class MinhaCollectionRepository:
    """Minha collection repo."""

    def __init__(self, db_connection) -> None:
        """Construct."""
        self.__db_connection = db_connection
        self.__collection_name = "minhaCollection"

    def insert_document(self, document: Dict) -> Dict:
        """Insert de unico documento."""
        collection = self.__db_connection.get_collection(
            self.__collection_name
        )
        collection.insert_one(document)
        return document

    def insert_list_of_documents(self, documents: List[Dict]) -> List:
        """Insert mais de um documento."""
        collection = self.__db_connection.get_collection(
            self.__collection_name
        )
        collection.insert_many(documents)
        return documents

    def select_many(
        self, filtros: Dict = None, opcoes_de_retorno: Dict = None
    ) -> List[Dict]:
        """Select many documents.

        Parameters
        ----------
        filtros: Dict, default = None
            Pega os documentos que possuem as chaves e valores especificados.
        opcoes_de_retorno: Dict
            Se 0 retorna todos os campos menos esse marcado como 0. Se 1,
            devolve somente esse(s) marcado(s) com 1.
            Ex: Retorna todos os campos menos o campo "name".
                opcoes_de_retorno = {
                    "name": 0
                }
        """
        collection = self.__db_connection.get_collection(
            self.__collection_name
        )
        data = collection.find(filtros, opcoes_de_retorno)

        response = []
        for elementos in data:
            response.append(elementos)

        return response

    def select_one(self, filter: Dict = None) -> Dict:
        """Select unico registro com determinado filtro."""
        collection = self.__db_connection.get_collection(
            self.__collection_name
        )
        response = collection.find_one(filter, {"_id": 0})
        return response

    def select_if_property_exists(self, campo: str) -> List[Dict]:
        """Select por um campo que exista nos documentos.

        Parameters
        ----------
        campo: str
            campo para ser filtrado.
        """
        collection = self.__db_connection.get_collection(
            self.__collection_name
        )
        data = collection.find({campo: {"$exists": True}})
        response = []
        for elem in data:
            response.append(elem)
        return response

    def select_many_order(
        self,
        sort_filtro: str,
        filtros: Dict = None,
        opcoes_de_retorno: Dict = None,
        ascending: int = True,
    ):
        """Select ordenado.

        Parameters
        ----------
        ascending: int, default=True
            Se "True", retorna os valores de forma crescente.
        sort_filtro: str
            campo que deseja fazer a ordenacao.
        filtros: Dict, default = None
            Pega os documentos que possuem as chaves e valores especificados.
        opcoes_de_retorno: Dict
            Se 0 retorna todos os campos menos esse marcado como 0. Se 1,
            devolve somente esse(s) marcado(s) com 1.
            Ex: Retorna todos os campos menos o campo "name".
                opcoes_de_retorno = {
                    "name": 0
                }
        """
        collection = self.__db_connection.get_collection(
            self.__collection_name
        )
        if ascending:
            asc = -1
        else:
            asc = 1

        data = collection.find(filtros, opcoes_de_retorno).sort(
            [(sort_filtro, asc)]
        )

        for elem in data:
            print(elem)

    def select_or(self, filtros: List[Dict]) -> List[Dict]:
        """Select por um OU outro(s) filtros.

        Parameters
        ----------
        filtros: List[Dict]
            exemplo
            [{"name": "admin"}, {"cpf": {"$exists":True}}]
        """
        collection = self.__db_connection.get_collection(
            self.__collection_name
        )
        data = collection.find({"$or": filtros})
        response = []
        for elem in data:
            response.append(elem)
        return response

    def select_by_object_id(self, id: str) -> List[Dict]:
        """Select pelo id.

        Parameters
        ----------
        id: str
            Object id.
        """
        collection = self.__db_connection.get_collection(
            self.__collection_name
        )
        data = collection.find({"_id": ObjectId(id)})
        response = []
        for elem in data:
            response.append(elem)
        return response
