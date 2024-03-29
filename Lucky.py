Lucky = 15
Guess = int(input("Guess the number:"))
if Guess <= Lucky - 3:
    print(" Too Low")
if Guess >= Lucky + 3:
    print("Too High")
if Guess == Lucky:
    print("Yes")
