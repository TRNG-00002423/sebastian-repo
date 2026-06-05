class TestCase:
    total_created = 0

    def __init__(self, name, description, tags, priority="medium"):
        self.name = name 
        self.description = description 
        self.priority = priority 
        self.tags = tags

        TestCase.total_created += 1    

    def run(self):
        return "fail" not in self.name

    @classmethod
    def from_dict(cls, data):
        TestCase.total_created += 1    
        return cls(
            name=data["name"],
            description=data["description"],
            tags=data["tags"],
            priority=data.get("priority", "medium")
        ) 

    @staticmethod
    def is_valid_name(name):
        if not name[:5] == 'test_':
            return False
        if ' ' in name:
            return False
        return True
