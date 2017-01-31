import sys


class GenomePathNode:
	def __init__(self, sequence):
		self.seq = sequence
		self.nodes_from = list()
		self.nodes_to = list()

	def verify_kmersize(self, kmersize):
		seqlen = len(self.seq)
		if kmersize > seqlen or kmersize <= 0:
			return None
		if kmersize == seqlen:
			return False
		if kmersize < seqlen:
			return True

	def left_slice(self, kmersize:int = None) -> str:
		if kmersize is None:
			kmersize = len(self.seq) - 1
		verified = self.verify_kmersize(kmersize)
		if verified is None:
			#TODO throw and handle exception
			pass
		elif verified:
			removenum = len(self.seq) - kmersize
			return self.seq[:-removenum]
		else:
			return self.seq

	def right_slice(self, kmersize:int = None) -> str:
		if kmersize is None:
			kmersize = len(self.seq) - 1
		verified = self.verify_kmersize(kmersize)
		if verified is None:
			#TODO throw and handle exception
			pass
		elif verified:
			removenum = len(self.seq) - kmersize
			return self.seq[removenum:]
		else:
			return self.seq

	def can_precede(self, othernode:'GenomePathNode', kmersize=None) -> bool:
		return self.right_slice() == othernode.left_slice(kmersize)

	def can_follow(self, othernode:'GenomePathNode', kmersize=None) -> bool:
		return self.left_slice() == othernode.right_slice(kmersize)

	def forge_link(self,  destnode:'GenomePathNode'):
		if destnode not in self.nodes_to:
			self.nodes_to.append(destnode)
		if self not in destnode.nodes_from:
			destnode.nodes_from.append(self)

patterns = sys.stdin.readlines()
nodes = list()  # type: list[GenomePathNode]
for pattern in patterns:
	tmpstr = pattern.rstrip()
	if not (tmpstr == ""):
		nodes.append(GenomePathNode(pattern.rstrip()))

adjacency_matrix = dict()  #type: dict[GenomePathNode, dict[GenomePathNode, bool]]
for litem in nodes:
	if litem not in adjacency_matrix:
		adjacency_matrix[litem] = dict()
	for ritem in nodes:
		if ritem not in adjacency_matrix[litem]:
			adjacency_matrix[litem][ritem] = litem.can_precede(ritem)
			if adjacency_matrix[litem][ritem]:
				litem.forge_link(ritem)

for node in nodes:
	for link in node.nodes_to:
		print("%s -> %s" % (node.seq, link.seq))
