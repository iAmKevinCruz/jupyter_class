import json

"""
Problem 1
Given two strings (string_a and string_b) let's check whether or not they are anagrams of each other given the following criteria:

Two strings are only anagrams of each other if all conditions below are met:

    1. They must be of exactly the same length.
    2. They must use exactly the same characters (no more, no less).
    Example: cars and scar, heart and earth, etc.
"""


def is_anagram(string_a, string_b):
    new_string_a = string_a.replace(" ", "").lower()
    new_string_b = string_b.replace(" ", "").lower()
    if len(new_string_a) is not len(new_string_b):
        return ("The length is wrong")
    char_times_a = dict()
    char_times_b = dict()
    
    for i in range(len(new_string_a)):
        if new_string_a[i] not in char_times_a.keys():
            char_times_a[new_string_a[i]] = 1
        else:
            char_times_a[new_string_a[i]] += 1
        if new_string_b[i] not in char_times_b.keys():
            char_times_b[new_string_b[i]] = 1
        else:
            char_times_b[new_string_b[i]] += 1
    
    return char_times_a == char_times_b

is_anagram("cars", "scar")



class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items[len(self.items)-1]

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []