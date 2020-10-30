"""
------------------------------------------------------------
- title: assement.py
- Author: Rakesh Niraula
- Date: 2020-10-08 18:47:09
------------------------------------------------------------
"""

"""
------------------------------------------------------------
   Problem 1

   (a) Write the code for these two equations. Let R=10000, C=1e-6, and Vs=10.
         T=RC
         Vc = Vs(1 - 10 ^ (t / T))

   The builder will enter t.
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


R = 10000
# 1e-6 == 1 * 10 ** -6
C = 1e-6
Vs = 10


def calculate(t):
    T = R * C
    Vc = Vs * (1 - 10 ** -(t / T))

   #  print(" -t/T: ",  -(t / T))
    return Vc


if __name__ == "__main__":
    # while True:
    #    try:
    #       t = float(input("Enter t: "))
    #       break
    #    except ValueError:
    #       print("Not a valid Number. Please enter again...")
    t = get_number("Enter t: ")

    Vc = calculate(t)
    print("Vc: ", Vc)
