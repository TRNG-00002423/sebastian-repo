from __future__ import annotations
from pathlib import Path
from flask import Flask, jsonify, request
from student import Student
import json

app = Flask("Student Management System ")

def db_read_all():
    with open('db.json', 'r') as f:
        json_file = json.load(f)
    return json_file


def db_read(student_id:int):
    with open('db.json', 'r') as f:
        json_file = json.load(f)
    student = list(filter(lambda x: int(x['id']) == int(student_id), json_file))
    return student

def db_write(student:Student):
    with open('db.json', 'r') as f:
        db_json = json.load(f)

    db_json.append(student.to_dict())

    with open('db.json', 'w') as f:
        json.dump(db_json, f, indent=4)
    

    return student.to_dict()

@app.get("/student/")
def get_all_student(): 
    return jsonify(db_read_all())

@app.get("/student/<student_id>")
def get_student(student_id:int): 
    return jsonify(db_read(student_id))

@app.post("/student/")
def post_student():
    data = request.get_json()
    student = Student(
        data["id"],
        data["name"],
        data["course"]
    )   
    
    return jsonify(db_write(student))


if __name__ == "__main__":
    app.run(debug=True)