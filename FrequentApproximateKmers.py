#!/usr/bin/env python3
__author__ = 'mgooch'
from BioinformaticsFunctions import *
debug = True
import sys
lines = sys.stdin.read().splitlines()

genome = lines[0]
numbers = lines[1].split()
k = int(numbers[0])
d = int(numbers[1])
if 'debug' in globals():
	print("genome : %s" % genome)
	print("k : %d" % k)
	print("d : %d" % d)

freqwords = FrequentApproximateSequences(genome, k, d)
print(" ".join(freqwords))
