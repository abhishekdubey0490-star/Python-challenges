"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
#Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

#Define the 'preparation_time_in_minutes()' function below.
def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the preparation time based on the number of layers.

    :param number_of_layers: int - the number of layers of lasagna.
    :return: int - total preparation time (in minutes).
    """
    return number_of_layers * PREPARATION_TIME
    
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.



#define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """
    Calculate the total elapsed time spent preparing and baking.

    :param number_of_layers: int - number of layers prepared.
    :param elapsed_bake_time: int - time the lasagna has been baking.
    :return: int - total elapsed time (in minutes).
    """
    return preparation_time_in_minutes(number_of_layers)+elapsed_bake_time


# Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
