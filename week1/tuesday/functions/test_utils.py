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

assert format_test_name("Valid Login") == "test_valid_login"
assert format_test_name("  Search Results  ") == "test_search_results"
assert is_valid_test_name("test_login")
assert not is_valid_test_name("login_test")
assert not is_valid_test_name("test_")
