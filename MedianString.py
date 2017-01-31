#!/usr/bin/env python3
__author__ = 'mgooch'
from BioinformaticsFunctions import *
debug = True
import sys
lines = sys.stdin.read().splitlines()
k = int(lines[0].strip())
dnalist = []
lines.pop(0)

while len(lines):
	line = lines[0].strip()
	if line != "":
		dnalist.append(line)
	lines.pop(0)

if 'debug' in globals():
	print("k : %d" % k)
	print("dnalist : %s" % "\n".join(dnalist))
	print("\n\n")
median = MedianString(dnalist, k)
print(median)
