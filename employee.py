# kam180013 portfolio1 professor mazidi 4395
# use data.csv file to santize the employee data

# parentheses after class declaration only required if they
# need to be declared with arguments


import sys
import pathlib
import re
import pickle
'''
person class: last, first, mi, id, phone, init(), display()
'''
class Person():
    def __init__(self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone

    def display(self):
        print(f"\nEmployee ID: {self.id}")
        print(f"\t{self.first} {self.mi} {self.last}")
        print(f"\t{self.phone}")

'''
to do: 
[x]open file, get rid of first line, for each line ->

process_lines()
[X]split on comma (fields as strings)
[X]names in capital case
[X]mi as single uppercase (or X if none)
[X]id mdded with regex (2 letters, 4 digits) -> error then user input
phone # in form 999-999-9999 with regex

[X]display function

[X]save person object with correct data and save object to
    dict of persons {id:person obj} -> check for duplicate id -> error mssg
[X]return dict to main function

[x]save dict in main as pickle file
[x]open pickle for read and print with display()

UPLOAD TO GITHUB PORTFOLIO (WITH OVERVIEW FROM DELIVERABLES)
'''

def process_lines(lines):
    # create empty dictionary
    employees = {}

    #print("processing lines now")

    for line in lines:

        # regex and such

        # split on comma (last, first, mi, id, phone) -> 0-4 index
        info = re.split(",", line)

        # capital case for names ################################################
        l = info[0]
        f = info[1]
        
        #print(l)
        #print(f)

        # LAST NAME #############################################################
        l = l.capitalize()
        #print(l)
        info[0] = l

        # FIRST NAME ############################################################
        f = f.capitalize()
        #print(f)
        info[1] = f

        # mi is single uppercase (if none, put x) ##############################
        mi = info[2]
        #print(mi)

        if(len(mi) == 0):
            mi = "X"
        mi = mi[0]
        #print(mi)

        match = re.search(r'[A-Za-z]', mi)

        while not match:
            print(f"Middle initial should be one capital letter. {mi} is not correct.")
            mi = input("Please enter the correct middle initial: ")
            match = re.search(r'[A-Za-z]', mi)
            mi = match.group()
            #print(mi)

        mi = mi.capitalize()
        #print(mi)
        info[2] = mi

        # id (2 letters, 4 digits) otherwise error mssg ########################

        id = info[3]
        #print(id)

        match = re.search(r'[A-Z]{2}[0-9]{4}|[a-z]{2}[0-9]{4}', id)

        while not match:
            print(f"ID is two letters followed by 4 digits. {id} is the incorrect format.")
            id = input("Please enter the correct id number: ")
            match = re.search(r'[A-Z]{2}[0-9]{4}|[a-z]{2}[0-9]{4}', id)
            id = match.group()
            #print(id)

        id = id.upper()
        #print(id)

        info[3] = id

        # phone number in 999-999-9999 #########################################
        
        phone = info[4]
        #print(phone)

        match = re.findall(r'[0-9]', phone)
        phone = "".join(match)

        while len(phone) != 10:
            print(f"Phone number should be 10 digits. {phone} is not correct.")
            phone = input("Please enter the correct phone number: ")
            match = re.findall(r'[0-9]', phone)
            phone = "".join(match)
            #print(phone)

        phone = phone[:3] + "-" + phone[3:6] + "-" + phone[6:]
        #print(phone)

        info[4] = phone

        # save each person to dict (id is key) -> {id key, person obj} ########
        person = Person(*info)

        key = info[3]

        # check for dupes
        if key not in employees:
            employees[key] = person
        else:
            print(f"Duplicate ID {key} detected. {info[0]}, {info[1]} information not entered.")
    
    return employees


'''
main function kicks things off
'''

def main(filename):
    # manages execution of code with a "context manager" (in this case -> "open")
    # with statement also properly closes the file (even with an exception occurring)
    # code within the with statement executes with the file object as its context
    #with open(filename, "data.csv") as file:
    #    contents = file.read.splitlines()
    
    with open(pathlib.Path.cwd().joinpath(filename), 'r') as f:
        text_in = f.read().splitlines()
    
    # parse data
    employees = process_lines(text_in[1:]) #ignores heading line

    # pickle the employees (dict)
    pickle.dump(employees, open('employees.pickle', 'wb'))

    # read the pickle back in
    employees_in = pickle.load(open('employees.pickle', 'rb'))

    # output employees
    print("\n\nEmployee list:")

    for emp_id in employees_in.keys():
        employees_in[emp_id].display()

    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 employee.py filenamepath")
        quit()
        #sys.exit(1)
    #rel_path = sys.argv[1]


    # * is used to unpack the elements of a list (or any iterable) into
    # separate positional arguments

    main(*sys.argv[1:2])
