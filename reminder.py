# This file contains all functions related to the reminder aspect of the bot

# Import Modules for database
from array import array
import json
from collections import defaultdict

# Dictionary that stores all assignments by subject
asgns = []

# Assignment Object
class Assignment():
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date

    def change_due_date(self,new_date):
        self.due_date = new_date
    
    def change_name(self, new_name):
        self.name = new_name
    
    def print_asgn(self):
        print("{} is due {}".format(self.name, self.due_date))



def add_assignment(name, due_date):
    # Create new assignment
    new_asgn = Assignment(name,due_date)

    # Add assignment to dictionary
    asgns.append(new_asgn)

# Prints List of subjects
def list_subjects():
    for i in asgns:
        i.print_asgn()


# Testing Purposes
#add_assignment("CSE101", "PA 1", "10/17/1999")
#add_assignment("CSE13S", "PA 2", "10/17/1999")
#print(asgns)
#list_subjects()



