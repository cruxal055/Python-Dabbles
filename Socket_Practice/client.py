import socket


temp = socket.socket()
temp.connect(("IP_ADDRESS", 1234))
print("connected!")

write_to = socket.socket();
write_to.bind(('', 1234))
write_to.listen()

print("connected pt 2")

client, from_where = write_to.accept()

printer = client.makefile('w')
user_input = ' '


print("sucuessfully connected!")
temp_input = temp.makefile('r')
str_input = " "
while len(str_input) != 0:
    str_input = temp_input.readline()
    print("they said: " + str_input)
    user_input = input("your response?")
    printer.write(user_input + "\n")
    printer.flush()

    # if str_input == ("RESPOND" + '\n'):
    #     user_input = input("your response?")
    #     printer.write(user_input + "\n")
    #     printer.flush()
    # else:
    #     print(str_input)
print("im done")