# de bruijn graph is prefix -> suffix of kmers using nodes of size k-1 and each node can be a prefix or a suffix
# duplicates are not only allowed, they must be represented and are required information
import sys
ksize = int(sys.stdin.readline().rstrip())
bruijsize = ksize - 1
seq = sys.stdin.readline().rstrip()
# nodes = list()  # type: list[str]
adjacencylist = dict()  # type: dict[str, list[str]]

prefix = seq[0:bruijsize]
suffix = ""

for i in range(0, len(seq)-bruijsize):
	prefix = seq[i:i+bruijsize]
	# if prefix not in nodes:
	# 	nodes.append(prefix)
	suffix = seq[i+1:i+bruijsize+1]
	# if suffix not in nodes:
	# 	nodes.append(suffix)
	# print("position: %d, kmer: %s => %s -> %s" % (i, seq[i:i+ksize], prefix, suffix))
	if prefix not in adjacencylist:
		adjacencylist[prefix] = list()
		# print("created entry for %s" % prefix)
	adjacencylist[prefix].append(suffix)
	# print("appended %s to entry for %s" % (adjacencylist[prefix][-1], prefix))
if suffix not in adjacencylist:
	adjacencylist[suffix] = list()
for item in sorted(adjacencylist.keys()):
	# print(item)
	if len(adjacencylist[item]) > 0:
		print("%s -> %s" % (item, (",".join(adjacencylist[item]))))
