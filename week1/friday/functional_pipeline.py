from functools import reduce

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

# task 3

total_duration = reduce(lambda acc, x: acc + x["duration_ms"], test_results, 0)
print("Total duration:", total_duration)

failure_time = reduce(lambda acc, x: acc + x["duration_ms"] if x["status"] == "fail" else acc, test_results, 0)
print("Total failure time:", failure_time)

longest_name = reduce(lambda acc, x: x["name"] if len(x["name"]) > len(acc) else acc, test_results, "")
print("Longest test name:", longest_name)

module_summary = reduce(
    lambda acc, x: {**acc, x["module"]: acc.get(x["module"], 0) + 1},
    test_results,
    {}
)
print("Module summary:", module_summary)

# task 4
endpoints = ["/login", "/search", "/checkout", "/profile"]
expected_codes = [200, 200, 201, 200]
actual_codes = [200, 500, 201, 403]

for endpoint, expected, actual in zip(endpoints, expected_codes, actual_codes):
    status = "PASS" if expected == actual else "FAIL"
    print(f"{status}: {endpoint} expected={expected} actual={actual}")

names, modules_list, durations, statuses = zip(*[
    (r["name"], r["module"], r["duration_ms"], r["status"]) for r in test_results
])
print("Names:", names)
print("Modules:", modules_list)
print("Durations:", durations)
print("Statuses:", statuses)

name_to_duration = dict(zip(
    map(lambda x: x["name"], test_results),
    map(lambda x: x["duration_ms"], test_results)
))
print("Name to duration:", name_to_duration)
