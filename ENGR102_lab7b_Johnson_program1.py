"""This program is meant to help give you practice with string manipulation.
“Pig Latin” is a way of converting words in standard English to similar words that sound different. The
rules for converting from standard words to Pig Latin are as follows:
• If a word starts with a consonant, move the consonants to the end of the word, and add “ay” to
the end.
o e.g. “computer” becomes “omputercay”
• If a word starts with a vowel, add “yay” on to the end of the word.
o e.g. “engineering” becomes “engineeringyay”
• Note: treat “y” as a vowel for this assignment.
Write a program that repeatedly reads in a word from a user and converts it to Pig Latin. The program
should continue reading words until the user enters “stop”.
Challenge: Try to write a program where, instead of just one word, the user enters an entire sentence,
and all words in the sentence are converted to Pig Latin."""

"""
By submitting this assignment, I agree to the following:
“Aggies do not lie, cheat, or steal, or tolerate those who do”
“I have not given or received any unauthorized aid on this assignment”


Name : Dathan Johnson
Section : 409
Assignment : lab 7b - 1
Date : 2-28-19
"""
# define variables
# creat strings
word = ''
#list for vowels
vowel = ['a', 'e', 'i', 'o','u','y','A','E','I','O','U','Y']
stryay = 'yay'
stray = 'ay'
space = ' '
complete = ''
#empty list that will later be used to compile a sentence
sentence = []
#list of capitalized consonants
consonant = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z', 'W']
#list of lowercase consonants
consonantlo = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z', 'w']
#loop for the continous input of words
while word != 'stop':
    word = input('what is your word?(stop quits code) ') # word input
    if space in word: # space means a sentence
        line = word.split() # line is a list that equals each word in the sentence
        for word in line: # for loop in list line
            if word[0] in vowel: # statements to transfer to Pig Latin
                word = word + stryay
                sentence.append(word) # append word to empty list
            elif word[0] in consonant or word[0] in consonantlo and word != 'stop':
                wcons = word[0]
                word = word[1:]
                word = word + wcons + stray
                sentence.append(word) # append word to empty list
        complete = ' '.join(i for i in sentence) # creates a string from the list
        print(complete) # print list
        sentence = [] # resets the list
    # transfering to pig latin for one word
    elif word[0] in vowel:
        word = word + stryay
        print(word)
    elif word[0] in consonant or word[0] in consonantlo and word != 'stop':
        wcons = word[0]
        word = word[1:]
        word = word + wcons + stray
        print(word)
    

    
