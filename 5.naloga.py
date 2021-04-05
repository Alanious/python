def mood_checker():
    mood = input("Enter your mood: ")
    if mood == "happy":
        return "It is great to see you happy"
    elif mood == "nervous":
        return "Take a deep breath 3 times"
    elif mood == "sad":
        return "Read some positive thought"
    elif mood == "positive":
        return "Stay that way"
    return "I don't recognize that mood"

#print(mood_checker())

def secret_number():
    count = 1
    nr = 15
    while count <= 3:
        guess = int(input("Guess the number: "))
        if guess == nr:
            return "Congrats! You guessed the right number!"
            break
        else:
            print("Sorry you're out of luck!")
            count += 1
    return "You ran out of guesses!"

#print(secret_number())


def calculator():
    num1 = int(input("Enter a first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Select a operator: ")

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    return "I don't recognize that operator!"

#print(calculator())


