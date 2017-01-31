#!/usr/bin/env python3
__author__ = 'mgooch'
from BioinformaticsFunctions import *
debug = True
import sys
lines = sys.stdin.read().splitlines()
genome = lines[0]
args = lines[1].split()
k = int(args[0])
L = int(args[1])
t = int(args[2])
if 'debug' in globals():
	print("text : %s" % genome)
	print("k : %d" % k)
	print("t : %d" % t)
	print("L : %d" % L)

clumps = ClumpFinding(genome, k, L, t)
print(" ".join(str(x) for x in clumps))
