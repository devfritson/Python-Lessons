schedule_list = ["1. Play Video Games", "2. Learn Python", "3. Go to class", "4. Do security research",
                 "5. Take a day trip", "6. Play the guitar", "7. Workout", "8. Have dinner", "9. Go to sleep"]

valid_options = [str(i) for i in range(1, len(schedule_list) + 1)]

daily_schedule = []

while True:
    print()
    print("-" * 80)
    print("-" * 80)
    print("Please select an option from the list below or enter quit to exit: ")
    print()
    for i in schedule_list:
        print(i)
    print()
    print("Your daily schedule:")
    for item in daily_schedule:
        print(item)
    print()
    selected_option = input("Please enter your option here: ")
    print()

    if selected_option == "quit":
        break
    elif selected_option not in valid_options:
        print("Invalid option!")
        print()

    else:
        selected_index = int(selected_option) - 1
        daily_schedule.append(schedule_list[selected_index])

print("Your daily schedule:")
for item in daily_schedule:
    print(item)
