# working:-
# 1) user will deposit a certain amount of money
# 2) We're then going to allow them to bet on either one,two or 3 lines of a slot machine
# 3) Then determine if they won and allow them to keep playing until they quit or run out of money

import random
MAX_LINES=3 # Global value
MAX_BET = 10000
MIN_BET = 50

ROWS=3
COLS=3

symbol_count ={
    "A":2,
    'B':4,
    'C':6,
    'D':8
}

symbol_values ={
    "A":5,
    'B':4,
    'C':3,
    'D':2
}

def check_winnings(columns, lines, bet, values):
    winnings=0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line+1)
    return winnings, winning_lines



def get_slot_machine_spin(rows, cols, symbols):
    all_symbols=[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] # slicing is used to copy a list
        for _ in range(rows):
            value = random.choice (all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

def print_slot_machine(columns):
    #transposing the upper matrix
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end='')

        print()



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

def game(balance):
    lines = no_of_lines()
    while True:
        bet = get_bet()
        total = bet * lines

        if total > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ₹{balance}")
        else:
            break

    print(f"You're betting ₹{bet} on {lines} lines. Total bet is equal to: ₹{total}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ₹{winnings}")
    print(f"You won on lines", *winning_lines)  # unpack operator !wow
    return winning_lines - total



def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        spin = input("Press enter to spin {press q to quit}: ")
        if spin =='q':
            break
        balance +=spin()
    print(f"You left with ₹{balance} ")
main()