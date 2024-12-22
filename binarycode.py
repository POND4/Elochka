import random


def game(hiddenNumber, low, high):
    if low > high:
        return "Error"

    mid = (low + high) // 2
    print(f"Is the number {mid}?")

    answ = input("Enter 'H' for higher, 'L' for lower, or 'Y' if correct: ").strip().lower()

    if answ == "h":
        return game(hiddenNumber, mid + 1, high)
    elif answ == "l":
        return game(hiddenNumber, low, mid - 1)
    elif answ == "y":
        return f"Game Over: The hidden number was {hiddenNumber}!"
    else:
        print("Invalid input. Please type 'H', 'L', or 'Y'.")
        return game(hiddenNumber, low, high)


hiddenNumber = random.randint(1, 100)
print("Welcome to the Guessing Game!")
print("guess a number from 1 to 100.")
print(game(hiddenNumber, 1, 100))