"""
------------------------------------------------------------
- title: assessment.py
- Author: Rakesh Niraula
- Date: 2020-10-15 13:30:35
------------------------------------------------------------
"""

"""
------------------------------------------------------------
   TASK
   - develop & test small application that allow mobile phone to compare the cost of
   their phone usage on particular day under plans from three different phone providers and find most
   most expensive and cheapest from them.
------------------------------------------------------------
"""

"""
------------------------------------------------------------
   TODO
   - display welcome msg eg ************\n msg \n *****************
   -
   -
------------------------------------------------------------
"""

"""
helper functions
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


def get_option(msg: str, lower_val: int, upper_val: int):
    """Get Number from input

    Args:
        msg (str): message to display for input
        lower_val (int): lower input option
        upper_val (int): upper input option

    Returns:
        input_digit: value entered by user
    """
    while True:
        try:
            option = int(input(msg))
        except:
            print("Not a Valid Number, Please enter again...")
            continue

        if option < lower_val or option > upper_val:
            print("Value must be between {} and {}. Please try again.".format(
                lower_val, upper_val))
            continue
        break

    return option


def welcome_msg(msg: str):
    str_len = len(msg)
    print("*" * str_len)
    print(msg)
    print("")
    print("*" * str_len)


def main_menu_option():
    print("\nMAIN MENU\n")
    print("Please select from the menu:")
    print("1. Enter Usage Details")
    print("2. Display Cost Under Provider 1")
    print("3. Display Cost Under Provider 2")
    print("4. Display Cost Under Provider 3")
    print("5. Clear Usage Details")
    print("6. Exit System")

    while True:
        try:
            option = int(input("Select Option: "))
        except:
            print("Not a Valid Number, Please enter again...")
            continue

        if option < 1 or option > 6:
            print("Value must be between 1 and 6. Please try again.")
            continue
        break

    return option


def enter_usage_details():
    print("ENTER USAGE DETAILS MENU")
    print("Please select an option from the menu: ")
    print("1. Phone Call")
    print("2. SMS")
    print("3. Data Usage")
    print("4. Return to main menu")

    return get_option("Enter your selection: ", 1, 4)


def display_cost(provider, total_calls, total_call_sec, total_sms, total_data):

    selected_provider_cost = PROVIDERS_COST[provider]

    msg = "Cost under Provider {}".format(provider)
    print(msg)
    print("*" * len(msg))

    print("Provider {} Cost Scheme:".format(provider))
    print("Per phone call (flag fall charge): ${}".format(
        selected_provider_cost['per_phone_call']))
    print("Per second of total time over all phone calls: ${}".format(
        selected_provider_cost['per_sec_total_call']))
    print("Per SMS: ${}".format(selected_provider_cost['per_sms']))
    print("Per MB of data usage: ${}".format(selected_provider_cost['per_mb']))

    print("*" * len(msg))

    total_call_cost = total_calls * selected_provider_cost['per_phone_call']
    total_call_time_cost = total_call_sec * \
        selected_provider_cost['per_sec_total_call']
    total_sms_cost = total_sms * selected_provider_cost['per_sms']
    total_data_cost = total_data * selected_provider_cost['per_mb']

    total_cost = total_call_cost + total_call_time_cost + \
        total_sms_cost + total_data_cost

    print("Number of Calls = {} \t $ {}".format(total_calls, total_call_cost))
    print("Total call time(secs) = {} \t ${}".format(
        total_call_sec, total_call_time_cost))
    print("Number of SMS = {} \t ${}".format(total_sms, total_sms_cost))
    print("Data Usage (MB) = {} \t ${}".format(total_data, total_data_cost))
    print("*" * 80)
    print("\nTOTAL COST \t ${}".format(total_cost))

# def phone_call():
#     cll_len = get_number("Enter call length in seconds:")

#     total_calls = get_number("Total number of calls so far:")

#     enter_usage_details()


def main():
    total_calls_sec = 0
    total_calls = 0
    total_sms = 0
    total_data = 0

    while True:
        msg = "WELCOME TO PHONE BILL COMPARISION SYSTEM"
        welcome_msg(msg)

        option = main_menu_option()

        if option == 1:
            while True:
                one_option = enter_usage_details()
                if one_option == 1:
                    cll_len = get_number("Enter call length in seconds:")

                    total_calls_sec += cll_len
                    total_calls += 1
                    print("Total number of cals so far = {}".format(total_calls))
                if one_option == 2:
                    total_sms += 1
                    print("Total number of SMS so far = {}".format(total_sms))
                if one_option == 3:
                    data_in_mb = get_number("Enter total amt. of data in MB: ")
                    total_data += data_in_mb
                    print("Data amount so far {} MB".format(total_data))

                if one_option == 4:
                    break

        if option in range(2, 5):
            while True:
                display_cost(option - 2, total_calls, total_calls_sec,
                             total_sms, total_data)
                val = get_number("Enter 1 to return: ")
                if val == 1:
                    break
        if option == 5:
            total_calls_sec = 0
            total_calls = 0
            total_sms = 0
            total_data = 0

            msg = "All USAGE DETAILS HAVE BEEN RESET TO 0"
            print("*" * len(msg))
            print(msg)
            print("*" * len(msg))

        if option == 6:
            print("Good Bye...")
            break


PROVIDERS_COST = [{'per_phone_call': 0.20, 'per_sec_total_call': 0.03, 'per_sms': 0.10, 'per_mb': 0.02},
                  {'per_phone_call': 0.15, 'per_sec_total_call': 0.04,
                      'per_sms': 0.12, 'per_mb': 0.04},
                  {'per_phone_call': 0.2, 'per_sec_total_call': 0.2, 'per_sms': 0.2, 'per_mb': 0.2}]


if __name__ == "__main__":
    main()
