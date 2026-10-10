import pandas as pd
import os

# # 1)
# # Create a function called "car_at_light"
# # It should take one parameter: "light"
# # which gives the color of a traffic light.
# # If the color is "red", the function should return
# # "stop". If the color is "green", the function
# # should return "go". If the color is "yellow"
# # the function should return "wait". If the color
# # is anything else, the function should raise
# # an exception with the following message: 
# # "Undefined instruction for color: <light>" 
# # where <light> is the value of the parameter light.

def car_at_light(light: str):
    if light == "red":
        return print("stop")
    elif light == "green":
        return print("go")
    elif light == "yellow":
        return print("wait")
    else:
        raise ValueError(f"Undefined instruction for color: {light!r}")

# Uncomment below to test Q1
# q1_test_red = car_at_light("red")
# q1_test_yellow = car_at_light("yellow")
# q1_test_green = car_at_light("green")
# q1_test_blue = car_at_light("blue")
# print(q1_test_red)
# print(q1_test_yellow)
# print(q1_test_green)
# print(q1_test_blue)

# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 
# # 

def safe_subtract(first, second):
    try:
        return first-second
    except TypeError:
        return None

# Uncomment below to test Q2
# q2_test_int_sub_int = safe_subtract(1, 2)
# q2_test_int_sub_str = safe_subtract(1, "two")
# q2_test_str_sub_str = safe_subtract("one", "onetwo")
# print(q2_test_int_sub_int)
# print(q2_test_int_sub_str)
# print(q2_test_str_sub_str)

# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that return the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl

def retrieve_age_eafp(person):
    try:
        return 2026 - person['birth']
    except KeyError:
        return ("The age is missing")

def retrieve_age_lbyl(person):
    if "birth" in person:
        return 2026 - person['birth']
    else:
                return ("The age is missing")

## Uncomment below to test Q3
# john  = {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# janet = {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# print(retrieve_age_lbyl(john))     # expected: 39 (2026 - 1987)
# print(retrieve_age_lbyl(janet))    # expected: whatever you decided for a missing birth year

# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that takes the path to the file as an argument
# and reads the file making sure to use to handle the fact
# that it might not exist. 

def read_csv(file_path: str):
     if os.path.exists(file_path):
        df_data = pd.read_csv(file_path)
        print("data.csv was successfully read")
        print(df_data)
     else:
        print("Oh no! This file/filepath does not exist.")

# Uncomment below to test Q4
# existing_filepath = "data/test_spreadsheet.csv"
# nonexistent_filepath = "data1/test_spreadsheet.csv"
# q4_test_filepath_exists = read_csv(existing_filepath)
# q4_test_filepath_doesnt_exist = read_csv(nonexistent_filepath)     

# # 5) Squash some bugs! 
# # Find the possible logical errors (bugs) 
# # in the code blocks below. Comment in each of them
# # which logical errors did you find and correct them
# ### (a)
# total_double_sum = 0
# for elem in [10, 5, 2]:
#     double = elem * 2
#     total_double_sum += elem

# ### (b)
# strings = ''
# for string in ['I', 'am', 'Groot']:
#     strings = string+"_"+string

# ### (c) Careful!
# j=10
# while j > 0:
#    j += 1

# ### (d)
# productory = 0
# for elem in [1, 5, 25]:
#     productory *= elem