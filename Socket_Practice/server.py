import socket

temp = socket.socket()
# temp.bind((socket.gethostbyname('localhost'), 1234))
temp.bind((socket.gethostbyname('localhost'), 1234))
print(socket.gethostbyname('localhost'))

# while True:
temp.listen()
clientSoc, where = temp.accept()
printer = clientSoc.makefile('w')
user_input = " "
while len(user_input) != 0:
    user_input = input("input stuff: ")
    printer.write(user_input + '\n')
    printer.flush()

print("done!")
