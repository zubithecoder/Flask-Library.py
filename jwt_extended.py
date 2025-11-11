from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

# Secret key for signing JWTs
app.config["JWT_SECRET_KEY"] = "mysecretkey"
jwt = JWTManager(app)

# Fake users database
users = {
    "zubi": "1234",
    "ali": "abcd"
}

@app.route("/")
def home():
    return jsonify({"msg": "Welcome! Flask JWT API is running."})

# Login Route -> Generates JWT Token
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

# Check if user exists and password is correct
    if username in users and users[username] == password:
        token = create_access_token(identity=username)
        return jsonify ({"msg": "Login successful", "token": token})
    else:
        return jsonify({"msg": "Invalid credentials"}), 401

# Protected Route -> Needs Token
@app.route("/profile", methods=["GET"])
@jwt_required() # This makes route protected

def profile():
    current_user = get_jwt_identity()
    return jsonify({"msg": f"Welcome {current_user}, This is your profile!"})

if __name__ == "__main__":
    app.run(debug=True)

