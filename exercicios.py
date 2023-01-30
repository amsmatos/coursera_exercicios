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

def exercicio2(): #<-- ATENÇÃO: criei esta função somente para não executar o código no meu ficheiro enquanto testo o código. Aresposta é sem esta linha.
    cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
    for keys, values in cool_beasts.items():
        print("{} have {}".format(keys, values))

'''

# The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. 
# Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).


def email_list(domains):
	emails = []
	for ___:
	  for user in users:
	    emails.___
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

'''

# Minha resposta

def email_list(domains):
    emails = []
    for domain, users in domains.items():
        for user in users:
            emails.append("{}@{}".format(user, domain))
            #print(user, domain)
    return(emails)

'''

# The groups_per_user function receives a dictionary, which contains group names with the list of users.
# Users can belong to multiple groups. 
# Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 


def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for ___:
		# Now go through the users in the group
		for ___:
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

'''

# Minha resposta

def groups_per_user(group_dictionary):
    user_groups = {}
	# Go through group_dictionary
    for groups, users in group_dictionary.items():
		# Now go through the users in the group
        #if groups in group_dictionary.keys():
        for user in users:
			# Now add the group to the the list of
            # groups for this user, creating the entry
            # in the dictionary if necessary
           
            if user in user_groups.keys():
                user_groups[user] += [groups]
            else:
                user_groups[user] = [groups]

    return(user_groups)



'''

# The add_prices function returns the total price of all of the groceries in the  dictionary. 
# Fill in the blanks to complete this function.

def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for ___:
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += ___
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44

'''

# Minha resposta

def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for prod in basket.values():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += prod
	# Limit the return value to 2 decimal places
	return round(total, 2)  

'''

# The format of the input variable “address_string” is: numeric house number, followed by the street name which may contain numbers and could be several words long (e.g., "123 Main Street", "1001 1st Ave", or "55 North Center Drive").
# Complete the string methods needed in this function so that input like "123 Main Street" will produce the output "House number 123 on a street named Main Street". 
# This function should:
# - accept a string through the parameters of the function;
# - separate the address string into new strings: house_number and street_name;
# - return the variables in the string format: "House number X on a street named Y". 

def format_address(address_string):


    house_number = ""
    street_name = ""


    # Separate the house number from the street name.
    address_parts = ___
    
    for address_part in address_parts:
       # Complete the if-statement with a string method.  
       if ___
         house_number = address_part
       else:
         street_name += address_part + " "
    # Remove the extra space at the end of the last "street_name".
    street_name = ___
 
    # Use a string method to return the required formatted string.
    return ___


print(format_address("123 Main Street"))
# Should print: "House number 123 on a street named Main Street"


print(format_address("1001 1st Ave"))
# Should print: "House number 1001 on a street named 1st Ave"


print(format_address("55 North Center Drive"))
# Should print "House number 55 on a street named North Center Drive"


'''

# Minha resposta

def format_address(address_string):


    house_number = ""
    street_name = ""


    # Separate the house number from the street name.
    address_parts = address_string.split()
    i = 0
    for address_part in address_parts:
        # Complete the if-statement with a string method.
        if address_parts[i].isnumeric():
            house_number = address_part
        else:
            street_name += address_part + " "
        i += 1
    # Remove the extra space at the end of the last "street_name".
    street_name = street_name.rstrip()
 
    # Use a string method to return the required formatted string.
    return "House number {} on a street named {}".format(house_number, street_name)

'''
# Complete the for loop and string method needed in this function so that a function call like "alpha_length("This has 1 number in it")" will return the output "17". 
# This function should:
# - accept a string through the parameters of the function;
# - iterate over the characters in the string;
# - determine if each character is a letter (counting only alphabetic characters; numbers, punctuation, and spaces should be ignored);
# - increment the counter;
# - return the count of letters in the string.


def alpha_length(string):
    character = ""
    count_alpha = 0
    # Complete the for loop sequence to iterate over "string".
    for ___: 
        # Complete the if-statement using a string method. 
        if ___:
            count_alpha += 1  
    return count_alpha
 
print(alpha_length("This has 1 number in it")) # Should print 17
print(alpha_length("Thisisallletters")) # Should print 16
print(alpha_length("This one has punctuation!")) # Should print 21

'''

# Minha resposta


def alpha_length(string):
    character = ""
    count_alpha = 0
    # Complete the for loop sequence to iterate over "string".
    for character in string:
        # Complete the if-statement using a string method. 
        if character.isalpha():
            count_alpha += 1
    return count_alpha

'''

# Consider the following scenario about using Python lists:
# Employees at a company shared  the distance they drive to work (in miles) through an online survey.
# These distances were automatically added by Python to a list called “distances” in the order that each employee submitted their distance.
# Management wants the list to be sorted in the order of the longest distance to the shortest distance.
# Complete the function to sort the “distances” list. This function should:
# - sort the given “distances” list, passed through the function’s parameters;
# - reverse the sort order so that it goes from the longest to the shortest distance;
# - return the modified “distances” list.

def sort_distance(distances):
    ___ # Sort the list
    ___ # Reverse the order of the list
    return distances


print(sort_distance([2,4,0,15,8,9]))
# Should print [15, 9, 8, 4, 2, 0]

'''

