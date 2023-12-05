digits = {
  "one" : "1",
  "two" : "2",
  "three" : "3",
  "four" : "4",
  "five" : "5",
  "six" : "6",
  "seven" : "7",
  "eight" : "8",
  "nine" : "9",
}

def get_calibration_value(string):
    first_digit = None
    last_digit = None
    for index, char in enumerate(string):
        if char.isdigit():
            if first_digit is None:
                first_digit = char
            last_digit = char
            continue
        for number in digits:
          if string[index:].startswith(number):
              if first_digit is None:
                  first_digit = digits[number]
              last_digit =digits[number]

    return int(first_digit + last_digit)

with open("input.txt") as f:
    lines = f.readlines()
    sum_of_digits = 0
    for line in lines:
        sum_of_digits += get_calibration_value(line.strip())

    print(sum_of_digits)