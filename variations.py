#!/usr/bin/env python 3.7

message = input('please enter a message: ')

print("Lowercase:", message.lower())
print("Uppercase: ", message.upper())
print("Title case: ", message.title())
print("Capitalized: ", message.capitalize())

words = message.split()
print("words: ", words)

sorted_words = sorted(words)

print("Aplhabetic first word: ", sorted_words[0])
print("alphabetic last word: ", sorted_words[-1])
