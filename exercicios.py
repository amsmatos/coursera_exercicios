''' Exercício :

# Try out the enumerate function for yourself in this quick exercise. 
# Complete the skip_elements function to return every other element from the list, 
# this time using the enumerate function to check if an element is in an even position or an odd position.


def skip_elements(elements):
	# code goes here
	
	return ___

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
'''

# Minha resposta

def skip_elements(elements):
    # code goes here
    elements2 = []
    i = 0
    for element in elements:
        if i % 2 == 0:
            elements2.append(element)
        i += 1
    return elements2

''' Exercício:

# The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. 
# Fill in the blanks in the function, using list comprehension. 
# Hint: remember that list and range counters start at 0 and end at the limit minus 1.

def odd_numbers(n):
	return [x for x in ___ if ___]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

'''

# Minha resposta

def odd_numbers(n):
	return [x for x in range(n+1) if x % 2 == 1]