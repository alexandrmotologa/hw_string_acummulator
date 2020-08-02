def get_user_friends():
    friends = ""
    friend = None
    inp_stop = 0

# verificarea daca apar errori la executare
    try:
        friend_nr = int(input("Enter a number of your friends: "))
        assert friend_nr >= 0

# adaugat in caz ca sunt introduse date de tip str sau floatin input
    except ValueError:
        print("That's not a valid option!")
        exit()

# adaugat in caz ca sunt introduse numere negative
    except AssertionError:
        print("Number is negative")
        exit()

    while inp_stop != friend_nr and friend != "":
        if friend_nr > 0:
            friend = input("Friend name?: ")
            if inp_stop == (friend_nr - 1):
                friends += friend + "."
                inp_stop += 1
            elif inp_stop >= 0:
                friends += friend + ", "
                inp_stop += 1

    print("User friends: " + friends)


#######
get_user_friends()
