Notes:
#1 In function we need not have to mention "return"

def anagram (a,b):
    if sorted(a)== sorted(b):
        print("It is Anagram")
    else:
        print("It is not an Anagram")


anagram("listen","silent")
# use of "find" function

def find_substring (string,substring):
    if string.find(substring)==-1:
        print ("Not found")
    else:
        print ("Found")


string ="geeks for geeks"
substring = "geeks"

find_substring(string,substring)

##password generator code
import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 8
p =  "".join(random.sample(s,passlen ))
print (p)

#1. to count small and capital characters in a string

def up_low(string):
    uppers = 0
    lowers = 0
    for char in string:
        if char.isupper():
            uppers = uppers+1
        elif char.islower():
            lowers = lowers+1

    return (uppers,lowers)

print (up_low('Hello Mr. Rogers, how are you this fine Tuesday?'))

#2. Password Checking

# Option:1
  password = "unsafepassword"
  if password == "unsafepassword":
    print("You may enter.")
  else:
    print("Try again!")
# Option:2 a more practical password-checking piece of code:

  real_password = "unsafepassword"
  user_password = input("Enter the password: ")
  while user_password != real_password:
    user_password = input("Enter the password: ")
  print("You may enter!")


#2. to count digit and letter characters in a string

def char_dig (string):
    char = 0
    dig = 0
    for i in string:
        if i.isalpha():
            char = char+1
        elif i.isdigit():
            dig = dig+1
    return (char,dig)

print (char_dig("Tom1234"))

for i in string:
    i.isdigit()

#3 to add and chop suffix

def mix_char (a):
    if a [-3:] == "ing":
        a += "ly"
    else:
        a+= "ing"
    return a


print(mix_char("sing"))

print(mix_char("play"))

#4. Find numbers between two numbers where each digit of a number is an even number

items = []
for i in range (100,400):
    s = str(i)
    if (int(s[0])%2 == 0) and (int(s[1])%2 == 0) and (int(s[2])%2 == 0):
    # if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
        items.append(s)
print (items)
print (",".join(items))

# 5 convert lower case string to upper case

print("Enter 'x' for exit.")
string = input("Enter any string to convert in uppercase: ")
if string == 'x':
    exit()
else:
    string_in_uppercase = string.upper()
    print("\nString in Uppercase =",string_in_uppercase)

#6 to make the lowercase string into uppercase (hello-->Hello)
lines = []

while True:
    s = input()
    if s:
        lines.append(s.upper())
    else:
        break

for sentence in lines:
    print (sentence)

# 7 Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for i in range (1,51):
    if (i%3==0) and (i%5==0):
        print ("fizzbuzz")

    elif i%3 == 0:
        print ("fizz")

    elif i%5 ==0:
        print ("buzz")
    else:
        print(i)

#4 Python program to create a 2 Dimensional matrix
n = 3
m = 4
a = [[0] * m for i in range(n)]
print (a)

#program, which will find all such numbers between 1000 and 3000(both included) such that each digit of the number is an even number. The numbers obtained should be printed in a comma - separated sequence on a single line.

l = []
for i in range (2000,3001):
    s = str(i)
    if  (int(s[0])%2 ==0) and (int(s[1])%2 ==0)and (int(s[2])%2 ==0)and(int(s[3])%2):
        #if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
        l.append(i)
print (l)

# REgular Expression

import re
def remove_special_characters(text, remove_digits=False):
    pattern = r'[^a-zA-z0-9\s]' if not remove_digits else r'[^a-zA-z\s]'
    text = re.sub(pattern, '', text)
    return text


print (remove_special_characters("Well this was fun! What do you think? 123#@!",
                          remove_digits=True))

#5 Program to scrap newspaper data using beautiful soap

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")
# Print news title, url and publish date
for news in news_list:
  print(news.title.text)
  print(news.link.text)
  print(news.pubDate.text)
  print("-"*60)
