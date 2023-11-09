# app.py - A deliberately insecure API for educational purposes.

from flask import Flask, request, jsonify, make_response
import sqlite3
import os

app = Flask(__name__)

# Insecure: Hardcoded secret key
app.config['SECRET_KEY'] = 'supersecret'

# Insecure Database Connection: No password, and using SQLite for simplicity
DATABASE = 'data.db'


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/login', methods=['POST'])
def login():
    # Insecure Authentication: Simple token validation without hashing or proper verification
    username = request.json.get('username')
    password = request.json.get('password')
    
    if username == 'admin' and password == 'password':  # Insecure: Default credentials
        return jsonify({'token': 'secret-token-123'}), 200  # Insecure: Hardcoded token
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    # Insecure: Direct parameter insertion into SQL query leading to SQL Injection
    query = f"SELECT * FROM users WHERE id = {user_id};"
    conn = get_db_connection()
    user = conn.execute(query).fetchone()
    conn.close()
    
    # Insecure: Verbose error messages
    if user is None:
        return jsonify({'message': 'No user found!'}), 404
    
    return jsonify(dict(user)), 200


@app.route('/users', methods=['POST'])
def create_user():
    # Insecure: No input validation or sanitation
    username = request.json.get('username')
    password = request.json.get('password')
    
    # Insecure: Potential Mass Assignment Vulnerability
    conn = get_db_connection()
    conn.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                 (username, password))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'User created'}), 201


# Insecure: Debug mode should never be enabled in production
if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        # Insecure: Executing SQL commands from string can lead to SQL injection
        conn.executescript("""
        DROP TABLE IF EXISTS users;
        CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT);
        INSERT INTO users (username, password) VALUES ('admin', 'password');
        """)
        conn.commit()
        conn.close()
    
    app.run(debug=True)
