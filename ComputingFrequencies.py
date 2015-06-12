#!/usr/bin/env python3
__author__ = 'mgooch'
from BioinformaticsFunctions import *
debug = True
import sys
lines = sys.stdin.read().splitlines()
text = lines[0]
k = int(lines[1])
if 'debug' in globals():
	print("text : %s" % text)
	print("k : %d" % k)

frequencies = ComputingFrequencies(text, k)
print(" ".join(str(x) for x in frequencies))
