#!/usr/bin/env python3
__author__ = 'mgooch'
from BioinformaticsFunctions import *
debug = True
import sys
lines = sys.stdin.read().splitlines()
numbers = lines[0].strip().split()
k = int(numbers[0])
t = int(numbers[1])
n = int(numbers[2])
dnalist = []

lines.pop(0)

while len(lines):
	line = lines[0].strip()
	if line != "":
		dnalist.append(lines[0])
	lines.pop(0)
if 'debug' in globals():
	print("k : %d" % k)
	print("t : %d" % t)
	print("n : %d" % n)
	print("dnalist : \n%s" % "\n".join(dnalist))
	print("\n")
motifs = GibbsSampler(dnalist, k, t, n)
print("\n".join(motifs))