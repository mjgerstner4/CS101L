########################################################################
##
## CS 101 Lab
## Matthew Gerstner
## mjgg5g@mail.umkc.edu
##
## PROBLEM :
## The Linda Hall library is in need of a new library card numbering system
## for students, so I must come up with a system containg the first five
## characters of the student's name, along with a value for their school,
## followed by their grade level and lastly finished with two charcters (0-9)
## with the last value being a check digit for previous values.
##
########################################################################

import string

def character_value(char : str) -> int:
    ''' Returns 0 for A, 1 for B, etc. '''
    value = ord(char)
    if (value >= 48 and value<=57):
        return value - 48
    elif (value >= 65 and value<=90):
        return value - 65

def get_check_digit(idnumber : str) -> int:
    ''' Returns the check digit for the name and sid. '''
    sum = 0
    for i in range(len(card_num)):
        value = character_value(card_num[i])
        sum += value * (i+1)
    return sum % 10
    
def verify_check_digit(idnumber : str) -> tuple:
    ''' returns True if the check digit is valid, False if not '''
    if len(card_num) != 10:
        return (False,"The length of the number given must be 10")
    #check first five characters
    for i in range(5):
        if card_num[i] < 'A' or card_num[i] > 'Z':
            msg = "The first 5 characters must be A-Z, the invalid character is at index " \
            + str(i) +" is " + card_num[i]
            return (False, msg)
    #check charactersn at index 7-9
    for i in range(7,10):
        if card_num[i] < '0' or card_num[i] > '9':
            msg = "The last 3 characters must be 0-9, the invalid character is at index "\
                    + str(i) +" is " + card_num[i]
            return (False, msg)
    #check character at index 5
    if (card_num[5] != '1' and card_num[5] != '2' and card_num[5] != '3'):
            return (False, "The sixth character must be 1,2 or 3")
    #check character at index 6
    if (card_num[6] != '1' and card_num[6] != '2' \
        and card_num[6] != '3' and card_num[6] != '4'):
            return (False, "The seventh character must be 1,2,3 or 4")
    
    calculated_value = get_check_digit(card_num)
    given_value = int(card_num[9])
    
    if given_value != calculated_value:
        msg = "Check digit " + str(given_value) + " does not match calculated value " \
               + str(calculated_value)
        return (False,msg)
        
    return (True,"Library card is valid.")

def get_school(idnumber : str) -> str:
    ''' Returns the school the 5th index or 6th character is for. '''
    if card_num[5] == '1':
        return "School of Computing and Engineering SCE"
    elif card_num[5] == '2':
        return "School of Law"
    elif card_num[5] == '3':
        return "College of Arts and Sciences"
    else:
        return "Invalid School"

def get_grade(idnumber : str) -> str:
    '''Returns the grade for index 6'''
    if card_num[6] == '1':
        return "Freshman"
    elif card_num[6] == '2':
        return "Sophomore"
    elif card_num[6] == '3':
        return "Junior"    
    elif card_num[6] == '4':
        return "Senior"
    else:
        return "Invalid Grade"
   
if __name__ == "__main__":

    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("="*60)

    while True:

        print()
        card_num = input("Enter Libary Card.  Hit Enter to Exit ==> ").upper().strip()
        if card_num == "":
            break
        result, error = verify_check_digit(card_num)
        if result == True:
            print("Library card is valid.")
            print("The card belongs to a student in {}".format(get_school(card_num)))
            print("The card belongs to a {}".format(get_grade(card_num)))
        else:
            print("Libary card is invalid.")
            print(error)
        