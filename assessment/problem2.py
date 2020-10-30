"""
------------------------------------------------------------
- title: problem2.py
- Author: Rakesh Niraula
- Date: 2020-10-08 19:21:39
------------------------------------------------------------
"""

"""
------------------------------------------------------------
    (b) Write the code to implement the equation below (ignore the units).
    Let G = 6.67 and r = 384e6 m.

        Fg = G * (m1 * m2) / r^2

    The user will enter m1 and m2.
------------------------------------------------------------
"""


G = 6.67 * 10 ** -11
r = 384e6


def calculate(m1: float, m2: float):
    """Calculate acceleration due to gravity between to masses

    Args:
        m1 (float): [description]
        m2 (float): [description]
    """

    F = G * (m1 * m2) / r ** 2
    return F


if __name__ == "__main__":
    while True:
        try:
            m1 = float(input("Enter m1: "))
            m2 = float(input("Enter m2: "))
            break
        except ValueError:
            print("Not a valid Number. Please enter again...")

    F = calculate(m1, m2)
    print("Fg: {} m/s^2".format(F))
