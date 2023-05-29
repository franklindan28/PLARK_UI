from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
URL = "https://www.trashcash.ph/api/v1/auth/sign_in"  


# This is just a dummy database for demonstration purposes.
# In a real-world scenario, you would store hashed passwords and user details in a database.
users = [
    {
        "email": "user1",
        "password": generate_password_hash("password1")
    },
    {
        "email": "user2",
        "password": generate_password_hash("password2")
    }
]

@app.route("/login", methods=["GET"])
def login():
    request_data = request.get_json(URL)
    email = request_data.get("email")
    password = request_data.get("password")

    for user in users:
        if user["username"] == email and check_password_hash(user["password"], password):
            return jsonify({"message": "Login successful"})

    return jsonify({"message": "Invalid username or password"}), 401

if __name__ == "__main__":
    app.run()