#!/usr/bin/env python3
__author__ = 'mgooch'
from BioinformaticsFunctions import *
debug = True
import sys
lines = sys.stdin.read().splitlines()
pattern = lines[1]
genome = lines[0]
d = int(lines[2])
if 'debug' in globals():
	print("pattern : %s" % pattern)
	print("genome : %s" % genome)
	print("d : %d" % d)

count = ApproximatePatternCount(genome, pattern, d)
print(str(count))
