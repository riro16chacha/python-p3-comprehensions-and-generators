#!/usr/bin/env python3

def return_evens(sequence):
    evens = [num for num in sequence if num % 2 == 0]
    return evens

result = return_evens([0, 2, 3, 5, 7, 8, 9])
print(result)

def make_exclamation(sentences):
    return [sentence + '!' for sentence in sentences]

result = make_exclamation(["Hello", "I'm doing great", "Python is fun"])
print(result)