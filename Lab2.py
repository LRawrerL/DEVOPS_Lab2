print("ET0735 (Devops for AIoT) - Lab 2 - Introduction to Python")

def display_main_menu(temperatures):
    print("display_main_menu")
    print("0. Input temperature")
    print("1. Calculate average")
    print("2. Find min/max")
    print("3. Sort temperature")
    print("4. Calculate median")
    print("5. Exit")

    selection = int(input("Please select: "))
    if selection == 5:
        print("Bye")
    elif len(temperatures) == 0 and selection != 0:
        print("Please input temperature first")
        display_main_menu(temperatures)
    else:
        if selection == 0:
            temperatures = get_user_input()
            print(temperatures)
            display_main_menu(temperatures)
        elif selection == 1:
            calc_average(temperatures)
            display_main_menu(temperatures)
        elif selection == 2:
            find_min_max(temperatures)
            display_main_menu(temperatures)
        elif selection == 3:
            sort_temp(temperatures)
            display_main_menu(temperatures)
        elif selection == 4:
            calc_median(temperatures)
            display_main_menu(temperatures)


def get_user_input():
    print("get_user_input")
    # counter = 0
    # temperatures = []
    # while counter < 5:
    #     temperature = float(input("Please enter temperature: "))
    #     temperatures.append(temperature)
    #     counter += 1
    # print(temperatures)
    # return temperatures
    temperatures = []
    while True:
        temperature_input = float(input("Please enter temperature (0 to exit):"))
        if temperature_input == 0:
            break
        else:
            temperatures.append(temperature_input)
    print(temperatures)
    return temperatures


def calc_average(temperatures):
    print("calc_average")
    print(temperatures)
    total = 0
    avg = 0
    for temperature in temperatures:
        total += temperature
    avg = total / len(temperatures)
    print("Average = " + str(avg))
    return avg


def find_min_max(temperatures):
    print("find_min_max")
    min_max = []
    min_max.append(min(temperatures))
    min_max.append(max(temperatures))
    print(min_max)
    return min_max


def sort_temp(temperatures):
    print("sort_temp")
    temperatures.sort()
    print(temperatures)
    return temperatures


def calc_median(temperatures):
    print("calc_median")
    temperatures.sort()
    # finding the median
    n = len(temperatures)
    if n % 2 == 0:
        median = (temperatures[n // 2 - 1] + temperatures[n // 2]) / 2
    else:
        median = temperatures[n // 2]
    # Print the median of the list
    print("Median of list is : " + str(median))


temperature = []
display_main_menu(temperature)
