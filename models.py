from config import db

investments = db["investments"]

def create_investment(data):
    return investments.insert_one(data)

def get_all_investments():
    return list(investments.find({}, {"_id": 0}))

def delete_investment(investment_id):
    return investments.delete_one({"investment_id": investment_id})