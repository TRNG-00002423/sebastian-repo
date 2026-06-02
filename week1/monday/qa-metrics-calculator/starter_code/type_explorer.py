def main():
    # Primitive variables
    age = 28
    price = 19.99
    name = "Alice"
    is_active = True
    result = None

    print("Variable Exploration:")
    print(f"  {'age':<12}= {str(age):<12} (type: {type(age).__name__})")
    print(f"  {'price':<12}= {str(price):<12} (type: {type(price).__name__})")
    print(f"  {'name':<12}= {str(name):<12} (type: {type(name).__name__})")
    print(f"  {'is_active':<12}= {str(is_active):<12} (type: {type(is_active).__name__})")
    print(f"  {'result':<12}= {str(result):<12} (type: {type(result).__name__})")

    print("\nOperators Demo:")
    print(f"  17 // 5     = {17 // 5:<12} (floor division)")
    print(f"  17 / 5      = {17 / 5:<12} (true division)")
    print(f"  \"QA \" * 3  = {'QA ' * 3}")
    print(f"  True + True = {True + True}")

    print("\nPrecision Gotcha:")
    print(f"  0.1 + 0.2  = {0.1 + 0.2} (not exactly 0.3!)")

    print("\n== vs is:")
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(f"  a = {a}, b = {b}")
    print(f"  a == b  → {a == b}  (same value)")
    print(f"  a is b  → {a is b}  (different object)")

    x = 42
    y = 42
    print(f"  x = {x}, y = {y}")
    print(f"  x == y  → {x == y}  (same value)")
    print(f"  x is y  → {x is y}  (CPython caches small ints, same object)")


if __name__ == "__main__":
    main()
