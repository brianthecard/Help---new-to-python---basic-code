my_list = ["apple", "testing", "check"] # default list
add = 0 # had to use this stupid shit to not get glitchy af
password = 0 # set to 0 on startup, to signify the login process

# THIS SHIT IMPORTS A SINGLE PASSWORD FROM A TEXT FILE!

with open("/projects/test/passwords.txt", "r") as myfile:
    password_list = myfile.read()

# THIS SHIT IMPORTS A SINGLE PASSWORD FROM A TEXT FILE!

while True:
    if password == 0:
        variable_2 = input("Password: ")
        if variable_2 == (password_list):
            password = 1
            continue
        else:
            print("Error: wrong password")
            continue
    else:
        variable = input("Terminal: ")
    if variable == "add":
        thing_to_add = (input("What to add?: "))
        for x in my_list:
# HELP HERE !!!!!!
            if x == thing_to_add:
                print("already listed")
                my_list.remove(thing_to_add)
                continue
            else:
                #print(thing_to_add)
                add = 1
                continue
    if add == 1:
        my_list.append(thing_to_add)
        add = 0
        continue


    elif variable == "search":
        search = input("looking for?: ")

        if search in my_list:
            variable_1 = 1
            print(str(search) + " " + "found!")
            continue
        else:
            variable_1 = 0
            print(str(search) + " " + "not found!")
            continue

    elif variable == "list":
        print(my_list)
        continue

    elif variable == "remove":
        delete = input("Delete what?: ")
        my_list.remove(delete)
        continue

    elif variable == "log-out":
        password = 0
        continue
    elif variable == "help":
        print("Commands: list, search, add, remove, log-out, (and help, idiot)")

    else:
        print("Error: invalid command!")
        continue

    #check

