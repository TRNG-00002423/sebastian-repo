"""
QA Test Metrics Calculator
Fill in the code below where you see # TODO comments.
"""

def main():
    print("═" * 40)
    print("  QA Test Metrics Calculator")
    print("═" * 40)

    # TODO 1: Get user input
    # - Total test cases (convert to int)
    # - Passed tests (convert to int)
    # - Total execution time in seconds (convert to float)

    print("")

    total_tests = int(input("Enter total test cases: "))
    passed_tests = int(input("Enter passed test cases: "))
    total_time = float(input("Enter total execution time (seconds): "))

    failed_tests = total_tests-passed_tests
    pass_rate = (passed_tests/total_tests)*100
    fail_rate = (failed_tests/total_tests)*100
    avg_time = (total_time/total_tests)


    print("")

    print("-" * 40)
    print("  QA Test Metrics Calculator")
    print("-" * 40)
    print(f'Total Tests:\t{total_tests}\nPassed:          {passed_tests}\nFailed:           {failed_tests}\nPass Rate:       {pass_rate:.1f}%\nFail Rate:        {fail_rate:.1f}%\nAvg Time/Test:   {avg_time:.2f}s\nTotal Time:      {total_time:.2f}s\n')
    
    veredict = "Verdict: "
    
    if pass_rate >=95:
        veredict += "✅ RELEASE APPROVED"
    elif pass_rate >=80:
        veredict += "⚠️ CONDITIONAL RELEASE — review failures"
    else:
        veredict += "❌ RELEASE BLOCKED — too many failures"
    
    print(veredict)

if __name__ == "__main__":
    main()
