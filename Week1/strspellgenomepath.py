import sys


def quickverify(left, right):
	return left[1:] == right[:-1]
genome = ""
patterns = sys.stdin.readlines()
lseq = patterns[0].rstrip()
genome += lseq
for i in range(1, len(patterns)):
	rseq = patterns[i].rstrip()
	if rseq == "":
		break
	if not quickverify(lseq, rseq):
		raise RuntimeError("Invalid Genome Path List, lseq: %s, rseq: %s" % (lseq, rseq))
	genome += rseq[-1]
	lseq = rseq

print(genome)