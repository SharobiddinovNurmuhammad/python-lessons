# CamelCase variable names

firstName = 'Javohir'
lastName = "To'xtasinov"
age = 20
isEmployed = True

# Underscore variable names

first_name = 'Fayzullo'
last_name = 'Turobxonov'
age = 20
is_employed = True

# CamelCase function names

def calculateAreaOfCircle(radius):
    pi = 3.1415
    area = pi * radius ** 2
    return area

# Underscore function names

def calculate_area_circle(radius):
    pi = 3.1415
    area = pi * radius ** 2
    return area

# https://github.com/tvmaly/clean-code-python

def  calc_sum(numbers):

    total_sum = 0
    
    for number in numbers:
        total_sum += number

    return total_sum
