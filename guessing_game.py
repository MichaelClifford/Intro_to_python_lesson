def start_game(range_to_guess = 100):

    """""
    This will be our main function that access and controls the other functions needed to play our 
    guessing game. 
    
    It will take as an input the largest number we want to guess. If no number is provided it will 
    default to 100,
    
    """""
    
    # Initialize our game
    completed = False # Did we guess the righ numeber yet?
    possible_answers = make_list(range_to_guess) # what are the possible solutions? 
    guess = make_a_guess(possible_answers) # Let's make our first guess
    
    # Interact with the Player
    print(f'Ok, Lets Play a game.')
    print(f'Think of a number between 0 and {range_to_guess}.')
    
    input("click any button when you are ready to play!")
    
    while completed == False:  
        possible_answers, completed = guessing_game_turn(guess, possible_answers, completed)
        guess = make_a_guess(possible_answers)
        
        
def guessing_game_turn(guess,possible_answers, completed):
    
    """""
    This function represents one turn of the guessing program. This is by far the most complicated of 
    the functions and it relies on additional functions and nested if/else statements. 
    
    Could we make this function even simpler by making more functions? 
    
    """""
    
    answer = input(f'Are you thinking of the number {guess}?')
    
    if answer.lower() == 'no':
        up_or_down = input("Is the number you are thinking of higher or lower?")
        
        if up_or_down.lower() == 'lower':
            possible_answers = cut_list_in_half("lower",possible_answers)
        
        elif up_or_down.lower() == 'higher':
            possible_answers = cut_list_in_half("higher", possible_answers)
        
        return possible_answers, False
        
        
    elif answer.lower() == "yes":
        completed = True
        print("Horray! I guessed right!")

        return possible_answers, True

    
def make_list(range_to_guess):
    
    """"" 
    This function takes in a number and outputs a list of integers up to that number
    
    """""
    
    my_list = []
    for i in range(range_to_guess):
        my_list.append(i)
        
    return my_list


def make_a_guess(current_list):
    
    """""
    This function finds the middle number in our list and makes the binary search guess
    
    """""
    
    middle_of_list = len(current_list)//2
    return current_list[middle_of_list]


def cut_list_in_half(direction, current_list):
    
    """""
    This function updates the list of possible guesses by cutting it in half after each incorrect guess. 
    
    """""
    
    middle_of_list = len(current_list)//2
    
    if direction == 'lower':
        current_list = current_list[:middle_of_list]
        
    elif direction == 'higher':
        current_list = current_list[middle_of_list:]
        
    return current_list


if __name__ == '__main__':
    
    start_game()
    
    
    

