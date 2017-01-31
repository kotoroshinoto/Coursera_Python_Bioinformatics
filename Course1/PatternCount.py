#!/usr/bin/env python3
__author__ = 'mgooch'
from BioinformaticsFunctions import *
debug = True
import sys
lines = sys.stdin.read().splitlines()
text = lines[0]
pattern = lines[1]
if 'debug' in globals():
	print("text : %s" % text)
	print("pattern : %s" % pattern)

count = PatternCount(text, pattern)
print("%d" % count)
