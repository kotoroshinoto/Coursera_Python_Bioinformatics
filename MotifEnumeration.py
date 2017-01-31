#!/usr/bin/env python3
__author__ = 'mgooch'
from BioinformaticsFunctions import *
debug = True
import sys
lines = sys.stdin.read().splitlines()
numbers = lines[0].strip().split()
k = int(numbers[0])
d = int(numbers[1])
dnalist = []

lines.pop(0)

while len(lines):
	dnalist.append(lines[0])
	lines.pop(0)
if 'debug' in globals():
	print("k : %d" % k)
	print("d : %d" % d)
	print("dnalist : \n%s" % "\n".join(dnalist))
	print("\n\n")
motifs = MotifEnumeration(dnalist, k, d)
if len(motifs) > 1:
	print(" ".join(motifs))
elif len(motifs) == 1:
	print(motifs[0])
else:
	print('')
