import random

def Check_for_winner():

    if grid[0][0] == grid[1][0] == grid[2][0] != " ":
        return grid[0][0]
    elif grid[0][1] == grid[1][1] == grid[2][1] != " ":
        return grid[0][1]
    elif grid[0][2] == grid[1][2] == grid[2][2] != " ":
        return grid[0][2]
    elif grid[0][0] == grid[0][1] == grid[0][2] != " ":
        return grid[0][0]
    elif grid[1][0] == grid[1][1] == grid[1][2] != " ":
        return grid[1][0]
    elif grid[2][0] == grid[2][1] == grid[2][2] != " ":
        return grid[2][0]
    elif grid[0][0] == grid[1][1] == grid[2][2] != " ":
        return grid[0][0]
    elif grid[0][2] == grid[1][1] == grid[2][0] != " ":
        return grid[0][2]
    else:
        return "Draw"

def Game_not_over():
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                return True
    return False

def Print_grid():
    for row in grid:
        print(" | ".join(row))
        print("-" * 9)

def Comp_move(grid, comp):
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] == ' ':
                empty_cells.append((i, j))
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = comp

grid = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

choice = input("Which symbol do you want? 'X' or 'O': ").upper()
while (choice != 'X' and choice != 'O'):
    choice = input("Invalid option... Choose 'X' or 'O': ").upper()

if choice == 'X': 
    comp = 'O'
else:
    comp = 'X'

turn = 'X'

while True:
    print('Let the game begin!')
    Print_grid()
    if turn == choice:
        print("Your turn!")
        while True:
            try:
                option = int(input("Enter your move (1-9): ")) - 1
                row = option//3
                col = option%3
                if grid[row][col] == ' ':
                    grid[row][col] = choice
                    break
                else:
                    print("This cell has already been played.. Enter another.")
            except (ValueError, IndexError):
                print("Invalid option... Enter again.")
    else:
        print("Opponet's turn...")
        Comp_move(grid, comp)
        
    result = Check_for_winner()
    
    if result == "X" or result == "O":
        Print_grid()
        print(result, "is the winner!\n")
        break
    
    elif result == "Draw":
        if Game_not_over():
            pass
        else:
            Print_grid()
            print(result)
            break
        
    if turn == comp:
        turn = choice
    elif turn == choice:
        turn = comp
