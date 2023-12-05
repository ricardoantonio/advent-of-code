def get_calibration_value(string):
    first_digit = None
    last_digit = None
    for char in string:
        if char.isdigit():
            if first_digit is None:
                first_digit = char
            last_digit = char
    return int(first_digit + last_digit)


with open("input.txt") as f:
    lines = f.readlines()
    sum_of_digits = 0
    for line in lines:
        sum_of_digits += get_calibration_value(line.strip())

    print(sum_of_digits)
        
