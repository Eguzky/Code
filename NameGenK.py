"""Create a new file called NameGenerator that has the following.
1.A function that generates a first name from a list of first names.  Have two lists, male names and female names.  
Have the function take the following arguments, sex [looking for either m, f, or None, default as None], firstname [expect a boolean and default as True] 
and lastname [expect a boolean and default as False]

Reminder: def function(argument, argument, argument):

2. The function will return a string of the first and last name, that's it.

3. You can use any number of functions to help the function do it's task.
4. Bonus:  Make a version of this code that instead of returning a string, returns a class called name, which has the properties of first and last."""

import random
from NameLists import male, female, last

def namegen(sex : str = None, firstname : bool = True, lastname : bool = False):
    """Sex expects either 'm' or 'f' as a value"""
    name = personname()

    if firstname:
        name.set_first(random.choice(firstlist(sex)))
    
    if lastname:
        name.set_last(random.choice(last))
    
    return name

def multiname(count, sex : str = None, firstname : bool = True, lastname : bool = False):
    namelist = []
    for x in range(count):
        namelist.append(namegen(sex, firstname, lastname))
    return namelist

def firstlist(sex):
    if sex == "m":
        first_list = male
    elif sex == "f":
        first_list = female
    else:
        first_list = male + female
    
    return first_list


class personname():
    def __init__(self, first = "", last = ""):
        self.first = first
        self.last = last
    
    def set_first(self, first: str):
        self.first = first.capitalize()
    
    def set_last(self, last: str):
        self.last = last.capitalize()
    
    
    def __str__(self):
        if self.first == "" and self.last == "":
            return ""
        elif self.last == "":
            return self.first
        elif self.first == "":
            return self.last
        else:
            return self.first + " " + self.last