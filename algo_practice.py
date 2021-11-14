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
    if len(string_a) is not len(string_b):
        return False
    # string_a_dict = dict("string_a")
    test = '{"a": 1, "b": 2}'
    result = json.loads(test)
    print(result)

is_anagram("cars", "scar")

