import sys


class DeBruijnIsolatedEdge:
	def __init__(self, seq: str):
		self.prefix = seq[:-1]  # todo need to be able to handle arbitrary kmer sizes
		self.suffix = seq[1:]  # todo need to be able to handle arbitrary kmer sizes
		self.edgeseq = self.suffix[-1]

	def __str__(self) -> str:
		str_form = "%s --[%s]-> %s" % (self.prefix, self.edgeseq, self.suffix)
		print(str_form)
		return str_form


class CompositionGraph:
	def __init__(self):
		self.edges = list()  # type: list[DeBruijnIsolatedEdge]

	@staticmethod
	def from_kmers(kmers: 'list[str]') -> 'CompositionGraph':
		comp_graph = CompositionGraph()
		for kmer in kmers:
			comp_graph.edges.append(DeBruijnIsolatedEdge(kmer))
		return  comp_graph

	def __str__(self) -> str:
		str_form_list = list()
		for edge in sorted(self.edges):
			str_form_list.append("%s" % edge)
		return "\n".join(str_form_list)


class DeBruijnNode:
	def __init__(self, seq: str):
		self.node_seq = seq
		self.edges = dict()  # type: dict[str, 'DeBruijnNode']
		self.edge_degree = {}  # type: dict[str, int]

	def __str__(self):
		listed_edges = ""
		i = 0
		for edge in self.edges:  # type: str
			edge_count = self.edge_degree[edge]
			while edge_count > 0:
				listed_edges += self.edges[edge].node_seq
				if edge_count > 1:
					listed_edges += ','
				edge_count -= 1
			if i+1 != len(self.edges):
				listed_edges += ','
			i += 1
		return "%s -> %s" % (self.node_seq, listed_edges)


class DeBruijnGraph:
	def __init__(self):
		self.nodes = dict()  # type: dict[str, DeBruijnNode]

	def get_or_create_node(self, nodeseq: str) -> 'DeBruijnNode':
		if nodeseq not in self.nodes:
			self.nodes[nodeseq] = DeBruijnNode(nodeseq)
		return self.nodes[nodeseq]

	def add_isolated_edge(self, node: DeBruijnIsolatedEdge):
		from_node = self.get_or_create_node(node.prefix)
		to_node = self.get_or_create_node(node.suffix)

		if node.edgeseq not in from_node.edges:
			from_node.edges[node.edgeseq] = to_node
			from_node.edge_degree[node.edgeseq] = 0
		from_node.edge_degree[node.edgeseq] += 1


	@staticmethod
	def from_composition_graph(compgraph:CompositionGraph) -> 'DeBruijnGraph':
		new_graph = DeBruijnGraph()
		for isoedge in compgraph.edges:
			new_graph.add_isolated_edge(isoedge)
		return new_graph

	def __str__(self) -> str:
		str_form_list = list()
		for node in sorted(self.nodes.keys()):
			if len(self.nodes[node].edges) > 0:
				str_form_list.append("%s" % self.nodes[node])
		return "\n".join(str_form_list)


kmers = list()

for line in sys.stdin:  # type: str
	kmers.append(line.rstrip())

comp_graph = CompositionGraph.from_kmers(kmers)
debruijn_graph = DeBruijnGraph.from_composition_graph(comp_graph)
print("%s" % debruijn_graph)
