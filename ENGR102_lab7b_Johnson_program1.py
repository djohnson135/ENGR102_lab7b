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
word = ''
vowel = ['a', 'e', 'i', 'o','u','y','A','E','I','O','U','Y']
stryay = 'yay'
stray = 'ay'
consanent = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z', 'W']
consanentlo = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z', 'w']
while word != 'stop':
    word = input('what is your word?(stop quits code) ')
    if word[0] in vowel:
        word = word + stryay
        print(word)
    if word[0] in consanent or word[0] in consanentlo and word != 'stop':
        wcons = word[0]
        word = word[1:]
        word = word + wcons + stray
        print(word)
    

    
