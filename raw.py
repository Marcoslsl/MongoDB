from pymongo import MongoClient

connection_string = "mongodb://marcos:marcos@localhost:27017/?authSource=admin"
client = MongoClient(connection_string)
db_connection = client["meuBanco"]


collection = db_connection.get_collection("minhaCollection")

search_filter = {
    "estou": "aqui"
}

response = collection.find(search_filter)

for i in response:
    print(i)

collection.insert_one({
    "estou": "aqui", 
    "numeros": [1,2,3]
})