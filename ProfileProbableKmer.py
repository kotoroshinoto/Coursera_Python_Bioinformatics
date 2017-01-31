#!/usr/bin/env python3
__author__ = 'mgooch'
from BioinformaticsFunctions import *
debug = True
def convertFloatArray(text):
	arr = []
	for num in text.split():
		arr.append(float(num))
	return arr
import sys
lines = sys.stdin.read().splitlines()
sequence = lines[0].strip()
k = int(lines[1].strip())
profile = {}
profile['A'] = convertFloatArray(lines[2].strip())
profile['C'] = convertFloatArray(lines[3].strip())
profile['G'] = convertFloatArray(lines[4].strip())
profile['T'] = convertFloatArray(lines[5].strip())

bases = ['A', 'C', 'G', 'T']

if 'debug' in globals():
	print("sequence: %s" % sequence)
	print("k : %d" % k)
	for base in bases:
		probstr = " ".join(map(str,profile[base]))
		print("%s : %s" % (base, probstr))
	print("\n")
kmer = ProfileProbableKmer(sequence, k, profile)
print(kmer)
