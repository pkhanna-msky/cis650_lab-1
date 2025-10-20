import os
print(os.getcwd())
os.chdir('Lab7-FileOperations')
filename = input('Enter a text file name: ')
with open(filename) as your_file:
    print(your_file.readline())
    print(your_file.readline())

print("reading all the lines\n=============")   
with open(filename) as your_file:
    my_text_file_data = your_file.readlines()
    print(my_text_file_data)
    #print(your_file.readlines())
    