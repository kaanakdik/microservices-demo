from flask import Flask, jsonify

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

if __name__ == "__main__":
    # Flask default 5000 portunda çalışır
    app.run(host="0.0.0.0", port=5000)
