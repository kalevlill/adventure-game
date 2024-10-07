def end_game():
    print("Thanks for playing, until next time")
def solve_riddle(riddle):
    print(riddle['Question'])
    answer = input("Your answer: \n")
    if answer.strip().lower() == riddle['answer'].strip().lower():
        print("Well done! Your answer is correct")
        return True
    else: 
        print("Your answer is wrong, try again")
        return False
def enter_room(room):
    print(room['name'])
    print(room['description'])

    solved = False
    while not solved:
        solved = solve_riddle(room['riddle'])
