'''
Write a function that takes in a string and returns the number of
unique consonants

EXAMPLE INPUT: “cat”
EXAMPLE OUTPUT: 2 (‘c’ and ‘t’ are both unique)
EXAMPLE INPUT: “cataract”
EXAMPLE OUTPUT: 1 (‘r’ is the only unique consonant)

What is the time and space complexity of your solution?
If you are making any assumptions in your calculations, list them.
'''

def count_unique_consonants(string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    seen = []
    unique = []
    # the above variables will allow us to compare each character of the string and make sure they're not a vowel and they're unique

    for char in string:
        if char not in vowel and char not in seen:
            seen.append(char)
            unique.append(char)
        elif char in seen and char in unique: # this will make sure the vowel will be removed from the unique list if seen again
            unique.remove(char)

    return len(unique)

# string1 = 'cat'
# string2 = 'cataract'
#
# print(count_unique_consonants(string1))
# print(count_unique_consonants(string2))
# print(count_unique_consonants('aaaaabcddggldd'))

# Time and space complexity of this solution is O(n) Linear time. The running time of this solution increases with the size of the string input as it needs to iterate through it

'''
Write a function that finds how many squares are in a X by X grid
For example a 2x2 Grid has 5 squares 

HINT:
There seems to be a pattern as X increases.
The number of 2x2 squares is the sum of the squares of 2 and 1.
The number of 3x3 squares is the sum of the squares of 3 and 2 and 1.
'''

def count_squares(x):
    if x == 1:
        return 1
    elif x == 2:
        return x ** 2 + (x - 1) ** 2
    else:
        return x ** 2 + count_squares(x-1)

print(count_squares(2))
print(count_squares(3))
print(count_squares(4))