#!/usr/bin/python

import sys,hashlib

if len(sys.argv) != 2:
    print "[!] python RainbowTable.py list.txt"
    sys.ext()

filename = sys.argv[1]

f = open(filename, "r")
file_data = f.readlines()
for line in file_data:
    hashed_word = hashlib.sha1(line.strip("\n")) .hexdigest()
    print "{0} : {1}".format(line.strip("\n"),hashed_word)