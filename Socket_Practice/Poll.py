from collections import namedtuple
import socket

already_voted = 0
question_DNE = 1
not_choice = 2

# QUESTIONS, CHOICE 1,

question = namedtuple("question", ["Q", "R1", "R2", "R3", "R4", "A"])

connection = namedtuple("connection", ["socket", "reader", "writer"])


# bind it, and listen
# for others, create the socket, and connect to where the original is bound


def connect(host_name: str, where: int) -> connection:
    new_socket = socket.socket()
    new_socket.bind((host_name, where))
    new_writer = new_socket.makefile('w')
    new_reader = new_socket.makefile('r')
    return connection(new_socket, new_reader, new_writer)


def print_questions(all_questions: list):
    counter = 0
    for i in all_questions:
        print("Q1: " + i.Q)


def load_questions() -> list:
    all_questions = []
    choices = _generate_size_4()
    counter = 0
    str_input = " "
    the_answer = " "
    while True:
        str_input = input("what is your question?")
        if len(str_input) == 0:
            break
        for i in range(4):
            choices[i] = input("what is a choice?")
        the_answer = int(input("what is the answer? (1-4)"))
        all_questions.append(question(str_input, choices[0], choices[1], choices[2], choices[3], the_answer))
    return all_questions


def _generate_size_4() -> list:
    choices = []
    for i in range(4):
        choices.append(" ")
    return choices


def write_to_file(all_questions):
    to_output = open("all_questions.txt", 'w')
    for i in all_questions:
        to_output.write(i.question + " " + i.R1 +
                        " " + i.R2 + " " + i.R3 + " "
                        + i.r4 + " " + i.A + '\n')


def read_in():
    all_questions = []
    to_input = open("all_questions.txt", 'w')
    str_input = " "
    while (len(str_input)) != 0:
        str_input = to_input.readline()
        parts_of_the_file = str_input.split() #yields a list
        all_questions.append(question(parts_of_the_file[0], parts_of_the_file[1], parts_of_the_file[2],
                                      parts_of_the_file[3], parts_of_the_file[4]))


def answer(number, their_answer, list_of_questions):
    if list_of_questions[number].A == their_answer:
        print("correct")
    else:
        print("incorrect")


x = load_questions()
print_questions(x)