"""
------------------------------------------------------------
- title: problem4.py
- Author: Rakesh Niraula
- Date: 2020-10-08 20:25:34
------------------------------------------------------------
"""

"""
------------------------------------------------------------
    (e) Programs to covert the following units (the builder will enter the first unit in each case):
        - centimetre to millimetre
        - feet to meter
        - pound to kilogram
        - kilometres to meter
        - yard to inch
------------------------------------------------------------
"""


def get_number(msg: str):
    """Get Float Number from input

    Args:
        msg (str): message to display for input

    Returns:
        input_digit: value entered by user
    """
    while True:
        try:
            num = float(input(msg))
            break
        except ValueError:
            print("Not a valid Number. Please enter again...")

    return num


def cm_to_mm(input_value):
    # 1 cm = 10 mm
    return input_value * 10


def feet_to_meter(input_value):
    # 1 ft = 0.3048 m
    return input_value * 0.3048


def kilometres_to_meter(input_value):
    # 1 km = 1000 m
    return input_value * 1000


def pound_to_kg(input_value):
    # 1 lb = 0.45359237 kg
    return input_value * 0.45359237


def yard_to_inch(input_value):
    # 1 yd = 36 in
    return input_value * 36


def all_operation(input_value):
    print("Input Value: ", input_value)
    print("cm to mm: {} mm".format(cm_to_mm(input_value)))
    print("feet to meter: {} m".format(feet_to_meter(input_value)))
    print("kilometres to meter: {} m".format(kilometres_to_meter(input_value)))
    print("pound to kilogram: {} kg".format(pound_to_kg(input_value)))
    print("yard to inch: {} in".format(yard_to_inch(input_value)))


def options():
    print("-----------------------------")
    print("\tUNIT CONVERTER")
    print("-----------------------------")
    print("1. centimetre to millimetre")
    print("2. feet to meter")
    print("3. kilometres to meter")
    print("4. pound to kilogram")
    print("5. yard to inch")
    print("6. Perform all Operation")

    while True:
        try:
            option = int(input("Select Option: "))
        except:
            print("Not a Valid Number, Please enter again...")
            continue

        if option < 1 or option > 6:
            print("Invalid Input. Select from (1-6)...")
            continue
        break

    return option


if __name__ == "__main__":
    option = options()

    value = get_number("Enter Number: ")

    # Convert values as per by selected option

    # Using if elif

    # if option == 1:
    #     pass
    # elif option == 2:
    #     pass
    # if option == 6:
    #     all_operation(value)

    # save all function to dictionary and select the required function
    # such as : key is option and value for dict is function

    convert_options = {1: cm_to_mm, 2: feet_to_meter, 3: kilometres_to_meter,
                       4: pound_to_kg, 5: yard_to_inch, 6: all_operation}

    if option == 6:
        all_operation(value)
    else:
        converted_val = convert_options[option](value)
        print("{}: {} ".format(convert_options[option].__name__, converted_val))

