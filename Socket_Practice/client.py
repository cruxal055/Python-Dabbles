import socket


temp = socket.socket()

temp.connect(("HIDDEN", 1234))
print("sucuessfully connected!")
temp_input = temp.makefile('r')
str_input = " "
while len(str_input) != 0:
    str_input = temp_input.readline()
    print(str_input)
print("im done")