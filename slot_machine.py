# working:-
# 1) user will deposit a certain amount of money
# 2) We're then going to allow them to bet on either one,two or 3 lines of a slot machine
# 3) Then determine if they won and allow them to keep playing until they quit or run out of money
from idlelib.searchengine import get_line_col

MAX_LINES=3 # Global value
MAX_BET = 10000
MIN_BET = 50
def deposit(): # responsible for collecting user input
    while True:
        amount = input("What would you like to deposit ? ₹")
        if amount.isdigit(): # checking if the input is integer
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def no_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1- "+ str(MAX_LINES)+" : )?")
        if lines.isdigit(): # checking if the input is integer
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

def get_bet():
    while True:
        amount = input("Enter the amount you like to bet on each line? ₹")
        if amount.isdigit(): # checking if the input is integer
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ₹{MIN_BET} and ₹{MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

def main():
    balance = deposit()
    lines = no_of_lines()
    while True:
        bet = get_bet()
        total = bet*lines

        if total >balance:
            print(f"You do not have enough to bet that amount, your current balance is: ₹{balance}")
        else:
            break

    print(f"You're betting ₹{bet} on {lines} lines. Total bet is equal to: ₹{total}")

main()