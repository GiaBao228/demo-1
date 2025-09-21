from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Kết nối SQLite
def get_db():
    conn = sqlite3.connect("users.db")
    return conn

@app.route("/")
def home():
    return "Hello DevSecOps Demo!"

# Lỗi SQL Injection (để test DAST)
@app.route("/user")
def get_user():
    username = request.args.get("username")
    conn = get_db()
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
