def converter():
    print("Hi, this is a unit converter. It will easily convert your kilometers into miles.")
    while True:
        number = float(input("Enter amount of kilometers you want to convert: "))
        print(f"{number} kilometer is {number*0.62} miles.")
        if input("Do you want to perform another action? (y/n) ") == "y":
            continue
        return "Thank you for using our converter!"
#print(converter())


def fizzBuzz():
    number = int(input("Select a number between 1 and 100: "))
    for e in range(1, number+1):
        if e % 3 == 0 and e % 5 == 0:
            print("fizzbuzz")
        elif e % 3 == 0:
            print("fizz")
        elif e % 5 == 0:
            print("buzz")
        else:
            print(e)

#print(fizzBuzz())


def strings():
    string = input("Enter a string you want to convert: ")
    if input("Do you want to make lowercase or uppercase? (l/u) ") == "l":
        return string.lower()
    return string.upper()

print(strings())







