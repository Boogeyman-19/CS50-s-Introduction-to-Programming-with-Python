def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    try:
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        if x > y:
            raise ValueError("X cannot be greater than Y.")

        return round((x / y) * 100)
    except (ValueError, ZeroDivisionError) as e:
        raise e
    except Exception:
        raise ValueError("Invalid input. Ensure X and Y are integers and in the form X/Y.")

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
