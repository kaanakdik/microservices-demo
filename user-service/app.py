from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Basit kullanıcı listesi (gerçekte DB'den gelir)
users = [
    {"id": 1, "name": "Kaan", "email": "kaan@example.com"},
    {"id": 2, "name": "Ahmet", "email": "ahmet@example.com"},
    {"id": 3, "name": "Ayşe", "email": "ayse@example.com"}
]

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


@app.route('/products-from-user')
def get_products_from_user():
    try:
        response = requests.get("http://192.168.1.5:5001/products")
        response.raise_for_status()
        products = response.json()
        return jsonify(products)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Flask default 5000 portunda çalışır
    app.run(host="0.0.0.0", port=5000)
