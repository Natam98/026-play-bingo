from random import sample, shuffle
from itertools import product
from statistics import mean

def create_bingo_card()-> dict[str, list[int]]: 

    bingo_columns: str = "BINGO"
    bingo_card: dict[str, list[int]] = {}

    start_range: int = 1
    for column in bingo_columns:
        bingo_card[column]=sample(range(start_range, start_range + 15), 5)
        start_range+=15
    
    return bingo_card


def display_bingo_card(bingo_card: dict[str, list[int]]) -> None:
    
    print("B    I    N    G    O")
    print("-"*23)
    for row in range(5):
        for column in bingo_card:
            print(f"{bingo_card[column][row]:<5}", end="")
        print()


def is_a_winning_bingo_card(bingo_card: dict[str, list[int]]) -> bool: 
    
    # Check for a winning row: five zeros in a horizontal line
    for index_row in range(5):
        if all(bingo_card[column][index_row] == 0 for column in bingo_card):
            return True

    
    # Check for a winning column: five zeros in a vertical line
    for column in bingo_card:
        if all(number == 0 for number in bingo_card[column]):
            return True
        
           
    # Check for a winning primary diagonal: five zeros from top-left to bottom-right

    if all(bingo_card[column][index_row] == 0 for index_row, column in enumerate(bingo_card)):
        return True
    

    # Check for a winning secondary diagonal: five zeros from top-right to bottom-left

    if all(bingo_card[column][4-index_row] == 0 for index_row, column in enumerate(bingo_card)):
        return True
    
    
    return False


def generate_bingo_calls() -> list[tuple[str, int]]:

    bingo_columns: str = "BINGO"
    start_range: int = 1
    bingo_calls: list[tuple[str, int]] = []

    for column in bingo_columns:
        
        bingo_calls.extend(list(product(column, range(start_range, start_range + 15))))
        start_range += 15

    shuffle(bingo_calls)
    return bingo_calls

 
def mark_called_number(bingo_card: dict[str, list[int]], bingo_call: tuple[str, int]) -> None:
    column: str
    number: int
    column, number = bingo_call
    
    if number in bingo_card[column]:
        
        index_to_mark: int
        index_to_mark = bingo_card[column].index(number)
        bingo_card[column][index_to_mark] = 0


def simulate_single_game() -> int:
    
    bingo_card: dict[str, list[int]] = create_bingo_card()
    bingo_calls: list[tuple[str, int]] = generate_bingo_calls()
    number_of_calls: int = 0
    
    for call in bingo_calls:
        mark_called_number(bingo_card, call)
        number_of_calls += 1
        
        if is_a_winning_bingo_card(bingo_card):
            return number_of_calls
              
    return number_of_calls

    
def main():
    
    NUMBER_OF_GAMES = 1000    
    calls_per_game: list[int] = []

    for _ in range(NUMBER_OF_GAMES):
        number_of_calls: int
        number_of_calls = simulate_single_game()
        
        calls_per_game.append(number_of_calls)
    
    print(f"Statistics of Bingo wins over {NUMBER_OF_GAMES} games:")
    print(f"- Minimum number of calls to win: {min(calls_per_game)}")
    print(f"- Maximum number of calls to win: {max(calls_per_game)}")
    print(f"- Average number of calls to win: {mean(calls_per_game):.2f}")
    

if __name__=="__main__":
    main()