# Minha resposta


def sort_distance(distances):
    distances.sort() # Sort the list
    distances.sort(reverse = True) # Reverse the order of the list
    return distances

'''

# Fill in the blank to complete the “increments” function.
# This function should use a list comprehension to create a list of numbers incremented by 2 (n+2).
# The function receives two variables and should return a list of incremented consecutive numbers between “start” and “end” inclusively (meaning the range should include both the “start” and “end” values).
# Complete the list comprehension in this function so that input like “squares(2, 3)” will produce the output “[4, 5]”.


def increments(start, end):
    return [ ___ ] # Create the required list comprehension.


print(increments(2, 3)) # Should print [4, 5]
print(increments(1, 5)) # Should print [3, 4, 5, 6, 7]
print(increments(0, 10)) # Should print [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

'''

# Minha resposta

def increments(start, end):
    return [ x+2 for x in range(start, end+1) ] # Create the required list comprehension.


'''

# Fill in the blanks to complete the “endangered_animals” function.
# This function accepts a dictionary containing a list of endangered animals (keys) and their remaining population (values).
# For each key in the given “animal_dict” dictionary, format a string to print the name of the animal, with one animal name per line.


def endangered_animals(animal_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.    
    for ___ 
        # Use a string method to format the required string.
        result += ___ 
    return result


print(endangered_animals({"Javan Rhinoceros":60, "Vaquita":10, "Mountain Gorilla":200, "Tiger":500}))

# Should print:
# Javan Rhinoceros
# Vaquita
# Mountain Gorilla
# Tiger

'''

# Minha resposta

def endangered_animals(animal_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.    
    for name in animal_dict.keys(): 
        # Use a string method to format the required string.
        result += str(name) + '\n'
    return result


'''

# Consider the following scenario about using Python dictionaries and lists:
# Tessa and Rick are hosting a party. 
# Before they send out invitations, they want to add all of the people they are inviting to a dictionary so they can also add how many guests each friend is bringing to the party.
# Complete the function so that it accepts a list of people, then iterates over the list and adds all of the names (elements) to the dictionary as keys with a starting value of 0.
# Tessa and Rick plan to update these values with the number of guests their friends will bring with them to the party. Then, print the new dictionary.
# This function should:
# - accept a list variable named “guest_list” through the function’s parameter;
# - add the contents of the list as keys to a new, blank dictionary;
# - assign each new key with the value 0;
# - print the new dictionary.


def setup_guests(guest_list):
    # loop over the guest list and add each guest to the dictionary with
    # an initial value of 0
    result = ___ # Initialize a new dictionary 
    for ___ # Iterate over the elements in the list 
        ___ # Add each list element to the dictionary as a key with 
            # the starting value of 0
    return result

guests = ["Adam","Camila","David","Jamal","Charley","Titus","Raj","Noemi","Sakira","Chidi"]

print(setup_guests(guests))
# Should print {'Adam': 0, 'Camila': 0, 'David': 0, 'Jamal': 0, 'Charley': 0, 'Titus': 0, 'Raj': 0, 'Noemi': 0, 'Sakira': 0, 'Chidi': 0}

'''

# Minha resposta


def setup_guests(guest_list):
    # loop over the guest list and add each guest to the dictionary with
    # an initial value of 0
    result = {} # Initialize a new dictionary 
    for name in guests: # Iterate over the elements in the list 
        result[name] = 0 # Add each list element to the dictionary as a key with 
            # the starting value of 0
    return result

guests = ["Adam","Camila","David","Jamal","Charley","Titus","Raj","Noemi","Sakira","Chidi"]


'''

# Consider the following scenario about using Python dictionaries:
# A teacher is using a dictionary to store student grades. The grades are stored as a point value out of 100.
# Currently, the teacher has a dictionary setup for Term 1 grades and wants to duplicate it for Term 2. 
# The student name keys in the dictionary should stay the same, but the grade values should be reset to 0.

# Complete the “setup_gradebook” function so that input like “{"James": 93, "Felicity": 98, "Barakaa": 80}” will
# produce a resulting dictionary that contains  “{"James": 0, "Felicity": 0, "Barakaa": 0}”. This function should: 
# - accept a dictionary “old_gradebook” variable through the function’s parameters;
# - make a copy of the “old_gradebook” dictionary;
# - iterate over each key and value pair in the new dictionary;
# - replace the value for each key with the number 0;
# - return the new dictionary.


def setup_gradebook(old_gradebook):
  # Use a dictionary method to create a new copy of the "old_gradebook".
  ___ 
    # Complete the for loop to iterate over the new gradebook. 
    for ___
        # Use a dictionary operation to reset the grade values to 0.
        ___
    return new_gradebook

fall_gradebook = {"James": 93, "Felicity": 98, "Barakaa": 80}
print(setup_gradebook(fall_gradebook))
# Should output {'James': 0, 'Felicity': 0, 'Barakaa': 0}


'''

# Minha resposta

def setup_gradebook(old_gradebook):
  # Use a dictionary method to create a new copy of the "old_gradebook".
    new_gradebook =  old_gradebook.copy()
    # Complete the for loop to iterate over the new gradebook. 
    for name in new_gradebook.keys():
        # Use a dictionary operation to reset the grade values to 0.
        new_gradebook[name] = 0
    return new_gradebook


'''
# Want to give this a go? Fill in the blanks in the code to make it print a poem.

class ___:
  color = 'unknown'

rose = Flower()
rose.color = ___

violet = ___
___

this_pun_is_for_you = ___

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you) 

'''

# Minha resposta

class Flower:
    color = 'unknown'

rose = Flower()
rose.color = "red"

violet = Flower()
violet.color = "blue"

this_pun_is_for_you = "This pun is for you"

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you) 

