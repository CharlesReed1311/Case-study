 
import random 

deck = [x for x in range(52)] 

suits = ["Spades", "Hearts", "Diamonds", "Clubs"] 
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", 
"10", "Jack", "Queen", "King"] 

random.shuffle(deck)

num = eval(input("Enter the number of cards you want to draw (1-52): "))

print("You have drawn the following cards:")
for i in range(num): 
     suit = suits[deck[i] // 13] 
     rank = ranks[deck[i] % 13] 
     print("The", rank, "of", suit)

