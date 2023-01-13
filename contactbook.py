#%%

print("\nWelcome to contact book, a book for contacts.")
contacts = {}

def start_here(): #done
    print("\nPlease choose an option below: \n a. Add a Contact \n b. Delete a Contact \n c. Search by Name \n d. Search by Number \n e. Display the Contact Book")
    entry = input("Please choose a letter between a, b, c, d, or e. \n You can also press enter 'q' to quit. ").strip().lower()
    if entry == "a":
        return add_contact()
    if entry == "b":
        return remove_contact()
    if entry == "c":
        return search_contact_by_name()
    if entry == "d":
        return search_contact_by_phone_number()
    if entry == "e":
        return display_contactbook()
    if entry == "q":
        return
    else:
        print("Invalid option, please choose a letter between a to e")
        return start_here()
    

def add_contact(): 
    contact_name = input("Please give me a name: ").strip().lower()
    while contact_name.isdigit():
        print("Please give letters only")
        return add_contact()
    contact_number = input("Now give me that contact's number (no need for special characters such as '+'): ").strip()
    while contact_number.isdigit() == False: 
        print("Please give numbers only")
        return add_contact()
    else:
        contacts.update({contact_name:contact_number})  
        print("Details received:", *[str(k) + ' : + ' + str(v) for k,v in contacts.items()], sep='\n')
    return start_here()

def remove_contact(): 
    delete = input("Type the name of contact you wish to delete: ").strip().lower()
    if delete in contacts.keys():
            contacts.pop(delete)
            print("Contact deleted. See updated contact book below:", *[str(k) + ' : + ' + str(v) for k,v in contacts.items()], sep='\n')
            return start_here()         
    else:
        print("You don't have that contact")
        return start_here()

def search_contact_by_name(): 
    search_name = input("Type the name of the contact you are looking for: ").strip().lower()
    if search_name in contacts.keys(): 
        print("Contact", search_name, "found with phone number +",contacts[search_name]) #crude but works
        return start_here()
    else: 
        print("Contact not found")
        return start_here()

def search_contact_by_phone_number(): 
    search_number = input("Type the number of the contact you are looking for: ").strip()
    for name, number in contacts.items():
        if search_number == number:
            print("Contact number +",search_number, "found for contact", name)
            return start_here()
    else: 
        print("Contact not found")
        return start_here()


def display_contactbook(): 
    if bool(contacts) != False: 
        print("Your contacts are", *[str(k) + ' : +' + str(v) for k,v in contacts.items()], sep='\n')        #print("Your contacts are:\n", contacts)
        return start_here()
    else:
        print("No contacts yet, go back to the menu to add one")
        return start_here()



start_here()





#%%



