#!/usr/bin/env python3
__author__ = 'mgooch'
from BioinformaticsFunctions import *
debug = True
import sys
lines = sys.stdin.read().splitlines()
# numbers = lines[0].split()
# k = int(numbers[0])
# d = int(numbers[1])
dnalist = []

# lines.pop(0)

while len(lines):
	line = lines[0].strip()
	lines.pop(0)
	if line != '':
		dnalist.append(line)

if 'debug' in globals():
	print("dnalist : \n%s" % "\n".join(dnalist))
	print("\n\n")
# motifs = MotifEnumeration(dnalist, k, d)
# if len(motifs) > 1:
# 	print(" ".join(motifs))
# else:
# 	print(motifs[0])

entropy = Entropy(dnalist)
print(entropy)

