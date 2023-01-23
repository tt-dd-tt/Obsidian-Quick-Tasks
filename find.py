import os
import pickle


filename = 'tasks_app.md'
file_path = ''

# function named is_path_file that check if there is a file_path.txt file in the device's storage. If not, it will run function find_file() to find the file path of the file named tasks_app.md and store it in a text file. If there is a text file, it will use that text file to get the file_path
def is_path_file():
    global file_path
    if os.path.isfile('path.txt'):
        print('path.txt exists')
        read_path()
    else:
        print('path.txt does not exist')
        find_file(filename)
        print(file_path)
        with open('path.txt', 'w') as f:
            f.write(file_path)
            print('path.txt created')
            print(file_path)
    return file_path

#function that finds a file named tasks_app.md using "os" python package in the device's storage and writes the path to a text file called path.txt
def find_file(filename):
    global file_path
    for root, dirs, files in os.walk('/'):
        if filename in files:
            file_path = os.path.join(root, filename)
            print('find_function returns' + file_path)
            return
    return None

# function that reads file path from text file path.txt
def read_path():
    global file_path
    with open('path.txt', 'r') as f:
        file_path = f.read()
        print(r'read_function' + file_path)
    return file_path
   

print(r' first' + file_path)
is_path_file()
print(r' second' + file_path)
read_path()



