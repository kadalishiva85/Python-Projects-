import random  # Import the random module to pick random values

# Constants for the slot machine
MAX_LINES = 3  # Maximum number of lines you can bet on
MAX_BET = 100  # Maximum bet per line
MIN_BET = 1    # Minimum bet per line

ROWS = 3  # Number of rows in the slot machine
COLS = 3  # Number of columns in the slot machine

# Dictionary to store how many of each symbol are in the slot machine
symbol_count = {
    "A": 2,  # There are 2 'A' symbols
    "B": 4,  # There are 4 'B' symbols
    "C": 6,  # There are 6 'C' symbols
    "D": 8   # There are 8 'D' symbols
}

# Dictionary to store the value (multiplier) for each symbol
symbol_value = {
    "A": 5,  # 'A' pays 5x your bet
    "B": 4,  # 'B' pays 4x your bet
    "C": 3,  # 'C' pays 3x your bet
    "D": 2   # 'D' pays 2x your bet
}

def check_winnings(columns, lines, bet, values):
    """
    Checks each line the user bet on to see if all symbols match.
    If they do, add winnings for that line.
    Returns total winnings and a list of winning lines.
    """
    winnings = 0
    winning_lines = []
    for line in range(lines):  # Loop through each line the user bet on
        symbol = columns[0][line]  # Take the symbol from the first column for this line
        for column in columns:  # Check the same row in every column
            symbol_to_check = column[line]
            if symbol != symbol_to_check:  # If any symbol doesn't match, break
                break
        else:
            # If all symbols matched, add winnings for this line
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)  # Store the line number (1-indexed)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    """
    Randomly generates the slot machine columns based on the symbol counts.
    Returns a list of columns, each containing symbols for that column.
    """
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)  # Add each symbol the correct number of times
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)  # Pick a random symbol
            current_symbols.remove(value)  # Remove it so it's not picked again for this column
            column.append(value)  # Add symbol to the column

        columns.append(column)  # Add the column to the slot machine

    return columns

def print_slot_machine(columns):
    """
    Prints the slot machine in a row-by-row format for the user to see.
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ") 
            else:
                print(column[row], end="")
        print()  # Newline after each row

def deposit():
    """
    Asks the user to enter a deposit amount and checks if it's valid.
    Returns the deposit amount as an integer.
    """
    while True:
        amount = input("What would you like to deposite? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a numebr.")
    return amount

def get_number_of_lines():
    """
    Asks the user how many lines they want to bet on (1 to MAX_LINES).
    Returns the number of lines as an integer.
    """
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter the valid number of lines") 
        else:
            print("Please enter a numebr.") 
    return lines 

def get_bet():
    """
    Asks the user how much they want to bet on each line.
    Returns the bet amount as an integer.
    """
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit(): 
            amount = int(amount) 
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a numebr.") 
    return amount

def spin(balance):
    """
    Handles a single round of spinning the slot machine:
    - Asks user for number of lines and bet per line
    - Checks if user has enough balance
    - Spins the slot machine and prints the result
    - Calculates winnings and updates balance
    Returns the net change in balance (winnings - total bet)
    """
    lines = get_number_of_lines()  # User chooses how many lines to bet on
    while True:
        bet = get_bet()  # User chooses how much to bet per line
        total_bet = bet * lines  # Total bet is bet per line times number of lines

        if total_bet > balance:  # Check if user has enough money
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)  # Spin the slot machine
    print_slot_machine(slots)  # Show the result
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)  # Calculate winnings
    print(f"You won ${winnings}.")
    print(f"you won on lines:", *winning_lines)
    return winnings - total_bet  # Net change in balance

# Main Function
def main():
    """
    Main game loop:
    - Asks user to deposit money
    - Lets user play rounds until they quit
    - Shows balance after each round
    """
    balance = deposit()  # Get user's starting balance
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)  # Update balance after each round
    print(f"You left with ${balance}")

main()  # Start the game
