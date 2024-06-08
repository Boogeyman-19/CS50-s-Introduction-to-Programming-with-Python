def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not s[:2].isalpha():  # Check if the first two characters are letters
        return False

    if not s.isalnum():
        return False

    seen_digit = False

    for char in s:
        if char.isdigit():
            if not seen_digit and char == '0':
                return False
            seen_digit = True
        elif seen_digit:
            return False

    return True

if __name__ == "__main__":
    main()
