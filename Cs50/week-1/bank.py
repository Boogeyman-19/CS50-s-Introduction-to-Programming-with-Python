def main():
    greeting = input("Greeting: ")
    print(value(greeting))

def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
