

def getStuff() -> list:
    my_list = []
    'returns a list containign all of the user input'
    user_input = " "
    while len(user_input) != 0:
        user_input = input("input some stuff")
        my_list.append(user_input)
    return my_list


def printAll (my_list : [str]):
    print("you inputted: ", " ")
    for i in my_list:
        print(i, " ")


my_list = getStuff()
printAll(my_list)





