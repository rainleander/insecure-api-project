from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///api_database.db'
db: SQLAlchemy = SQLAlchemy(app)


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)


# Routes
@app.route('/', methods=['GET'])
def home():
    return "Hello, World!"


@app.route('/authenticate', methods=['POST'])
def authenticate():
    # [TODO] Implement Authentication Logic
    return jsonify({'message': 'Authentication Endpoint'})


@app.route('/users/<username>', methods=['GET', 'POST'])
def user_data(username):
    if request.method == 'POST':
        # [Intentional Vulnerability] SQL Injection
        query = "SELECT * FROM user WHERE username = '{}'".format(username)
        result = db.engine.execute(query)
        return jsonify({'user': [dict(row) for row in result]})
    else:
        # [TODO] Implement Data Retrieval Logic
        return jsonify({'message': 'User Data Retrieval Endpoint'})


@app.route('/admin', methods=['GET'])
def admin_functions():
    # [TODO] Implement Administrative Functions
    return jsonify({'message': 'Admin Endpoint'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)

