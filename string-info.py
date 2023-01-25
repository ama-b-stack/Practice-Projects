#!/usr/bin/env python3.7

message = input("Hello! Please input a word: ")
print("The first letter of this word is: ", message[0])
print("The last letter of this word is: ", message[len(message) - 1])
print("The middle characters of this word are as follows: ", message[1:len(message) - 1])

print("The even characters of this word are as follows: ", message[::2])
print("The odd characters of this word are as follows: ", message[1::2])

print("This word in reverse order is: ", message[::-1])

# cloud guru python course lab work
