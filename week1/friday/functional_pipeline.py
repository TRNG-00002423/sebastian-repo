test_results = [
    {"name": "test_login", "module": "auth", "duration_ms": 1200, "status": "pass"},
    {"name": "test_register", "module": "auth", "duration_ms": 2100, "status": "pass"},
    {"name": "test_logout", "module": "auth", "duration_ms": 300, "status": "pass"},
    {"name": "test_search", "module": "search", "duration_ms": 850, "status": "fail"},
    {"name": "test_filter", "module": "search", "duration_ms": 1800, "status": "fail"},
    {"name": "test_sort", "module": "search", "duration_ms": 670, "status": "pass"},
    {"name": "test_add_cart", "module": "checkout", "duration_ms": 2300, "status": "fail"},
    {"name": "test_payment", "module": "checkout", "duration_ms": 3100, "status": "pass"},
    {"name": "test_confirm", "module": "checkout", "duration_ms": 1900, "status": "pass"},
    {"name": "test_view_profile", "module": "profile", "duration_ms": 380, "status": "pass"},
    {"name": "test_edit_profile", "module": "profile", "duration_ms": 540, "status": "pass"},
    {"name": "test_settings", "module": "profile", "duration_ms": 420, "status": "fail"},
]
test_results.sort(key=lambda x: x['duration_ms'])
print(test_results)

print("\n\n")
#Sort by module name, then by duration within each module.
#Sort by status ("fail" before "pass") then by name

test_results.sort(key=lambda x: (x['name'],x['duration_ms']))
print(test_results)

print("\n\n")
test_results.sort(key=lambda x: (x['status'],x['name']))
print(test_results)

print("\n\n")

#task 2

test_names = list(map(lambda x: x["name"], test_results))
print("Test names:", test_names)

failures = list(filter(lambda x: x["status"] == "fail", test_results))
print("Failures:", failures)

slow_tests = list(filter(lambda x: x["duration_ms"] > 1500, test_results))
print("Slow tests:", slow_tests)

summaries = list(map(
    lambda x: f"{'✅' if x['status'] == 'pass' else '❌'} {x['name']} ({x['duration_ms']}ms)",
    test_results
))
print("Summaries:", summaries)

modules = set(map(lambda x: x["module"], test_results))
print("Modules:", modules)

