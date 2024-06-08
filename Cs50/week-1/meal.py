
def convert(time):

    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60

def main():

    time = input("Enter a time in 24-hour format : ")

    time_in_hours = convert(time)
    if 7.00 <= time_in_hours <= 8.00:
        print("breakfast time")
    elif 12.00 <= time_in_hours <= 13.00:
        print("lunch time")
    elif 18.00 <= time_in_hours <= 19.00:
        print("dinner time")

if __name__ == "__main__":
    main()
