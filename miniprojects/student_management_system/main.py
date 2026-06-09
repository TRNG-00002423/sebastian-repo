from __future__ import annotations
from pathlib import Path
from flask import Flask, jsonify, request
import controller
import json

app = Flask("Student Management System ")

@app.get("/student/")
def get_all_student(): 
    return jsonify(controller.db_read_all())

@app.get("/student/<student_id>")
def get_student(student_id:int): 
    return jsonify(controller.db_read(student_id))

@app.post("/student/")
def post_student():
    data = request.get_json()
    student = {'id':0,
        'name':data["name"],
        'course':data["course"]
    }    
    return jsonify(controller.db_write(student))

@app.put("/student/<student_id>")
def put_student(student_id):
    data = request.get_json()

    student = {
        'id':student_id,
        'name':data["name"],
        'course':data["course"]
    }    

    return jsonify(controller.db_update(student))

@app.delete("/student/<student_id>")
def delete_student(student_id):
    return controller.db_delete(int(student_id))


if __name__ == "__main__":
    app.run(debug=True)