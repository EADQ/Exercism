"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# TODO: define the 'EXPECTED_BAKE_TIME' constant
EXPECTED_BAKE_TIME= 40
# TODO: consider defining the 'PREPARATION_TIME' constant
PREPARATION_TIME= 2
#       equal to the time it takes to prepare a single layer

# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time): 
    """elapsed_bake_time 

    :param: int - elapsed_bake_time
    :return: int - EXPECTED_BAKE_TIME - int -elapsed_bake_time

    This function with a single param evaluate the elapsed_bake_time, giving the time remaining
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time 

# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(number_of_layers):
    """"preparation_time_in_minutes

    :param: int - number_of_layers
    :return: int - number_of_layers * PREPARATION_TIME all this time in minutes

    This function calculates the preparation_time_in_minutes, when the number_of_layers mult with the PREPARATION_TIME
    """"

    return number_of_layers * PREPARATION_TIME

# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """"elapsed_time_in_minutes

    :param: int - number_of_layers 
    :param: int - elapsed_time_in_minutes

    This function evaluates the number_of_layers and the elapsed_time_in_minutes and plus both on retur
    """"

    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)
