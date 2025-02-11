from flask import Blueprint, request, jsonify
from models import create_investment, get_all_investments, delete_investment

api = Blueprint("api", __name__)

@api.route("/investments", methods=["POST"])
def add_investment(): 
    data = request.json 

    # checkear si existen los campos obligatorios
    required_fields = ["investment_id", "amount", "company", "date"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"El campo '{field}' es obligatorio"}), 400

    # 'investment_id' es int
    if not isinstance(data["investment_id"], (int)):
        return jsonify({"error": "El campo 'investment_id' debe ser un string o número"}), 400

    # 'amount' es int o float mayor que 0
    if not isinstance(data["amount"], (int, float)) or data["amount"] <= 0:
        return jsonify({"error": "El campo 'amount' debe ser un número mayor a 0"}), 400

    # 'company' es string no vacio
    if not isinstance(data["company"], str) or data["company"].strip() == "":
        return jsonify({"error": "El campo 'company' debe ser un string no vacío"}), 400

    # si todo OK entonces se almacena en db
    create_investment(data)
    return jsonify({"message": "Inversión registrada correctamente"}), 201

@api.route("/investments", methods=["GET"])
def list_investments():
    investments = get_all_investments()
    return jsonify(investments)

@api.route("/investments/<investment_id>", methods=["DELETE"])
def remove_investment(investment_id):
    delete_investment(investment_id)
    return jsonify({"message": "Inversión eliminada"}), 200
