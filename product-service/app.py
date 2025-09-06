from flask import Flask, jsonify

app = Flask(__name__)

# Basit ürün listesi
products = [
    {"id": 1, "name": "Laptop", "price": 1500},
    {"id": 2, "name": "Telefon", "price": 800},
    {"id": 3, "name": "Kulaklık", "price": 200}
]

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)  # dikkat: 5001 portu
