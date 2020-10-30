"""
------------------------------------------------------------
- title: problem3.py
- Author: Rakesh Niraula
- Date: 2020-10-08 20:09:08
------------------------------------------------------------
"""

"""
------------------------------------------------------------
    Problem 3
    Code all these equations.
    (6 ^(2 + a) / (4 + b)) + (c + 180) * (b/a) * ( (6 + 2.8/3 - 3^2.5) / (4/3 * 7/(3 * 2.4)) )

    all parameters are inserted

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


def calculate(a: float, b: float, c:float):

    calc_value = (6 ** (2 + a) / (4 + b)) + (c + 180) * (b/a) * ( (6 + 2.8/3 - 3 ** 2.5) / (4/3 * 7/(3 * 2.4)) )

    return calc_value

if __name__ == "__main__":
    a = get_number("Enter a: ")
    b = get_number("Enter b: ")
    c = get_number("Enter c: ")

    calc_value = calculate(a, b,c)
    print("Calculated Value: ", calc_value)
