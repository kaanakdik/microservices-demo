from flask import Flask, jsonify
import requests
import mysql.connector
import os

app = Flask(__name__)

# Ortam değişkenlerinden DB bilgilerini oku
DB_HOST = os.getenv("DB_HOST", "user-db")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "secret")
DB_NAME = os.getenv("DB_NAME", "user_service_db")

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name, email FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)


@app.route('/products-from-user')
def get_products_from_user():
    try:
        response = requests.get("http://product-service:5001/products")
        response.raise_for_status()
        products = response.json()
        return jsonify(products)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Flask default 5000 portunda çalışır
    app.run(host="0.0.0.0", port=5000)