'''

# Creating new instances of class objects can be a great way to keep track of values using attributes associated with the object.
# The values of these attributes can be easily changed at the object level. 
# The following code illustrates a famous quote by George Bernard Shaw, using objects to represent people.
# Fill in the blanks to make the code satisfy the behavior described in the quote. 

# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw


# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
#Here, despite G.B. Shaw's quote, our characters have started with       #different amounts of apples so we can better observe the results. 
#We're going to have Martin and Johanna exchange ALL their apples with #one another.
#Hint: how would you switch values of variables, 
#so that "you" and "me" will exchange ALL their apples with one another?
#Do you need a temporary variable to store one of the values?
#You may need more than one line of code to do that, which is OK. 
    	___
    	return you.apples, me.apples
    
def exchange_ideas(you, me):
    #"you" and "me" will share our ideas with one another.
    #What operations need to be performed, so that each object receives
    #the shared number of ideas?
    #Hint: how would you assign the total number of ideas to 
    #each idea attribute? Do you need a temporary variable to store 
    #the sum of ideas, or can you find another way? 
    #Use as many lines of code as you need here.
    you.ideas ___
    me.ideas ___
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))



'''

# Minha resposta


# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
#Here, despite G.B. Shaw's quote, our characters have started with       #different amounts of apples so we can better observe the results. 
#We're going to have Martin and Johanna exchange ALL their apples with #one another.
#Hint: how would you switch values of variables, 
#so that "you" and "me" will exchange ALL their apples with one another?
#Do you need a temporary variable to store one of the values?
#You may need more than one line of code to do that, which is OK. 
    temp = you.apples
    you.apples = me.apples
    me.apples = temp
    return you.apples, me.apples
    
def exchange_ideas(you, me):
    #"you" and "me" will share our ideas with one another.
    #What operations need to be performed, so that each object receives
    #the shared number of ideas?
    #Hint: how would you assign the total number of ideas to 
    #each idea attribute? Do you need a temporary variable to store 
    #the sum of ideas, or can you find another way? 
    #Use as many lines of code as you need here.
    temp2 = you.ideas
    you.ideas = me.ideas + temp2
    me.ideas = temp2 + me.ideas
    return you.ideas, me.ideas



'''

Pergunta 3
# The City class has the following attributes: name, country (where the city is located), elevation (measured in meters), and population (approximate, according to recent statistics).
# Fill in the blanks of the max_elevation_city function to return the name of the city and its country (separated by a comma), when comparing the 3 defined instances for a specified minimal population.
# For example, calling the function for a minimum population of 1 million: max_elevation_city(1000000) should return "Sofia, Bulgaria". 


# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	# Initialize the variable that will hold 
# the information of the city with 
# the highest elevation 
	return_city = City()

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if ___
		return_city = ___
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	if ___
		return_city = ___
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
	if ___
		return_city = ___

	#Format the return string
	if return_city.name:
		return ___
	else:
		return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""


'''


# Minha resposta


# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	# Initialize the variable that will hold 
# the information of the city with 
# the highest elevation 
	return_city = City()
	return_city.population = min_population

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if return_city.population < city2.population:
		return_city.name = city1.name 
		return_city.country = city1.country
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	if return_city.population > city1.population and return_city.population < city3.population:
		return_city.name = city2.name
		return_city.country = city2.country
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
	if return_city.population > city3.population:
		return_city.name = "" 
		return_city.country = ""

	#Format the return string
	if return_city.name:
		return return_city.name + ", " + return_city.country
	else:
		return ""




'''

# We have two pieces of furniture: a brown wood table and a red leather couch. Fill in the blanks following the creation of each Furniture class instance, 
# so that the describe_furniture function can format a sentence that describes these pieces as follows: "This piece of furniture is made of {color} {material}"

class Furniture:
	color = ""
	material = ""

table = Furniture()
___
___

couch = Furniture()
___
___

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table)) 
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch)) 
# Should be "This piece of furniture is made of red leather"

'''

# Minha resposta


class Furniture:
	color = ""
	material = ""

table = Furniture()
table.color = "brown"
table.material = "wood" 

couch = Furniture()
couch. color = "red"
couch.material = "leather"

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table)) 
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch)) 
# Should be "This piece of furniture is made of red leather"

