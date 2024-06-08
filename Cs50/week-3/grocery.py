def main():
    import sys
    from collections import defaultdict

    grocery_dict = defaultdict(int)

    print("")

    try:
        while True:
            item = input().strip().lower()
            grocery_dict[item] += 1
    except EOFError:
        pass

    sorted_items = sorted(grocery_dict.items())

    for item, count in sorted_items:
        print(f"{count} {item.upper()}")

if __name__ == "__main__":
    main()
