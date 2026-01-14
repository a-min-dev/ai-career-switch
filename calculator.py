def main():
    print("--- AI Career Switch: Study Tracker ---")

    # input() will always return a string, even if the input is a number
    hours_week = input("How many hours did you study and review for the week?: ")

    # convert the input from a string to usable numbers
    # calculate the average hours studied/reviewed per day
    average_per_day = round((float(hours_week)/7), 2)

    print(f"The average study time per day over the last week: {average_per_day} hours")

main()
