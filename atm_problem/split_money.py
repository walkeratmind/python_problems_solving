
total_50 = 10
total_20 = 20
total_10 = 100
total_5 = 100

total_money = {
    '50':10,
    '20':20,
    '10':100,
    '5':100
}

total_cash = sum(int(k) * v for k, v in total_money.items())
print("Total Amount: ", total_cash)

provived_cash = {'50': 0, '20': 0, '10': 0, '5': 0}

while total_cash >= 0:
    amount_to_withdraw = int(input("Amount: "))

    if amount_to_withdraw % 5 != 0:
        print("enter amount divisible by 5")
        break

    if total_cash > amount_to_withdraw:
        collected_cash = 0
        while collected_cash != amount_to_withdraw:
            # difference = amount_to_withdraw - collected_cash

            # add 50
            # possible_50 = int(difference / 50)
            # possible_20 = int(difference / 20)
            # possible_10 = int(difference / 10)
            # possible_5 = int(difference / 5)

            # if total_50 < possible_50:
            #     total_50 -= possible_50

            if (collected_cash + 50) <= amount_to_withdraw and total_50 != 0:
                provived_cash['50'] += 1
                total_50 -= 1
                collected_cash += 50

            if (collected_cash + 20)<= amount_to_withdraw and total_20 != 0:
                provived_cash['20'] += 1
                total_20 -= 1
                collected_cash += 20

            if (collected_cash + 10)<= amount_to_withdraw and total_10 != 0:
                provived_cash['10'] += 1
                total_10 -= 1
                collected_cash += 10

            if (collected_cash +5)<= amount_to_withdraw and total_5 != 0:
                provived_cash['5'] += 1
                total_5 -= 1
                collected_cash += 5

            print("Collected Cash : ", collected_cash)
        print("Provided Cash : ", provived_cash)
        print("Provided Sum: ", sum(int(k) * v for k, v in provived_cash.items()))
    else:
        print("not enough money...")

print("Finshed")

def add_cash(collected_cash, total_amount, total_no_cash):
    if (collected_cash +5)<= total_amount and total_no_cash != 0:
        provived_cash['5'] += 1
        total_no_cash -= 1
        collected_cash += 5
