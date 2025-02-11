from pymongo import MongoClient

MONGO_URI = "mongodb+srv://Adriansen:W5KEFs6WotPhkxNC@cluster0.iz0qh.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client["investment_db"]
