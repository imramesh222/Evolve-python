def match_case_example(value):
    match value:
        case 1:
            print("Value is 1")
        case 2:
            print("Value is 2")
        case _:
            print("Value is something else")

match_case_example(1)  # Output: Value is 1
match_case_example(3)  # Output: Value is something else
