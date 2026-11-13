import random

winningnums = random.sample(range(1, 60), 6)
ticket = random.sample(range(1, 60), 6)

print("Welcome to the Lottery")
print("Your ticket contains the numbers :", sorted(ticket))
print("The winning numbers are          :", sorted(winningnums))

commoncount = len(set(winningnums) & set(ticket))
print("Matching numbers                 :", commoncount)

match commoncount:
    case 6:
        print("Congratulations! You have won the jackpot!")
    case 5:
        print("Great job! You have won the second prize!")
    case 4:
        print("Good effort! You have won the third prize!")
    case 3:
        print("Nice! You have won the fourth prize!")
    case 2:
        print("You have won the fifth prize!")
    case 1:
        print("You have won the consolation prize!")
    case _:
        print("Sorry, you did not win this time. Better luck next time!")
