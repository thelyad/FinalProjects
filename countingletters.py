'''
Created on Nov 18, 2017

@author: ITAUser
'''
'''create a function that accepts the filename and character'''
def calculate_char(filename, mychar):
    f = open(filename, 'r')
    count = 0;
    isDone = False
    while not isDone:
        char=f.read(1)
        char = char.lower()
        if char == mychar: 
            count = count +1;
        if char == '':
            isDone = True
    print(count)
import string
#make a list with the alphabet
letters = list(string.ascii_lowercase)
#make a list to store the count of each letter
#make loop that counts how many of each letter there are 
#define the maximum value
#find the letter at the max value
#print the answer
