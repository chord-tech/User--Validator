from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os
import re

app = Flask(__name__, static_folder=".", static_url_path="")
CORS(app)

DB_PATH = "users.db"


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def validate_username(username: str) -> tuple[bool, str]:
    if len(username) < 8:
        return False, "Username must be at least 8 characters long"
    if " " in username:
        return False, "Username must not contain spaces"
    if any(char.isdigit() for char in username):
        return False, "Username must not contain digits"
    return True, "Username is valid"


def validate_password(password: str) -> tuple[bool, str]:
    if len(password) < 7:
        return False, "Password must be at least 7 characters long"
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one digit"
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter"
    return True, "Password is valid"


@app.route("/")
def index():
    return send_from_directory(".", "index.html")


@app.route("/api/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    username = (data.get("username") or "").strip()
    password = data.get("password") or ""
    confirm = data.get("confirm") or ""

    # Validate username
    ok, msg = validate_username(username)
    if not ok:
        return jsonify({"success": False, "error": msg}), 400

    # Validate password
    ok, msg = validate_password(password)
    if not ok:
        return jsonify({"success": False, "error": msg}), 400

    # Confirm match
    if password != confirm:
        return jsonify({"success": False, "error": "Passwords do not match"}), 400

    # Check if username already exists
    conn = get_db()
    existing = conn.execute(
        "SELECT id FROM users WHERE username = ?", (username,)
    ).fetchone()

    if existing:
        conn.close()
        return jsonify({"success": False, "error": "Username already taken"}), 409

    # Store user with hashed password
    password_hash = generate_password_hash(password)
    conn.execute(
        "INSERT INTO users (username, password_hash) VALUES (?, ?)",
        (username, password_hash),
    )
    conn.commit()
    conn.close()

    return jsonify({
        "success": True,
        "message": f"User '{username}' registered successfully!"
    }), 201


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    username = (data.get("username") or "").strip()
    password = data.get("password") or ""

    if not username or not password:
        return jsonify({"success": False, "error": "Username and password required"}), 400

    conn = get_db()
    user = conn.execute(
        "SELECT * FROM users WHERE username = ?", (username,)
    ).fetchone()
    conn.close()

    if not user or not check_password_hash(user["password_hash"], password):
        return jsonify({"success": False, "error": "Invalid username or password"}), 401

    return jsonify({
        "success": True,
        "message": f"Welcome back, {username}!"
    })


@app.route("/api/users", methods=["GET"])
def list_users():
    """List registered usernames (for demo purposes only)."""
    conn = get_db()
    rows = conn.execute(
        "SELECT id, username, created_at FROM users ORDER BY created_at DESC"
    ).fetchall()
    conn.close()

    users = [
        {"id": r["id"], "username": r["username"], "created_at": r["created_at"]}
        for r in rows
    ]
    return jsonify({"users": users, "count": len(users)})


if __name__ == "__main__":
    init_db()
    print("Database ready. Starting server at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
