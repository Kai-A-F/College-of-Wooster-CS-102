# Kai Francis
# Lab 04: Functions
# 09/06/2021

# TODO: Write your functions here
#part1
string="Hello World!"
length=0
for i in string:
    length=length+1


#part2
has_character = "Hello World!!"
if 'd' in has_character:
    print("True!")
else:
    print("False!")
#part3
import string
has_upper = "hello world"
correct = string.ascii_letters
if has_upper in correct:
    print("True")
else:
    print('False')

#part4
vowel = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
find_vowels= ("helloworld")
count = 0
for letter in find_vowels:
    if letter in vowel:
        count += 1
print(count)
vowel = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
find_vowels= ("COmputErScience")
count = 0
for letter in find_vowels:
    if letter in vowel:
        count += 1
print(count)

#part5
def find_substring(string, sub_str):
    if (string.find(sub_str) == -1):
        print("True")
    else:
        print("False")
            
string = "Hello World"
sub_str ="lo Wo"
find_substring(string, sub_str)

#part6
def is_palindrome(k, a, f):
    return k, a, f== k[::-1]
 
k = "racecar"
a = "evil olive"
f = "taco cat"
ans = is_palindrome(k, a, f)
 
if ans:
    print("True")
else:
    print("False")
    
#part7
find_character = "Hello World"
character = "r"

if character in find_character:
    print ("Found!")
else:
    print ("Not Found!")
    
#part8
def skip(string):
    ret = ""
    i = True  
    for char in string:
        if i:
            ret += char
        if char != ' ':
            i = not i
    return ret
print(skip("helloworld"))

#part9
sentence = ("Computer Science is neat!")
longest = max(sentence.split(), key=len)
print("Longest word is: ", longest)
print("And its length is: ", len(longest))

# Code to execute when the program starts
def main():
    # TODO: Run the functions you write here
    #1
    #2
    #3
    #4
    #5
    #6
    #7
    #8
    #9
  
# DO NOT EDIT THE LINES BELOW THIS COMMENTi
    if __name__ == "__main__":
    # Call main function
        main()