# -*- coding: utf-8 -*-

from __future__ import print_function
import json,urllib2,sys,getopt,string,time,random
from itertools import chain, imap, product
import itertools

baseURL = "http://suggestqueries.google.com/complete/search?client=firefox&q="

depth = 0
base = "dc%20"

# http://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()


# print(len(sys.argv))
if len(sys.argv) > 1:
  base = urllib2.quote(sys.argv[1]) + "%20"
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

iter = 0

for fetch in fetches:
    time.sleep(random.random() * 0.5)
    response = urllib2.urlopen(baseURL + fetch)
    text = unicode(response.read(), "ISO-8859-1")
    data = json.loads(text)
    try:
        output.extend(data[1])
    except ValueError,UnicodeDecodeError:
        pass
    iter = iter + 1
    printProgressBar(iter,len(fetches),length=80)

outputText = "\n".join(sorted(set(output)))
print(outputText)
