from __future__ import annotations
from pathlib import Path
from flask import Flask, jsonify, request
import json

app = Flask("Student Management System ")

def db_size():
    with open('db.json', 'r') as f:
        json_file = json.load(f)        
    return len(json_file)

def db_read_all():
    with open('db.json', 'r') as f:
        json_file = json.load(f)
        print(len(json_file))
    return json_file


def db_read(student_id:int):
    with open('db.json', 'r') as f:
        json_file = json.load(f)
    student = list(filter(lambda x: int(x['id']) == int(student_id), json_file))
    return student

def db_write(student):
    with open('db.json', 'r') as f:
        db_json = json.load(f)
    student['id'] = db_size()
    db_json.append(student)

    with open('db.json', 'w') as f:
        json.dump(db_json, f, indent=4)
    

    return student

@app.get("/student/")
def get_all_student(): 
    return jsonify(db_read_all())

@app.get("/student/<student_id>")
def get_student(student_id:int): 
    return jsonify(db_read(student_id))

@app.post("/student/")
def post_student():
    data = request.get_json()
    student = {'id':0,
        'name':data["name"],
        'course':data["course"]
    }    
    return jsonify(db_write(student))


if __name__ == "__main__":
    app.run(debug=True)