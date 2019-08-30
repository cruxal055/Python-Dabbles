import socket

temp = socket.socket()
# temp.bind((socket.gethostname(), 1234))
temp.bind(('', 1234))

# while True:
print("looking for a signal")
temp.listen()
clientSoc, where = temp.accept()
print("found a signal from " + str(where))
printer = clientSoc.makefile('w')
user_input = " "
while len(user_input) != 0:
    user_input = input("input stuff: ")
    printer.write(user_input + '\n')
    printer.flush()

print("done!")
