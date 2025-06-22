from random import randint
easy_level_turns = 5
hard_level_turns =10

# break up code into sections

#guess check
def answer_check(guest_answer, actual_answer):
    if guest_answer < actual_answer:
        print (f"You guessed too low")
    elif guest_answer > actual_answer:
        print (f"You guessed too high")
    else:
        print(f"You guessed correct, tha answer is {answer}")
        
#difficulty level
def difficulty_level():
    diff_level = input("Choose a level: Easy or Hard ")
    if diff_level == "easy":
        return easy_level_turns
    else:
        return hard_level_turns


print("welcome to Guess-o-rama")
print("Guess a number from 1 to 100 ")
answer = randint(1,100)
guess = int(input("Make your guess: "))
turns = difficulty_level()
print(f"You have {turns} left")