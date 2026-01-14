"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(minutes_in_oven):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    

    time_remaining = EXPECTED_BAKE_TIME - minutes_in_oven
    return time_remaining

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time based on the number of layers

    :param number_of_layers: int - number of layers of lasagna 
    
    """
    total_time = number_of_layers * PREPARATION_TIME
    return total_time

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the time the user have been in the kitchen.

    :param number_of_layers: int - number of layers of lasagna
    :param elapsed_bake_time: int - the number of minutes the lasagna has spent baking        already

    :return: int - total_time_cooking (in minutes) variable that saves the result of the     calculation.

    Function that takes the number of layers of the lasagna and the time elapsed since       the start of the cooking, calculated by multiplying the number of layers and the         PREPARATION_TIME constant plus the number of minutes the lasagna has spend baking        already
    """
    total_time_cooking = (number_of_layers * PREPARATION_TIME) + elapsed_bake_time
    return total_time_cooking

