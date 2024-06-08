import random

def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass
        print("Invalid input. Please enter a positive integer.")

def main():
    level = get_positive_integer("Enter a level: ")

    target = random.randint(1, level)

    while True:
        guess = get_positive_integer("Guess the number: ")

        if guess < target:
            print("Too small!")
        elif guess > target:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
