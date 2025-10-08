import random

# Mapping: Snake = 1, Water = -1, Gun = 0
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# Get user input with validation
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
if youstr not in youDict:
    print("Invalid input! Please enter 's', 'w', or 'g'.")
    exit()

you = youDict[youstr]
computer = random.choice([-1, 0, 1])

print(f"You chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

# Determine the winner
if computer == you:
    print("It's a draw!")
elif (you - computer) % 3 == 1:
    print("You win!")
else:
    print("You lose!")
