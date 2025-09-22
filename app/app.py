from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("users.db")
    return conn

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/user")
def get_user():
    username = request.args.get("username", "")
    conn = get_db()
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    return jsonify(result)
