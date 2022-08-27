


def only_numbers(string):
    emp_string=""
    for m in string:
        if m.isdigit():
            emp_string+=m
    return emp_string