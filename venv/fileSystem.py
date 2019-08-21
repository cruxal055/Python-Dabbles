
def get_input() -> list:
    my_list: [str] = []
    user_input: str = " "
    while True:
        user_input = input("Please input something")
        if len(user_input) == 0:
            break
        my_list.append(user_input)
    return my_list


def write_out(my_list: [str]):
    the_file = open('/Users/blank/Desktop/tester.txt', "w")
    for item in my_list:
        the_file.write(item + '\n')
    the_file.close()


def files_bs():
    the_file = open('/Users/blank/Desktop/tester.txt', "r")

    for line in the_file:
        # if line[-1] == '\n':
        #     line = line[:-1]
        print(line)
    the_file.close()


my_list = get_input()
write_out(my_list)u