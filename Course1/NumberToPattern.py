#!/usr/bin/env python3
__author__ = 'mgooch'
from BioinformaticsFunctions import *
debug = True
import sys
lines = sys.stdin.read().splitlines()
number = int(lines[0])
k = int(lines[1])
if 'debug' in globals():
	print("number : %s" % number)
	print("k : %d" % k)

pattern = NumberToPattern(number, k)
print(pattern)
