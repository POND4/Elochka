def game(hiddenNumber, low, high):
    if low > high:
        return "Error"
    mid = (low + high) // 2

    if hiddenNumber > mid:
        print("Higher")
        return game(hiddenNumber, mid + 1, high)

    elif hiddenNumber < mid:
        print("Lower")
        return game(hiddenNumber, low, mid - 1)
    else:
        return "Game Over"

hiddenNumber = int(input("Enter a number between 1 and 100: "))
print(game(hiddenNumber, 1, 100))
