# This code demonstrates how to use Flask with blueprints & Flask-RESTful for creating a RESTful API.app
from flask import Flask, Blueprint
from flask_restful import Api, Resource

# Create the main Flask app 
app = Flask(__name__)

# Create a Blueprint for user-related routes
user_blueprint = Blueprint("user",__name__)

# Attach Flask-RESTful API to this Blueprint
api = Api(user_blueprint)

# Define a Resource for the Blueprint
class UserResource(Resource):
    def get(self):
        return {"message":"User GET request"}
    
# Add Resource to the Blueprint API 
api.add_resource(UserResource, "/user")

# Register the Blueprint with the main app
app.register_blueprint(user_blueprint, url_prefix="/api")    # Optional url_prefix

# Optional: Add a root route
@app.route("/")
def home():
    return {"message": "Welcome to the Flask Blueprint API!"}

# Run the app
if __name__ == "__main__":
    app.run(debug=True) 
