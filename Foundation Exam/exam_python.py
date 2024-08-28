from itertools import combinations


"""
HANDSHAKE CHALLENGE

You will need to:
- Write a function that takes an integer for the number of people and returns an integer with the number of handshakes
- Validate if a handshake can occur given X as an input
- Identify an error state and throw a custom exception
- Create a test file for the function and create a comprehensive test suite

"""

"""
itertools is a Python in-built module used for the creation of iterators which helps us looping in a time-space efficient manner. Reading the python official documentation, I have found the combinations method which seemed to be perfect for the coding challenge. It is defined as a combinatoric generator and takes a list and an r number (n of elements of each combination, which in this case is two as we need two people for one handshake) and a and prints all possible combinations 
"""
def no_of_handshakes(no_people):
    # Creating a list of people
    try:
        people = [x for x in range(no_people)]

        #using the combinations method, which will return tuples of all possible combinations. From that, I have created a list so that I can count its length and return it
        handshakes = list(combinations(people, 2))

        return len(handshakes)

    except TypeError:
        print("TypeError: please check that you have called the function passing an integer as argument")


print(no_of_handshakes('hh'))