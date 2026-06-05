from test_management import TestCase, TestSuite, TestRunner

def main():
    t1 = TestCase("test_login_valid", "Valid login succeeds", ["smoke", "auth"], "high")
    t2 = TestCase("test_login_invalid", "Invalid login fails", ["auth"], "high")
    t3 = TestCase("test_logout", "User can log out", ["smoke"], "medium")
    t4 = TestCase("test_fail_on_empty_form", "Empty form shows error", ["regression"], "low")

    t5 = TestCase.from_dict({
        "name": "test_password_reset",
        "description": "Password reset email sent",
        "tags": ["regression", "auth"],
        "priority": "high"
    })
    t6 = TestCase.from_dict({
        "name": "test_fail_expired_token",
        "description": "Expired token rejected",
        "tags": ["auth"],
        "priority": "medium"
    })

    suite = TestSuite("Auth Suite", [])
    for t in [t1, t2, t3, t4, t5, t6]:
        suite.add_test(t)

    print(f"Total TestCase objects created: {TestCase.total_created}")
    print(f"Suite '{suite.name}' has {suite.count()} tests")

    high_priority = suite.get_by_priority("high")
    print(f"\nHigh-priority tests ({len(high_priority)}):")
    for t in high_priority:
        print(f"  - {t.name}")

    runner = TestRunner()
    results = runner.run(suite)
    runner.summary(results)

if __name__ == "__main__":
    main()
