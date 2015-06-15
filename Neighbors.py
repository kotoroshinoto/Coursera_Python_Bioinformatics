#!/usr/bin/env python3
__author__ = 'mgooch'
from BioinformaticsFunctions import *
# debug = True
import sys
lines = sys.stdin.read().splitlines()
pattern = lines[0]
d = int(lines[1])
if 'debug' in globals():
	print("pattern : %s" % pattern)
	print("d : %d" % d)

neighborhood = Neighbors(pattern, d)
print("\n".join(neighborhood))
