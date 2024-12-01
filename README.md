Understanding and Applying SOLID Principles in Python Flask

Introduction

In software development, writing clean, maintainable, and scalable code is essential. The SOLID principles, introduced by Robert C. Martin, provide a foundation for achieving these goals. In this article, we'll explore the SOLID principles and demonstrate how to apply them in Python Flask with practical examples and real-world use cases.

1. Single Responsibility Principle (SRP)

Definition: A class should have only one reason to change, meaning it should only have one job.

Python Flask Example:
In a Flask application, separating the database interaction logic from request handling logic ensures that each component has a single responsibility.

# db_service.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

def add_user(name):
    user = UserModel(name=name)
    db.session.add(user)
    db.session.commit()


# app.py
from flask import Flask, request
from db_service import db, add_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)

@app.route('/add_user', methods=['POST'])
def handle_add_user():
    name = request.json['name']
    add_user(name)
    return {"message": "User added successfully!"}


Real-World Use Case:
Imagine a microservice where one component manages user records while another handles analytics. This separation makes the system modular and easier to maintain.

2. Open/Closed Principle (OCP)

Definition: Software entities should be open for extension but closed for modification.

Python Flask Example:
Using blueprints in Flask to add new features without modifying existing code.

# views.py
from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    return {"message": "Login endpoint"}

@auth_blueprint.route('/logout', methods=['POST'])
def logout():
    return {"message": "Logout endpoint"}


Real-World Use Case:
You can add a new payment gateway to your e-commerce application by creating a separate blueprint instead of altering the original payment processing code.

3. Liskov Substitution Principle (LSP)

Definition: Objects of a superclass should be replaceable with objects of a subclass without altering the correctness of the program.

Python Flask Example:
Defining base and derived classes for user roles.

class BaseUser:
    def get_permissions(self):
        raise NotImplementedError

class AdminUser(BaseUser):
    def get_permissions(self):
        return ["read", "write", "delete"]

class RegularUser(BaseUser):
    def get_permissions(self):
        return ["read"]


Real-World Use Case:
In an API, substituting a base class NotificationService with EmailNotification or SMSNotification should not break the functionality.

4. Interface Segregation Principle (ISP)

Definition: A class should not be forced to implement methods it does not use.

Python Flask Example:
Creating modular service interfaces.

from abc import ABC, abstractmethod

class AuthService(ABC):
    @abstractmethod
    def login(self, username, password):
        pass

class TokenAuthService(AuthService):
    def login(self, username, password):
        return "Token-based authentication successful!"


Real-World Use Case:
Modularizing external integrations like authentication providers (e.g., Google, Facebook, etc.).

5. Dependency Inversion Principle (DIP)

Definition: High-level modules should not depend on low-level modules; both should depend on abstractions.

Python Flask Example:
Dependency injection for database services.

class DatabaseService:
    def save_data(self, data):
        print(f"Saving {data} to the database")

class Application:
    def __init__(self, service: DatabaseService):
        self.service = service

    def run(self):
        self.service.save_data({"key": "value"})

db_service = DatabaseService()
app = Application(db_service)
app.run()


Real-World Use Case:
Switching from a MySQL database to a MongoDB database without changing the application's core logic.

Conclusion

By adhering to the SOLID principles, you can build software that is easier to maintain, extend, and debug. Flask provides the flexibility needed to apply these principles effectively in web development. I hope this guide helps you understand and apply SOLID principles in your projects.

Read the detailed article on https://kaito31.hashnode.space/default-guide/v1.0?t=1733063530444
