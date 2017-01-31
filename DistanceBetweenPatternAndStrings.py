#!/usr/bin/env python3
__author__ = 'mgooch'
from BioinformaticsFunctions import *
debug = True
import sys
lines = sys.stdin.read().splitlines()
pattern = lines[0].strip()
dnalistline = lines[1].strip()
dnalist = dnalistline.split()

if 'debug' in globals():
	print("pattern : %s" % pattern)
	print("dna list line: %s" % dnalistline)
	print("dnalist : %s" % "\n".join(dnalist))
	print("\n\n")
hdist = DistanceBetweenPatternAndStrings(pattern, dnalist)
print("%d" % hdist)
