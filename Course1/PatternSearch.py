#!/usr/bin/env python3
__author__ = 'mgooch'
from BioinformaticsFunctions import *
debug = True
import sys
lines = sys.stdin.read().splitlines()
pattern = lines[0]
genome = lines[1]
if 'debug' in globals():
	print("pattern : %s" % pattern)
	print("genome : %s" % genome)

positions = PatternSearch(pattern, genome)
print(" ".join(str(x) for x in positions))
