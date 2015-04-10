'''
Created on Apr 3, 2015

@author: Jordi
'''

# Ask user what to do
def main():
    print("===Credit Card Validation===")
    print("1. Validate Number")
    print("2. Exit Program")
    print("============================")
    menuoption = int(input("Menu Choice: "))
    handle_menu_loop(menuoption)
   
def handle_menu_loop( menuoption ):
    if menuoption == 1:
        ccnum = input("Please Enter Credit Card Number: ")
        print("Card Number: ",ccnum)
        if number_len(ccnum):
            total1 = double_even_numbers(ccnum)
            total2 = add_odd_numbers(ccnum)
            if validate_card_number(total1, total2):
                card_type(ccnum)
                print("Card Number is Valid!")
                print("                     ")
                main()
            else:
                print("Card Number is Invalid!")
                print("                       ")
                main()
    elif menuoption == 2:
        exit
    else:
        print("Please Choose 1 or 2")
        main()
    
# Validate length of CC num  
def number_len ( ccnum ):
    if len(ccnum) >= 13 and len(ccnum) <= 16:
        return True
    else:
        print("Invalid Number Length")
        main()
        return False

def card_type( ccnum ):
    if int(ccnum[0]) == 4:
        print("Card Type: Visa")
    elif int(ccnum[0]) == 5:
        print("Card Type: Mastercard")
    elif int(ccnum[0]) == 6:
        print("Card Type: Discover")
    elif int(ccnum[0]) == 3 and int(ccnum[0]) == 7 :
        print("Card Type: American Express")
    else:
        print("Card Type: Unknown")
    
# Add and double even numbers
def double_even_numbers ( ccnum ):
    i = 1
    j = 0
    for c in reversed( ccnum ):
        if i % 2 == 0:
            if int(c) * 2 > 9:
                k = ((int(c) * 2) % 10) + 1
                j = j + k
            elif int(c) * 2 <= 9:
                j = j + (int(c) * 2)
        i = i + 1
    return j
    
def add_odd_numbers ( ccnum ):
    i = 1
    j = 0
    for c in reversed( ccnum ):
        if i % 2 != 0:
            j = j + int(c)
        i = i + 1
    return j

def validate_card_number ( total1 , total2 ):
    if (total1 + total2) % 10 == 0:
        return True
    else: 
        return False

# Run
if __name__ == '__main__':
    main()


