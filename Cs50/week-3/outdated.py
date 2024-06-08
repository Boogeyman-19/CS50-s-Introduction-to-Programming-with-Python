def main():
    import re

    # List of month names
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    month_to_number = {month: str(index).zfill(2) for index, month in enumerate(months, start=1)}

    while True:
        date_str = input("Enter a date (MM/DD/YYYY or Month D, YYYY): ").strip()

        match = re.match(r'^(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<year>\d{4})$', date_str)
        if match:
            month = match.group("month").zfill(2)
            day = match.group("day").zfill(2)
            year = match.group("year")
            if validate_date(month, day, year):
                print(f"{year}-{month}-{day}")
                break

        match = re.match(r'^(?P<month_name>[A-Za-z]+) (?P<day>\d{1,2}), (?P<year>\d{4})$', date_str)
        if match:
            month_name = match.group("month_name")
            day = match.group("day").zfill(2)
            year = match.group("year")
            if month_name in month_to_number and validate_date(month_to_number[month_name], day, year):
                print(f"{year}-{month_to_number[month_name]}-{day}")
                break

        print("Invalid date format. Please try again.")

def validate_date(month, day, year):

    try:
        month = int(month)
        day = int(day)
        year = int(year)
        if 1 <= month <= 12 and 1 <= day <= 31:
            return True
    except ValueError:
        return False
    return False

if __name__ == "__main__":
    main()
