import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pizza.py <filename.csv>")

    filename = sys.argv[1]

    if not filename.endswith(".csv"):
        sys.exit("Error: Not a CSV file")

    try:
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
    except FileNotFoundError:
        sys.exit(f"Error: File '{filename}' not found")
    except Exception as e:
        sys.exit(f"Error: {e}")


    table = tabulate(data, headers='firstrow', tablefmt='grid')

    print(table)

if __name__ == "__main__":
    main()
