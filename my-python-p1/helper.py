def days_to_units(no_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{no_of_days} days are {no_of_days * 24} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{no_of_days} days are {no_of_days * 24 * 60} {conversion_unit}"
    else:
        return "unsupported unit"


def validate(days_and_unit_dict):
    try:
        user_input_num = int(days_and_unit_dict["days"])
        # we should accept the positive values only
        if user_input_num > 0:
            result = days_to_units(user_input_num, days_and_unit_dict["unit"])
            print(result)
        elif user_input_num == 0:
            print("you entered the value 0, please enter a +ve number")
        else:
            print("your input is not a valid no.")
    except ValueError:
        print("your input is a not valid, pls enter a number")


user_input_msg = "enter no. of days and conversion units. eg. 20:hours\n"