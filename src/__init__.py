import os

from flask import  Flask, jsonify, request
from flask_restx import Resource, Api, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app_settings = os.getenv("APP_SETTINGS")
app.config.from_object(app_settings)

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

user = api.model("User", {
    "id": fields.Integer(readOnly=True),
    "username": fields.String(required=True),
    "email": fields.String(required=True),
    "created_date": fields.DateTime(),
})

class Ping(Resource):
    def get(self):
        return {
            "status": "success",
            "message": "pong"
        }

api.add_resource(Ping, "/ping")

class Users(Resource):
    @api.expect(user, validate=True)
    def post(self):
        data = request.get_json()
        username = data.get("username")
        email = data.get("email")

        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            error = {
                "message": f"User {email} is already registered."
            }

            return error, 409

        db.session.add(User(username, email))
        db.session.commit()

        created_user = {
            "message": f"User {email} added."
        }

        return created_user, 201

api.add_resource(Users, "/users")