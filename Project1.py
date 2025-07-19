import random # random module is used to pick some random value 

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][lines]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet

    return winnings


def get_slot_machine_spin(rows, cols, symbols): # here we are creating a function to spin slot machine which has rows, cols, symbols
    all_symbols = []
    for symbol, symbol_count in symbols.items(): # .items() helps you get both the key and the value from a dictionary when you're looping through it.
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    # Transposing
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ") 
            else:
                print(column[row], end="")

        print()


 # section 1 Asking user to enter bet amount
def deposit(): # Here we created a function to collect the dposite from the user (function executes a block of code and return us a value)
    while True:
        amount = input("What would you like to deposite? $")
        if amount.isdigit(): # This here ensures that the user enters a valid number
            amount = int(amount) # Converting user input input integer after checking the input
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0") # if user enter -ve number then this will be printed
        else:
            print("Please enter a numebr.") # if user give some thing else other than digit as input this will print
    return amount

# section 2 Asking user on how many line they want to bet
def get_number_of_lines():
        while True:
            lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ") # Here we are asking to the no of lines between 1-3
            if lines.isdigit(): # checking if it's number
                lines = int(lines) # converting to int
                if 1 <= lines <= MAX_LINES: # chceking if the lines are in max range ie 1-3
                    break
                else:
                    print("Enter the valid number of lines") 
            else:
                print("Please enter a numebr.") 
    
        return lines 

# section 3 Asking user what would they like to bet 
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit(): 
            amount = int(amount) 
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.") # A way to automatically convert intiger values to string
        else:
            print("Please enter a numebr.") 
    
    return amount

# Main Function
def main():  # this is the main function
    balance = deposit()  # user deposite is the current balance
    lines = get_number_of_lines() # User no of lines to bet on
    while True:
        bet = get_bet() # user amount of bet on lines
        total_bet = bet * lines # The bet is multiplied as per the lines selected by user

        if total_bet > balance:  # Checking if the bet amount is available to bet on lines
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

main()