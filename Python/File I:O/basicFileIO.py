"""
***************************************************
Title: file IO
Author: Brogan Avery
Created: 2020-02-25
Description :
OS: macOS Catalina
Copyright : This is my own original work based on specifications issued by the course instructor
***************************************************
"""

def write_to_file(some_tuple):
    with open("student_info.txt", "a") as file:
        file.write(str(some_tuple))
        file.write('\n')

def get_student_info(name):
    score_list = []
    score = 0
    while (score > -1 ):
        try:
            score = int(input("Enter (next) test score. Enter -1 when finished: "))
            score_list.append(score)

        except ValueError:
            print("Enter test score. When fisnished, enter -1")
    score_list.remove(-1)
    name_score_tuple = (name, score_list)
    write_to_file(name_score_tuple)

def read_from_file():
    with open("student_info.txt") as file:
        for line in file:
            print(line)


if __name__ == '__main__':
    count = 0
    open("student_info.txt","w").close()
    first_tuple = (1,2,3,4,5)

    write_to_file(first_tuple)

    while (count <5):
        student_name = input("Enter your name:")
        get_student_info(student_name)
        count = count + 1
    read_from_file()
