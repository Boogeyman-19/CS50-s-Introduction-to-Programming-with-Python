import sys
import inflect

def main():
    p = inflect.engine()
    names = []

    print("Enter names, one per line (press Control-D when done):")
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        pass

    if len(names) == 0:
        sys.exit("Error: No names were entered.")

    formatted_names = p.join(names)
    print(f"Adieu, adieu, to {formatted_names}")

if __name__ == "__main__":
    main()
