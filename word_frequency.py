#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True
def ask_user():
    user_sentence = input("Enter a sentence: ")
    while (is_sentence(user_sentence) == False):
        print("This does not meet the criteria for a sentence.")
        user_sentence = input("Enter a sentence: ")

    return user_sentence
        
def replace_letter(user_sentence):
    user_sentence = user_sentence.replace('.', '')
    user_sentence = user_sentence.replace('!', '')
    user_sentence = user_sentence.replace('?', '')

    user_sentence = user_sentence.lower()
    word_list = user_sentence.split()
    return word_list

def frequency_count(word_list):
    words = []
    frequencies = []

    for i in word_list:
        if words.count(i) > 0:
            index = words.index(i)
            frequencies[index] = frequencies[index] + 1
        else:
            words.append(i)
            frequencies.append(1)
    return [words,frequencies]
    
def print_output(words, frequencies):
    print("Output:")
    for i in range(len(words)):
        print(words[i], ":", frequencies[i])

def main():
    user_sentence = ask_user()
    word_list = replace_letter(user_sentence)
    words, frequencies = frequency_count(word_list)
    print_output(words, frequencies)
    
main()
