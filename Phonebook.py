# Assignment Phone book 
# Phonebook
# create a phonebook - Repo/ file - commit / main - branch 
# sub prob - list 
# how user input on comamand line? 


# GIT LIST MENU BRANCH 
Menu = """ Electronic Phone book
# print (*"1. Look up an entry")
# print (*"2. Set an entry")
# print (*"3. Delete an entry")
# print (*"4. List all entries")
# print (*"5. Quit What do you want to do (1-5)? 
 """

 #git commit - m " add menu" push - upstream - branch 2 - compare and pull/approve - merge into main - comments /
 #git checkout - 
 #git pull to merge to local 

def print_menu():
    print (*"1. Look up an entry") 
    print (*"2. Set an entry" )
    print (*"3. Delete an entry")
    print (*"4. List all entries")
    print (*"5. Quit What do you want to do (1-5)?")
    
# Git checkout Branch - new "user input" - ticket 
# selected user = input "what option would you like 1-5?"


# def phonebook (name,number): 
# print ("name, number")
# name = ("Melissa", "Igor", "Jazz")
# number =  ("857-485-2935", "1-857-2935", "334-584-2345")
# if name == " Melissa ":
#    print (number)
#    phonebook ("Igor")
#    phonebook ("Jazz")

# User 
# Dictionary :  
# {"name": "Melissa", "Igor", "Jazz"
# "number" : "857-485-2935", "1-857-2935", "334-584-2345"
# } if == 

# Git branch - git add . git checkout - New Branch - Contract entry 

# below from Stackoverflow 

numbers = {}
menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input("Type in a number (1-5): "))
    if menu_choice == 1:
        print("Telephone Numbers:")
        for x in numbers.keys():
            print("Name: ", x, "\tNumber:", numbers[x])
        print()
    elif menu_choice == 2:
        print("Add Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        numbers[name] = phone
    elif menu_choice == 3:
        print("Remove Name and Number")
        name = input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "was not found")
    elif menu_choice == 4:
        print("Lookup Number")
        name = input("Name: ")
        if name in numbers:
            print("The number is", numbers[name])
        else:
            print(name, "was not found")
    elif menu_choice != 5:
        print_menu()

# TROY's code 2/22   functions? while not(has quit) & print menu 
# if selected_ option == "2"
#    name = input (What is the contact's name?")
#    phone_number = input ("what is their phone number?")
#   phonebook (name) = phone number 
#    print ("Contact added successfully!" )
#    print (menu)

#    # Git add . - git commit -m "comment" - git push - compare & pull merge etc - pull  Able to see changes 
#    # main local and pull to update 
#   # new branch - 

#elif selected_option == "1"
#    name = input ("What contact's number would you like?")
#    if phonebook.get(name) == None: 
#    print("There's no contact with that name... please try again.")
#   else: 
#        print("Here's their number:", phonebook[name])
#  elif selcted_option == "5":
    # hasQuit = True 


# Notes - dictionary - key/ name - index 

# function 
# if (): 
#     print(name,number"")

# Save - not on auto save     

# Run 
# Create Repo - c/p 
# push py

# Notes: that numbers is equal to {} - this signifies that it is a "Dictionary", which stores key/value pairs. To add to a dictionary (or "dict"), you can modify it manually as such: numbers = {'David': 18003574689}. So, in order to access David's phone number, you would type in numbers['David'].
# Another way to add to it is by instantiating it (which is already done for you via numbers = {}), and then adding information into to it via the shortcut formula dictname['key'] = value. So in this case, the shorthand can be numbers['Laura'] = 9173162546.
# Now, to add a list into the mix, you could use [] (which is a list in python), but you would probably be better suited nesting another dict into the current one. For example, instead of numbers = {'David': 18003574689}, you can now have numbers = {'David': {'phone number': 18003574689, 'e-mail': 'david2015@gmail.com', 'address web page': 'http://dave.com'}, 'Laura': [...etc...]}.
# To access these new nested dicts, what you can do is the shorthand numbers['David']['phone number'], which will return his #. You can then do this exact shortcode 2 more times numbers['David']['e-mail'] & numbers['David']['address web page']. These three will access the associated data.
