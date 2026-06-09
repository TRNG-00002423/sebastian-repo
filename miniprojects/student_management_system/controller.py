import json

def db_size():
    with open('db.json', 'r') as f:
        json_file = json.load(f)        
    return len(json_file)

def db_read_all():
    with open('db.json', 'r') as f:
        json_file = json.load(f)
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

def db_update(student):
    with open('db.json', 'r') as f:
        db_json = json.load(f)
        db_json[int(student['id'])] = student
    with open('db.json', 'w') as f:
        json.dump(db_json, f, indent=4) 
    return student

def db_delete(student_id:int):
    with open('db.json', 'r') as f:
        db_json = json.load(f)   
        if student_id > len(db_json):
            return {'status':401,"message":"User ID VERY invalid"}
        elif db_json[student_id]['id'] != student_id:
            return {'status':401,"message":"User ID not valid"}
        else:
            db_json[student_id] = {"id": student_id,
        "name": "null",
        "course": "null"}
    with open('db.json', 'w') as f:
        json.dump(db_json, f, indent=4)
        return {'status':200,"message":"User succesfully removed"}
        
        
        