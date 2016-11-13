import sys
# from datetime import datetime
# start = datetime.now()
nodes = list()  # type: list[str]
prefixes = list() # type: list[str]
suffixes = list() # type: list[str]
adjacency_list = dict()  # type: dict[str, list[int]]
numnodes = 0
for line in sys.stdin:
	node = line.rstrip()
	if node != "":
		nodes.append(node)
		numnodes += 1
		suffix = node[1:]
		prefix = node[:-1]
		suffixes.append(suffix)
		prefixes.append(prefix)
		check_suff = suffixes[-1] not in adjacency_list
		if check_suff:
			adjacency_list[suffix] = list()
		for i in range(0, numnodes):
			#check prefix AND suffix
			if prefixes[i] == suffix:  #  other: BCDEF, ours: ABCDE  ours -> other
				adjacency_list[suffix].append(i)
			if suffixes[i] == prefix:  #  ours: BCDEF, other: ABCDE  other -> ours
				adjacency_list[suffixes[i]].append(numnodes-1)

# print("entries read and adjacency list constructed")

for i in range(0, numnodes):
	for index in adjacency_list[suffixes[i]]:
		print("%s -> %s" % (nodes[i], nodes[index]))
# end = datetime.now()
# print(end - start)