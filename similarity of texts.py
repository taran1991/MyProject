
# coding: utf-8

 """A set of sentences copied from Wikipedia is given. Each of them has a "cat theme" in one of three meanings:
 1)cats (animals),
 2)UNIX-utility cat for outputting the contents of files,
 3)versions of the operating system OS X, named after the family of felines.
 Task is to find two sentences, which are closest in the sense. Measure of closeness  is cosine distance."""

# Reading sentences from file
text = ''
with open('C:\\Users\\Home\\Downloads\\sentences.txt') as inf:
    for line in inf:
        line = line.strip().lower() 
        text += line + '\n'


# Splitting the text into words.
import re
slova = set()
slova = re.split('[^a-z]', text)
for i in range(slova.count('')):
    slova.remove('')


# Creation dictionary with all words with indexation
dictionary = {}
index = 0
for slovo in slova:
    if slovo not in dictionary:
        dictionary[slovo] = index
        index += 1


# Creation a matrix of size n * d, n - number of sentences, d - number of words. 
# The element with the index (i, j) in this matrix equal to the number of occurrences of the j-th word in the i-th sentence.
stroki = text.split('\n')
reverse_dicionary = {}
for key,value in dictionary.items():
    reverse_dicionary[value] = key
slova = set()
matrix = [[0 for j in range(len(dictionary))] for i in range(len( stroki) -1)]
for i in range(len(stroki)-1):
    slova = re.split('[^a-z]', stroki[i]) 
    for j in range(len(dictionary)):
        if reverse_dicionary[j] in slova:
            matrix[i][j] = slova.count(reverse_dicionary[j])


# Finding the cosine distance from the first sentence to all the rest.
from scipy import spatial
distance = []
for i in range(len(stroki)-1):
    distance.append(spatial.distance.cosine(matrix[i],matrix[0]))


# Finding two minimum of cosine distances
min1 = 1
min2 = 2
min1, min2 = min(min1,min2), max(min1,min2)
for i in range(4,len(stroki)-1):
    if distance[i] > distance[min1] and distance[i] < distance[min2] and distance[i] > 0:
        min2 = i
    elif distance[i] < distance[min1] and distance[i] > 0:
        min1,min2 = i,min1


# Writing results into file
file_obj = open('C:\\Users\\Home\\Downloads\\submission-1.txt', 'w')
string = str(min1) + ' ' + str(min2)
file_obj.write(string)
file_obj.close()

