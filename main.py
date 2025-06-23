import os
import subprocess


dir_list = os.listdir()


def num_assign(list):
    directory_dict = {}
    number = 1
    for i in list:
        directory_dict[number] = i
    return directory_dict


def move_into_dir(choice):

# print(num_assign(dir_list))
# dir = input("")
subprocess.run('ls')
