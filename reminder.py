# This file contains all functions related to the reminder aspect of the bot

# Import Modules for database
from array import array
import json
from collections import defaultdict
from datetime import datetime

# Dictionary that stores all assignments
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
        return ("{} is due {}".format(self.name, self.due_date))

# Adds assignment to list
def add_assignment(name, due_date):
    # Create new assignment
    new_asgn = Assignment(name,due_date)

    # Add assignment to dictionary
    asgns.append(new_asgn)

# Prints List of subjects
def list_subjects():
    # Sorts by due date
    asgns.sort(key = lambda date: datetime.strptime(date.due_date,"%m/%d/%Y"))

    for i in asgns:
        yield i.print_asgn()

# Checks if assignment name is present in asgn list, returns either true or false
def is_present(asgn):
    for i in asgns:
        if i.name == asgn:
            return True
    return False

# Deletes Assignment
def del_assignment(name):
    asgn = next(x for x in asgns if x.name == name )
    asgns.remove(asgn)

# Saves data into JSON file
def save_data():
    # Convert array to json string
    json_string = json.dumps(asgns)

    # Open json file and write data
    with open('asgn.json','w') as outfile:
        json.dump(json_string,outfile)



