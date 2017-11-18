'''
Created on Nov 18, 2017

@author: ITAUser
'''
'''create a function that accepts the filename and character'''
def countingLetters(filename, mychar):
    f = open(filename, 'r')
    count = 0;
    run = True
    while run:
        letter = f.read(1) # 1 means read one character at a time
        # Make the char lowercase by using the function char.lower()```
        letter = letter.lower()
        # If the character exists, note that if the character not exist, 
            #char == "" is True ```
        if letter == "":
            break
        else:
            if letter == mychar:
                count = count + 1
            # If the character is equal to variable mychar```
                # Update count by increament by 1 ```
    print(count)
    #We finish the loop, output the result ```
    
countingLetters(filename="constitution.txt", mychar = "a")
#countingLetters("constituion.txt", "a")

