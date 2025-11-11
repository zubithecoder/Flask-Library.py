from flask import Flask, jsonify, request
from models import db, Student

app = Flask(__name__)

# 💡 Switched to SQLite — no setup needed!
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flask_app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return {"message": "Flask + SQLAlchemy + SQLite working perfectly!"}

@app.route("/student", methods=["POST"])
def add_student():
    data = request.json
    new_student = Student(name=data["name"], age=data["age"])
    db.session.add(new_student)
    db.session.commit()
    return {"message": "Student added successfully"}

@app.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()
    data = [{"id": s.id, "name": s.name, "age": s.age} for s in students]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
