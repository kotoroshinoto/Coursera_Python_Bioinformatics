#!/usr/bin/env python3
__author__ = 'mgooch'
from BioinformaticsFunctions import *
debug = True
import sys
lines = sys.stdin.read().splitlines()
pattern = lines[0]
if 'debug' in globals():
	print("pattern : %s" % pattern)

revcomp = ReverseComplement(pattern)
print(revcomp)
