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

class TestResult:
    def __init__(self, test_name:str, status:str,  duration_ms:float, error_message=None) -> None:
        self.test_name:str = test_name 
        self.status:str = status 
        self.duration_ms:float = duration_ms 
        self.error_message = error_message 
    
    def summary(self):
        icon = {"pass":"✅","fail":"❌"}
        return f"{icon[self.status]} {self.test_name} ({self.duration_ms}ms {self.error_message}) "
        
