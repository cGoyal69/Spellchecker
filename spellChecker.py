import csv
import re


def strAssignment_star(word, index):
    word = list(word)
    word[index] = ".*"
    new_regex = ""
    for char in word:
        new_regex += char
    return new_regex+"$"


def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    #Taken from https://github.com/dwyl/english-words.git
    return valid_words


english_words = list(load_words())
word_search  = input("Enter the word: ")
words_to_search = list(set(word_search.split()))
correct_Guess = {}
n = len(words_to_search)

 
def findAlternates(word):
    correct_Guess = []
    w = word
    for i in range(len(word)):
        w = strAssignment_star(w, i)
        for check_word in english_words:
            if re.search(w, check_word):
                correct_Guess.append(check_word)
        w = word
        return correct_Guess

for word in words_to_search:
    correct_Guess[word] = findAlternates(word)
    
def freqMatcher(word, correct_guess):
    freqCheck = {}
    # print(correct_Guess)
    for word in correct_Guess.keys():
        for wording in correct_Guess[word]:
            if wording in freqCheck.keys():
                freqCheck[wording]+=1
            else:
                freqCheck[wording] = 1
    return freqCheck

freqCheck = freqMatcher(word, )

probWords = {}
with open("corpusCheck/mycsvfile.csv", "r+") as f:
    w = csv.reader(f)
    for lines in w:
        if lines[0] in freqCheck.keys():
            probWords[lines[0]] = lines[1]
    
print(probWords)
