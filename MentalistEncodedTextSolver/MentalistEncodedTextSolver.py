#!/usr/bin/python

from math import factorial
import os
import string
import itertools

def read_from_file(filename):
    file = open(filename, 'rb')
    data = ""
    while True:
        chunk = file.read(512)
        if not chunk:
            file.close()
            break
        else:
            data += chunk
    return data

def write_to_file(filename, data):
    folder = os.path.dirname(filename)
    if len(folder) > 0 and not os.path.exists(folder):
        os.makedirs(folder)
    file = open(filename, 'wb')
    file.write(data)
    file.close()
    
def generate_dictionary():
    dictionary = read_from_file('dictionary_names.txt')
    dictionary += "\n"
    dictionary += read_from_file('dictionary_words.txt')
    dictionary = dictionary.upper()
    dictionaryArray = dictionary.split()
    return dictionaryArray

def is_in_dictionary(decodedWord, dictionary):
    try:
        dictionary.index(decodedWord)
        return True
    except Exception as anException:
        return False
    
def exists_in_solution(text, solutions):
    try:
        solutions.index(text)
        return True
    except Exception as anException:
        return False

def save_solutions(solutions):
    solutions.sort(reverse=True)
    results = "The Mentalist Encoded Text Solver\n" \
              "(Best to Worst Match Order)\n" \
              "---------------------------------\n"
    for index in range(len(solutions)):
        results += "{0}\n" \
                   "---------------------------------\n".format(solutions[index][1])
    results += "Done."
    write_to_file('output.txt', results)

if __name__ == "__main__":
    #1 = Circle w/ dialogal slash
    #2 = Oval w/ vertical slash
    #3 = F
    #4 = Circle w/ horizontal slash
    #5 = Clover
    #6 = Diamond
    #7 = Filled up triangle
    #8 = Square root
    #9 = Standing fish thingy
    #10 = Square
    #11 = Spade
    #12 = Unfilled circle
    #13 = Three horizontal lines
    #14 = X
    #15 = Unfilled up triangle
    #16 = Pentagon house
    #17 = Cents
    #18 = CP 
    #19 = Heart 
    #20 = Upside-down T w/ line underneath 
    #21 = Filled left triangle
    #22 = Cross thingy
    #23 = Circle w/ dot in center
    #24 = Sideways T
    #25 = Small square root
    
    print("The Mentalist Encoded Text Solver\n")
    print("Loading dictionaries. Please wait.\n")
    dictionary = generate_dictionary()
    print("Dictionaries loaded.\n")
    encodedText = [
        [[1,2,3,4,5,6,6,7],[8,9,10,11,12]],
        [[20,12,9,14,8,15,7],[16,4,20,3,3]],
        [[8,17,9,4,4,22,7],[18,24,25,19,6,21]],
        [[13,1,15,20],[9,6,15,1,3,7,16]],
        [[1,2,3,4,5,6],[8,9,10,11,12]],
        [[20,12,9,14,8,15],[16,4,20,3,3]],
        [[8,17,9,4],[18,19,22,23]],
        [[1,15,9,6],[15,1,3,7,16]]
        ]
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    permutations = itertools.permutations(characters)
    solutions = []
    print("Finding possible solutions. This may take awhile.\n")
    for permutation in permutations:
        decodedWords = 0
        isValidDecode = False
        decodedText = ''
        for encodedTextLineIndex in range(len(encodedText)):
            encodedTextLine = encodedText[encodedTextLineIndex]
            newline = '' \
                    if encodedTextLine == range(len(encodedText)) \
                    else "\n"
            for encodedTextWordIndex in range(len(encodedTextLine)):
                encodedTextWord = encodedTextLine[encodedTextWordIndex]
                decodedWord = ''
                for encodedCharacter in encodedTextWord:
                    decodedWord += permutation[encodedCharacter]
                if is_in_dictionary(decodedWord, dictionary):
                    decodedWords = decodedWords + 1
                space = '' \
                    if encodedTextWordIndex == len(encodedTextLine) - 1 \
                    else ' '
                decodedText += "{0}{1}".format(decodedWord, space)
            if encodedTextLineIndex < len(encodedText) - 1:
                decodedText += "\n"
        if decodedWords > 0:
            if not exists_in_solution([decodedWords, decodedText], solutions):
                solutions.append([decodedWords, decodedText])
    print("Saving solutions to disk. Please wait.\n")
    save_solutions(solutions)
    print("Finished. Any solutions are available in output.txt.")