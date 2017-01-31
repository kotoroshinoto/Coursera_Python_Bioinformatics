import sys

ksize = int(sys.stdin.readline().rstrip())
original = str(sys.stdin.readline().rstrip())
kmerlist = list()
for i in range(0, len(original) - ksize + 1):
	kmer = original[i:(i+ksize)]
	kmerlist.append(kmer)
for kmer in sorted(kmerlist):
	print(kmer)
