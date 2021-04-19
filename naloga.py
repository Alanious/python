from random import randint
from collections import defaultdict
import json
import os

def reader():
    for line in open("data.csv", "r").read().splitlines():
        data = line.split(",")
        print(f"{data[0]} is {data[1]} years and {data[2]}")

#print(reader())

def secret_number():

    secret_nr = randint(1,30)
    guessed_numbers = []
    scores = []
    scores_file= defaultdict(list)
    attempts = 0
    name = input("Enter your name: ")
    scores_file["Name"] = name

    with open("scores_file.json", "r") as list_of_scores:
        for results in json.loads(list_of_scores.read()):
            all = "{0} guessed secret number {1} in {2} attempts. All the guesses were {3}".format(results.get("Name"),
                                                                                                    ",".join(map(str, (results.get("The right number")))),
                                                                                                    results.get("Attempts"),
                                                                                                    ",".join(map(str, (results.get("Guessed numbers")))))
            print(all)

    while True:
        attempts += 1
        guess = int(input("Guess the number between 1 and 30: "))
        if guess == secret_nr:
            scores_file["Attempts"] = attempts
            scores_file["Guessed numbers"].append(guess)
            scores_file["The right number"].append(guess)
            if "scores_file.json" not in os.listdir(os.getcwd()):
                scores.append(scores_file)
                with open("scores_file.json", "w") as s:
                    s.write(json.dumps(scores, indent=2))
            else:
                with open("scores_file.json") as newfile:
                    new = json.load(newfile)
                new.append(scores_file)
                with open("scores_file.json", "w") as n:
                    n.write(json.dumps(new, indent=2))
            return "Congratulation! You guessed the right number! "
        elif guess > secret_nr:
            print("Try something lower! ")
            scores_file["Guessed numbers"].append(guess)
        elif guess < secret_nr:
            print("Try something higher! ")
            scores_file["Guessed numbers"].append(guess)


#print(secret_number())

