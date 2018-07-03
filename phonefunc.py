def menu_option(number)
        menu_option = {
            "1"
        }


def editphonebook(phonebook):
    menu = True
    while menu:
        choice = int(raw_input(
            "1. Look up an entry\n" + 
            "2. Set an entry\n" + 
            "3. Delete an entry\n" + 
            "4. List all entries\n" + 
            "5. Quit\n" + 
            "What do you want to do (1-5)?\n"))
        if choice == 1:
            name = raw_input("Who are you looking up?\n")
            name = name.lower()
            if name in phonebook:
                print phonebook[name]
            else:
                print "They do not exist in phonebook"
                continue
            continue
        elif choice == 2:
            newname = raw_input("Who are you adding?\n")
            phonenum = raw_input("What is their phone number?\n")
            phonebook[newname.lower()] = phonenum
            continue
        elif choice == 3:
            deletename = raw_input("Who are you removing?\n")
            deletename = deletename.lower()
            if deletename in phonebook:
                del phonebook[deletename]
            else:
                print "Name does not exist"
                continue
        elif choice == 4:
            print phonebook
        elif choice == 5:
            menu = False
        else:
            print "invalid input\n"
    return phonebook