r1 = ['_','_','_','_','_','_',' ',' ',' ']  

def grid(pos, val):
    r1[pos] = val
    matrix = f"""
        _{r1[0]}_|_{r1[1]}_|_{r1[2]}_
        _{r1[3]}_|_{r1[4]}_|_{r1[5]}_
         {r1[6]} | {r1[7]} | {r1[8]}
            """
    print(matrix)

def reset_board():
    global r1
    r1 = ['_'] * 6 + [' '] * 3  
def is_win(choice):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  
        (0, 3, 6), (1, 4, 7), (2, 5, 8), 
        (0, 4, 8), (2, 4, 6)  
    ]
    
    for a, b, c in win_conditions:
        if r1[a] == r1[b] == r1[c] == choice:
            print(f'{choice} win')
            again = input("Do you want to play again (Yes/No): ")
            if again.lower() == "yes":
                reset_board()
                grid(0,"_")
                user(1)  
            return True
    return False

def check(used, user_pos):
    if user_pos in used:
        return True
    else:
        used.append(user_pos)
        return False

def user(num):
    used = []
    tries = 1
    while num <= 9:  
        choice = "X" if num % 2 == 1 else "O"
        user_pos = int(input(f"{choice}'s turn (1-9) > ")) - 1
        
        if user_pos < 0 or user_pos >= 9:
            print('Error: Invalid position')
            continue
        
        if check(used, user_pos):
            print("Error: Position already taken")
            continue
        
        grid(user_pos, choice)
        
        if num >= 5:  
            if is_win(choice):
                break
        
        num += 1
    
    if num > 9:
        print("It's a draw!")
        again = input("Do you want to play again (Yes/No): ")
        if again.lower() == "yes":
            reset_board()
            user(1)

print("Starting Tic-Tac-Toe!")
grid(0, '_')  
user(1)
