from __future__ import print_function
import json,urllib2,sys,getopt,string
from itertools import chain, imap, product
import itertools

baseURL = "http://suggestqueries.google.com/complete/search?client=firefox&q="

depth = 0
base = "dc%20"
# print(len(sys.argv))
if len(sys.argv) > 1:
  base = sys.argv[1] + "%20"
if len(sys.argv) > 2:
  depth = int(sys.argv[2])

fetches = [ base ]
output = []

print("Running with keyword",base,"and char depth",depth,"... Run with params [keyword] [chardepth] to change")


alphabet = string.ascii_lowercase

for x in itertools.imap(''.join, itertools.chain(
    *(itertools.product(alphabet, repeat=i)
        for i in range(1,depth+1)))):
            fetches.append(base + x)

# print(fetches)

for fetch in fetches:
    response = urllib2.urlopen(baseURL + fetch)
    data = json.load(response)
    try:
        output.extend(data[1])
    except ValueError:
        pass

outputText = "\n".join(sorted(set(output)))
print(outputText)

# for x in imap(''.join, chain(product(alphabet, repeat=i)
#     for i in range(1,9))):
#         print x
#
# while depth > 0 :
#     for char in string.ascii_lowercase + string.numbers:
#
#
#
#     depth -= 1
#
