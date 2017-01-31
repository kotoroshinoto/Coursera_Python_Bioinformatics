#!/usr/bin/env python3
__author__ = 'mgooch'
from BioinformaticsFunctions import *
debug = True
import sys
lines = sys.stdin.read().splitlines()
pattern1 = lines[0]
pattern2 = lines[1]
if 'debug' in globals():
	print("pattern1 : %s" % pattern1)
	print("pattern2 : %s" % pattern2)

distance = HammingDistance(pattern1, pattern2)
print(distance)
