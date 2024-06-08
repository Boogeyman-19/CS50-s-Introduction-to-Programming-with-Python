import sys
import csv

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python scourgify.py input.csv output.csv")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, mode='r') as infile:
            reader = csv.DictReader(infile)
            students = []
            for row in reader:
                last, first = row['name'].split(", ")
                students.append({"first": first, "last": last, "house": row["house"]})

        with open(output_file, mode='w', newline='') as outfile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                writer.writerow(student)

    except FileNotFoundError:
        sys.exit(f"Error: File '{input_file}' not found")
    except KeyError:
        sys.exit(f"Error: Incorrect format in input file '{input_file}'")
    except Exception as e:
        sys.exit(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
