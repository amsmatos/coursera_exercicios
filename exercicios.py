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






'''
# This exercise will walk you through how to write a list comprehension to create a list of squared numbers (n*n).
# It needs to return a list of squares of consecutive numbers between “start” and “end” inclusively.
# For example, squares(2, 3) should return a list containing [4, 9].

def squares(start, end):
    return ___ 


print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

'''

# Minha resposta

def squares(start, end):
    return ([x*x for x in range(start,end+1)]) 





'''
# Given a list of filenames, we want to rename all the files with extension hpp to the extension h. 
# To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. 
# Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
___  

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

'''

# Minha resposta

def exercicio1(): #<-- ATENÇÃO: criei esta função somente para não executar o código no meu ficheiro enquanto testo o código. Aresposta é sem esta linha.
    filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
    newfilenames = []
    for names in filenames:
        if names.endswith(".hpp"):
            names = names.replace(".hpp", ".h")
        newfilenames.append(names)


    print(newfilenames)






'''
# Let's create a function that turns text into pig latin: a simple text transformation that 
# modifies each word moving the first character to the end and appending "ay" to the end. 
# For example, python ends up as ythonpay.



def pig_latin(text):
  say = ""
  # Separate the text into words
  words = ___
  for word in words:
    # Create the pig latin word and add it to the list
    ___
    # Turn the list back into a phrase
  return ___
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

'''

# Minha resposta

def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    word = word[1:] + word[:1] + "ay "
    say = say + word
    # Turn the list back into a phrase
  return say.strip()

'''
# The permissions of a file in a Linux system are split into three sets of three permissions: 
# read, write, and execute for the owner, group, and others. 
# Each of the three values can be expressed as an octal number summing each permission, 
# with 4 corresponding to read, 2 to write, and 1 to execute. 
# Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
# For example: 
# 640 is read/write for the owner, read for the group, and no permissions for the others; 
# converted to a string, it would be: "rw-r-----"
# 755 is read/write/execute for the owner, and read/execute for group and others; 
# converted to a string, it would be: "rwxr-xr-x"
# Fill in the blanks to make the code convert a permission in octal format into a string format.






def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for ___ in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if ___ >= value:
                result += ___
                ___ -= value
            else:
                ___
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------

'''

# Minha resposta

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for i in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if i >= value:
                result += letter
                i -= value
            else:
                result += "-"
    return result

'''

# The group_list function accepts a group name and a list of members,
# and returns a string with the format: group_name: member1, member2, … 
# For example, group_list("g", ["a","b","c"]) 
# returns "g: a, b, c". Fill in the gaps in this function to do that.






def group_list(group, users):
  members = ___
  return ___

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"
'''


# Minha resposta

def group_list(group, users):
    members = ", ".join(users)
    return group + ": " + members

'''
# The guest_list function reads in a list of tuples with the name, age, and profession of each party guest, 
# and prints the sentence "Guest is X years old and works as __." for each one. 
# For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")) 
# should print out: Ken is 30 years old and works as Chef. 
# Pat is 35 years old and works as Lawyer. 
# Amanda is 25 years old and works as Engineer.

# Fill in the gaps in this function to do that. 





def guest_list(guests):
	for ___:
		___
		print(___.format(___))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""

'''

# Minha resposta

def guest_list(guests):
	for name, age, job in guests:
		print("{} is {} years old and works as {}".format(name, age, job))


'''

# Complete the code to iterate through the keys and values of the cool_beasts dictionary.
# Remember that the items method returns a tuple of key, value for each element in the dictionary.


cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for ___ in cool_beasts.items():
    print("{} have {}".format(___))

'''

# Minha resposta

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for keys, values in cool_beasts.items():
    print("{} have {}".format(keys, values))

'''

'''