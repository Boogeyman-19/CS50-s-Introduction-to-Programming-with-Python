import sys

def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python lines.py <filename>")

    filename = sys.argv[1]

    if not filename.endswith(".py"):
        sys.exit("Error: Not a Python file")

    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit(f"Error: File '{filename}' not found")

    loc = count_lines_of_code(lines)
    print(loc)

def count_lines_of_code(lines):
    loc = 0
    for line in lines:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith("#"):
            loc += 1
    return loc

if __name__ == "__main__":
    main()
