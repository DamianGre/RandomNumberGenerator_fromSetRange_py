import random

try:
    print("Hey, I will pick and print for you choosen number of random numbers from choosen range.")
    print("Enter min range: ")
    min = int(input())
    print("Enter maximum range: ")
    max = int(input())
    print("How many random numbers you want me to print: ")
    howMany = int(input())
    if (howMany <= 0):
        raise Exception("Wrong amount of random numbers!")
    if (max <= min):
        raise Exception("Wrong numbers range! Max cannot be smaller or equal then max!")
    for i in range(howMany):
        print(f"Number {i+1} random is: " + str(random.randint(min, max)))
except:
    print("An exception occurred")
