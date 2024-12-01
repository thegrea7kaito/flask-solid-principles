from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask app
app = Flask(__name__)

# Set up the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable unnecessary warnings
db = SQLAlchemy(app)

# Define the User model
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

# Ensure the database is created
with app.app_context():
    db.create_all()

# Define the route for adding a user
@app.route('/add_user', methods=['POST'])
def add_user():
    # Get the JSON data from the request body
    data = request.get_json()

    # Create a new user with the data
    new_user = UserModel(name=data['name'])

    # Add the user to the database and commit the changes
    db.session.add(new_user)
    db.session.commit()

    # Return a success message
    return jsonify({'message': 'User added successfully!'})

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
