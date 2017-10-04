# workshop.py
# Python as a Tool for Social Scientists
# NaLette Brodnax
# www.nalettebrodnax.com
# August 24, 2017

import csv

print("What file should I read from?")

filename = input("> ")

print("How many lines should I read?")

lines_to_read = input("> ")
line_counter = 0

# open file and read the lines given by the user

# file = open(filename, 'r')
# while line_counter < int(lines_to_read):
#     print(file.readline())
#     line_counter = line_counter + 1
# file.close()

with open(filename, 'r') as file:
    while line_counter < int(lines_to_read):
        print(file.readline())
        line_counter += 1
    print(str(line_counter) + " lines read\n")

# count words
def count_words(mytext):
    """Returns the number of words in a string
    str -> int"""
    words = mytext.split(" ")
    return len(words)

# find average length
def longest_word_length(mytext):
    """Returns the average word length in a string
    str -> int"""
    words = mytext.split(" ")
    word_lengths = []
    for word in words:
        word_lengths.append(len(word))
    return max(word_lengths)

# export line information to csv file
with open("workshop.csv", 'w') as csvfile, \
     open(filename, 'r') as txtfile:
    writer = csv.writer(csvfile)
    writer.writerow(["line number", "word count", "longest word length"])
    line_counter = 0
    while line_counter < int(lines_to_read):
        line_number = line_counter + 1
        content = txtfile.readline()
        word_count = count_words(content)
        longest_word = longest_word_length(content)
        writer.writerow([line_number, word_count, longest_word])
        line_counter += 1


