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
        return "stop"
    elif light == "green":
        return "go"
    elif light == "yellow":
        return "wait"
    else:
        raise ValueError(f"Undefined instruction for color: {light}")

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
        return first - second
    except TypeError:
        return None
    except Exception as error:
        print(f"An error occurred: {error}")

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
        return "The age is missing"

def retrieve_age_lbyl(person):
    if "birth" in person:
        return 2026 - person['birth']
    else:
        return "The age is missing"

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

def read_data(file_path: str):
    try:
        df_data = pd.read_csv(file_path)
        print("data.csv was successfully read")
        print(df_data)
    except FileNotFoundError:
        print("Oh no! This file/filepath does not exist.")
    except pd.errors.ParserError as error:
        print(f"Could not parse CSV file: {error}")

# Uncomment below to test Q4
# existing_filepath = "data/test_spreadsheet.csv"
# nonexistent_filepath = "data1/test_spreadsheet.csv"
# q4_test_filepath_exists = read_csv(existing_filepath)
# q4_test_filepath_doesnt_exist = read_csv(nonexistent_filepath)     


# # 5) Squash some bugs! 
# # Find the possible logical errors (bugs) 
# # in the code blocks below. Comment in each of them
# # which logical errors did you find and correct them

# Since the instruction asks to correct the errors, I have added the corrected bit of code below my comments below.
# I then printed the final result below the code so we have something to look at.

# ### (a)
# total_double_sum = 0
# for elem in [10, 5, 2]:
#     double = elem * 2
#     total_double_sum += elem

# Here we are not using the double variable which we defined in the center of the funciton. In the end, we are taking the sum
# of the list [10, 5, 2] which would be 17. We should instead replace the elem in the right operand with double. You could also
# simply take lst = [10, 5, 2], then 2*sum(lst) is our double sum.

total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += double
print(total_double_sum)


# ### (b)
# strings = ''
# for string in ['I', 'am', 'Groot']:
#     strings = string+"_"+string

# Here we would set strings to "I_I", then overwriting this and then defining strings as "am_am", then once again overwriting
# strings and setting it to "Groot_Groot". It is implied that the function is meant not to overwrite previous code as that would
# be redundant. You might instead want to create the string "I_I_am_am_Groot_Groot" (just my guess), which you could do by adding
# a "+" to the code, so we set strings += string + "_" + string + "_", then returning strings[:-1] to cut off the last str "_".

strings = ''
for string in ['I', 'am', 'Groot']:
    strings += string + "_" + string + "_"
# Again I reiterate we slice the last character "_" of the string, which
# would print "I_I_am_am_Groot_Groot" (I believe is what the intended output)
print(strings[:-1])


# ### (c) Careful!
# j=10
# while j > 0:
#    j += 1

# This is a classical indexing error. Since j = 10 is already greater than 0 we will run through this while loop infinitely.
# This is because j > 0 will always evaluate as true, and since it will only terminate when j <= 0. We should instead set the
# loop update expression to j -= 1, allowing the loop to run 10 times.

j = 10
count = 0
while j > 0:
    count += 1
    j -= 1
# This would print 10
print(count)


# ### (d)
# productory = 0
# for elem in [1, 5, 25]:
#     productory *= elem

# productory would stay 0, since anything multiplied by 0 is 0. We should instead define productory as 1 the multiplicative identity
# over F (e.g. field F = N the field of natural numbers).

productory = 1
for elem in [1, 5, 25]:
    productory *= elem
# This would print the product of 1, 5, and 25, which is 125:
print(productory)
