

print("Think of number between 1 and 1000 and ill guess in 10 trys or less")
min = 0
correct = "correct"
check_cheater = 0
to_big = "less"
to_low = "more"
max = 1000
guess = int((max - min)/2 + min)
answer = ""
while answer != "correct":
    print(guess)
    inp = input("Is it too big? ")
    if inp == "yes":
        max = guess
        guess = int((max - min) / 2 + min)
    elif inp == "no":
        linp = input("Is it too small? ")
        if linp == "yes":
            min = guess
            guess = int((max - min) / 2 + min)
        elif linp == "no":
            print("Dont cheat")
            guess = int((max - min) / 2 + min)
    else:
        print("Sorry, I didn't understand, make sure to use 'yes' or 'no' ")
print(answer)