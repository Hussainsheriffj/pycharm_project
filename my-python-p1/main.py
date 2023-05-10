cal_to_seconds = 24
unit = "hours"


def validate():
    try:
        user_input_num = int(no_of_day_element)
        # we should accept the positive values only
        if user_input_num > 0:
            result = days_to_units(user_input_num)
            print(result)
        elif user_input_num == 0:
            print("you entered the value 0, please enter a +ve number")
        else:
            print("your input is not a valid no.")
    except ValueError:
        print("your input is a not valid, pls enter a number")


def days_to_units(no_of_days):
    return f"{no_of_days} days are {no_of_days * cal_to_seconds} {unit}"


user_input = ""
while user_input != "exit":
    user_input = input("enter number you want to convert as a comma separated list\n")
    list_of_days = user_input.split(", ")
    print(list_of_days)
    print(set(list_of_days))
    print(type(list_of_days))
    print(type(set(list_of_days)))
    for no_of_day_element in set(list_of_days):
        validate()






