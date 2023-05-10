"""'#cal_to_seconds = 24
#unit = "hours"
#import helper   --when I don't want the whole page just one of the function then
from helper import validate, user_input_msg
#from helper import *      #to import all from the helper


user_input = ""
while user_input != "exit":
    user_input = input(user_input_msg)
    days_and_unit = user_input.split(":")
    #print(days_and_unit)
    days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    #print(days_and_unit_dict)
    #print(type(days_and_unit_dict))
    validate(days_and_unit_dict)  #instead of helper.validate just use the validate(function)name directly"""

"""import os

print(os.name)"""

import logging

logger = logging.getLogger("MAIN")
logger.error("Error happened in the app")
