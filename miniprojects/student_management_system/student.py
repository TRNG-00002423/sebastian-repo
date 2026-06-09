class Student:
    def __init__(self, id:int, name:str, course:str) -> None:
        self.id:int = id
        self.name:str = name
        self.course:str = course
        
    def __repr__(self):
        return str({
            "id": self.id,
            "name": self.name,
            "course": self.course
        })
        
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "course": self.course
        }