# This file contains all functions related to the reminder aspect of the bot

# Import Modules for database
from array import array
import json
from collections import defaultdict

# Dictionary that stores all assignments by subject
asgns = defaultdict(list)

# Assignment Object
class Assignment():
    def __init__(self, subject, name, due_date):
        self.subject = subject
        self.name = name
        self.due_date = due_date

    def change_due_date(self,new_date):
        self.due_date = new_date
    
    def change_name(self, new_name):
        self.name = new_name



def add_assignment(subject, name, due_date):
    # Create new assignment
    new_asgn = Assignment(subject,name,due_date)

    # Add assignment to dictionary
    asgns[new_asgn.subject].append(new_asgn)

# Prints List of subjects
def list_subjects():
    for i in asgns:
        print(i)


# Testing Purposes
add_assignment("CSE101", "PA 1", "10/17/1999")
add_assignment("CSE13S", "PA 2", "10/17/1999")
print(asgns)
list_subjects()



