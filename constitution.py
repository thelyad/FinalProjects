'''
Created on Nov 4, 2017

@author: ITAUser
'''
import string 

def calculate_char(filename, mychar):
    f = open(filename, 'r')
    count = 0;
    words = f.read()
    for word in words:
        for letter in word:
            if letter.lower() == mychar:
                count = count+1
    return count

letters = list(string.ascii_lowercase)
letters_count = [0]*26
for i in range(1,26):
    letters_count[i] = calculate_char('constitution.txt', letters[i])
print(letters_count)
m = max(letters_count)
max_index = 0
for i in range(1,26):
    if m == letters_count[i]:
        max_index = i
        break
print(letters[max_index])