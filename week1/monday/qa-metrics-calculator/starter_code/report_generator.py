def main(test_names, duration, status):
    num_names = len(test_names)
    num_duration = len(duration)
    num_status = len(status)
    
    if not (num_duration == num_names == num_status):
        return "One list has more than the other, check your data and try again."
    
    title1="Test Name"
    title2="Duration"
    title3="Status"

    passed_tests = 0

    print(f"┌{"─"*18}┬{"─"*12}┬{"─"*10}┐") 
    print(f"| {title1:<17}| {title2:<11}| {title3:<9}| ")
    print(f"├{"─"*18}┼{"─"*12}┼{"─"*10}┤") 
    
    for t,d,s in zip(test_names, duration, status):
        sign = ""
        if s == "PASS":
            passed_tests += 1
            sign = "✅" 
        else:
            sign = "❌"
        
        print(f"| {t:17}| {d:>7,} ms | {sign} {s:<6}|")
        

    print(f"├{"─"*18}┼{"─"*12}┼{"─"*10}┤")

    tests_text = f"{passed_tests}/{num_status} Pass"
    print(f"| {"TOTAL":<17}| {sum(duration):>7,} ms | {tests_text:<9}| ")
    print(f"└{"─"*18}┴{"─"*12}┴{"─"*10}┘") 
'''
 test_login       │   1,200 ms │ ✅ PASS  │
│ test_search      │     850 ms │ ✅ PASS  │
│ test_checkout    │   2,300 ms │ ❌ FAIL  │
│ test_profile     │     450 ms │ ✅ PASS  │
│ test_logout      │     180 ms │ ✅ PASS  
'''
names = ["test_login","test_search","test_checkout","test_profile","test_logout"]
dura = [1200, 850, 2300, 450, 180]
status = ["PASS", "PASS", "FAIL", "PASS", "PASS"]
if __name__ == "__main__":
    main(names,dura,status)
