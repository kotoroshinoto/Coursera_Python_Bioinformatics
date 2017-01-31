#!/usr/bin/env python3
__author__ = 'mgooch'
from BioinformaticsFunctions import *
debug = True
import sys
lines = sys.stdin.read().splitlines()
pattern = lines[0]
genome = lines[1]
d = int(lines[2])
if 'debug' in globals():
	print("pattern : %s" % pattern)
	print("genome : %s" % genome)
	print("d : %d" % d)

positions = ApproximatePatternSearch(pattern, genome, d)
print(" ".join(str(x) for x in positions))
