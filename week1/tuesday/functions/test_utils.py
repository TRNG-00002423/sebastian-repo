import re

def format_test_name(name)-> str:
    result = "test"
    for n in name.lower().split():
        result += f"_{n}"
    return result

def is_valid_test_name(name)-> bool:
    if len(name) < 6 :
        #print("size")
        return False
    if not "test_" == name[:5]:
        #print("not test_")
        return False
    pattern = r'^[a-z0-9_]+$'
    #print("regex")
    return bool(re.match(pattern, name))

#print(is_valid_test_name("test_login"))

def create_test_result(name, status="pass", duration_ms=0, error=None):
    return {"name":name, "status": status, "duration_ms": duration_ms, "error":error}


def format_duration(ms, unit="ms"):
    unit_dict = {"ms":1, "s": 1000, "min":100}
    if unit == "s":
        return f"{ms/1000:,.2f}{unit}"
    if unit == "min":
        return f"{ms/100:,.2f}{unit}"
    return f"{ms:,}{unit}"

def calculate_stats(*scores):
    count = len(scores)
    total = sum(scores)
    average = total/count
    mini = min(scores)
    maxi = max(scores)

    return {
            "count": count, 
            "total": total, 
            "average": average,
            "min": mini,
            "max": maxi
            }
   

def build_test_config(**settings):
    config = {
        "browser": "chrome",
        "headless": False,
        "timeout": 30,
        "retries": 0,
        "base_url": "http://localhost:3000"
    }
    for key, value in settings.items():
        config[key] = value
    return config
   
#Test task 1
assert format_test_name("Valid Login") == "test_valid_login"
assert format_test_name("  Search Results  ") == "test_search_results"
assert is_valid_test_name("test_login")
assert not is_valid_test_name("login_test")
assert not is_valid_test_name("test_")

#test task 2
r1 = create_test_result("test_login")
assert r1 == {"name": "test_login", "status": "pass", "duration_ms": 0, "error": None}

r2 = create_test_result("test_checkout", status="fail", duration_ms=2300, error="Timeout")
assert r2["status"] == "fail"
assert r2["error"] == "Timeout"

assert format_duration(1200) == "1,200ms"
assert format_duration(1200, "s") == "1.20s"

#test task 3
stats = calculate_stats(85, 92, 78, 95, 88)
assert stats["count"] == 5
assert stats["average"] == 87.6
assert stats["min"] == 78
assert stats["max"] == 95

config = build_test_config(headless=True, timeout=60)
assert config["browser"] == "chrome"  # default
assert config["headless"] == True     # overridden
assert config["timeout"] == 60       # overridden
