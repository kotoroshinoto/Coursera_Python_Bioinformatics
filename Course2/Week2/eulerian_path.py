import random
import sys
import re


class NodeEdge:
	def __init__(self, isource: int, idest: int, degree:int = 1):
		self.source = isource  #  type: int
		self.dest = idest  #  type: int
		self.degree = degree  #  type: int

	def __str__(self):
		if self.degree == 1:
			return "%d -> %d" % (self.source, self.dest)
		else:
			return "%d -> %d{%d}" % (self.source, self.dest, self.degree)

	def validate(self):
		assert (type(self.source) is int)
		assert (type(self.dest) is int)
		assert (type(self.degree) is int)


class NumberNode:
	def __init__(self, number: int):
		self.value = number  # type: int
		self.edges = dict()  # type: dict[int, NodeEdge]
		self.edge_keys = list()  # type: list[int]
		self.indegree = 0
		self.outdegree = 0

	def __str__(self):
		itercount = 0
		result = "%d -> " % self.value
		for edgeval in self.edges:
			# print("edgeval: %d; itercount: %d" % (edgeval, itercount))
			edge = self.edges[edgeval]  # type: NodeEdge
			for i in range(0, edge.degree):
				# print("i: %d" % i)
				result += "%d" % edge.dest
				if not(itercount + 1 == len(self.edges) and i + 1 == edge.degree):
					# print("adding a comma")
					# print("itercount+1 : %d, len(edges): %d \t i+1 : %d, edge.degree: %d" % ((itercount+1), len(self.edges), (i+1), edge.degree))
					result += ','
			itercount += 1
		return result

	def add_edge(self, edge: 'NodeEdge'):
		# degree = int(edge.degree)
		if edge.dest in self.edges:
			# print("adding %d to existing edge degree" % degree)
			self.edges[edge.dest].degree += edge.degree
		else:
			# print("creating new edge with degree %d" % degree)
			self.edges[edge.dest] = NodeEdge(edge.source, edge.dest, edge.degree)
			self.edge_keys.append(edge.dest)

	def validate(self):
		assert (type(self.value) is int)
		assert (type(self.edge_keys) is list)
		for item in self.edge_keys:
			assert (type(item) is int)
		assert (type(self.edges) is dict)
		for item in self.edges:
			assert (type(item) is int)
			assert (type(self.edges[item]) is NodeEdge)
			self.edges[item].validate()


class EulerianGraph:
	def __init__(self):
		self.nodes = dict()  # type: dict[int, NumberNode]
		self.node_keys = list()  # type: list[int]

	def get_unbalanced_nodes(self) -> 'list[NumberNode]':
		unbal = list()
		for node_value in self.node_keys:
			node = self.nodes[node_value]
			if node.indegree != node.outdegree:
				unbal.append(node.value)
		return unbal

	def get_node(self, value: int):
		return self.nodes[value]

	def get_edge(self, source: int, dest: int):
		return self.nodes[source].edges[dest]

	def ensure_node_exists(self, value: int):
		if value not in self.nodes:
			self.nodes[value] = NumberNode(value)
			self.node_keys.append(value)

	def add_edges(self, edge: NodeEdge):
		source = int(edge.source)
		dest = int(edge.dest)
		# degree = int(edge.degree)
		# print("adding edge %d -> %d [%d]" % (source, dest, degree))
		self.ensure_node_exists(source)
		self.ensure_node_exists(dest)
		self.nodes[source].add_edge(edge)
		self.nodes[source].outdegree += 1
		self.nodes[dest].indegree += 1

	def create_edge(self, source: int, dest: int):
		self.add_edges(NodeEdge(source, dest))

	def __str__(self):
		str_versions = list()
		for node in self.nodes:  # type: int
			str_versions.append(self.nodes[node].__str__())
		return "\n".join(str_versions)

	@classmethod
	def construct_from_edges(cls, edgelist: 'list[NodeEdge]') -> 'EulerianGraph':
		new_graph = EulerianGraph()
		for edge in edgelist:
			new_graph.add_edges(edge)
		return new_graph

	def validate_types(self):
		assert (type(self.node_keys) is list)
		for item in self.node_keys:
			assert (type(item) is int)
		assert (type(self.nodes) is dict)
		for item in self.nodes:
			assert (type(item) is int)
			assert (type(self.nodes[item]) is NumberNode)
			self.nodes[item].validate()


class UnexploredEdges:
	def __init__(self, graph: EulerianGraph):
		#object mapping to lists of unexplored edges for specific sources
		self.unexplored_edges = dict()  # type: dict[int, list[NodeEdge]]
		self.sources_w_unexplored_edges = list()  # type: list[int]
		self.traversal_count = dict()  # type: dict[NodeEdge, int]
		self.traversed_nodes_w_unexplored_edges = list()  # type: list[int]
		for source in graph.node_keys:
			if source not in self.sources_w_unexplored_edges:
				if len(graph.nodes[source].edge_keys) > 0:
					self.sources_w_unexplored_edges.append(source)
					self.unexplored_edges[source] = list()
			for dest in graph.nodes[source].edge_keys:
				edge_node = graph.get_edge(source, dest)
				self.unexplored_edges[source].append(edge_node)

	def has_unexplored_edges(self, source: int):
		return source in self.sources_w_unexplored_edges

	def get_random_source_w_unexplored_edges(self) -> int:
		return random.choice(self.sources_w_unexplored_edges)

	def get_traversed_source_w_unexplored_edges(self) -> int:
		return random.choice(self.traversed_nodes_w_unexplored_edges)

	def get_random_unexplored_edge_for_source(self, source: int) -> 'NodeEdge':
		if not (type(source) is int):
			print("attempted to provide non-integer %s of type %s" % (source, type(source)))
		return random.choice(self.unexplored_edges[source])

	def mark_traversal(self, edge: 'NodeEdge'):
		if edge not in self.traversal_count:
			self.traversal_count[edge] = 1
		else:
			self.traversal_count[edge] += 1
		# print("counted %d traversals of edge: %s" % (edge.degree, edge))
		# check if edge needs to be removed
		if self.traversal_count[edge] == edge.degree:
			self.unexplored_edges[edge.source].remove(edge)
			# check if source has no remaining unexplored edges (and thus needs to be removed)
			if len(self.unexplored_edges[edge.source]) == 0:
				self.unexplored_edges.pop(edge.source)
				self.sources_w_unexplored_edges.remove(edge.source)
				if edge.source in self.traversed_nodes_w_unexplored_edges:
					self.traversed_nodes_w_unexplored_edges.remove(edge.source)
			elif edge.source not in self.traversed_nodes_w_unexplored_edges:
				self.traversed_nodes_w_unexplored_edges.append(edge.source)
		elif edge.source not in self.traversed_nodes_w_unexplored_edges:
			if self.has_unexplored_edges(edge.source):
				self.traversed_nodes_w_unexplored_edges.append(edge.source)

	def __len__(self):
		return len(self.sources_w_unexplored_edges)


class EulerianPath:
	def __init__(self, graph: EulerianGraph):
		# list of edges, in order
		self.path = list()  # type: list[int]
		self.unexplored = UnexploredEdges(graph)
		# form a cycle Cycle by randomly walking in Graph (don't visit the same edge twice!)
		unbalanced = graph.get_unbalanced_nodes()
		start = None
		if len(unbalanced) == 0:
			start = self.unexplored.get_random_source_w_unexplored_edges()
		elif len(unbalanced) == 2:
			start = EulerianPath.select_start_node_from_unbalanced(unbalanced, graph)
		if start is None:
			self.path = None
			return
		self.path = self.random_walk(start)
		# print("initial cycle: %s" % self.__str__())
		# while there are unexplored edges in Graph
		while len(self.unexplored) > 0:
			# for edge in self.unexplored.unexplored_edges:
				# print("edge: %s" % edge)
			# 	select a node newStart in Cycle with still unexplored edges
			new_start = self.unexplored.get_traversed_source_w_unexplored_edges()
			new_cycle = self.random_walk(new_start)
			# print("->".join(str(x) for x in new_cycle))
			self.integrate_cycle(new_cycle)
			# print("integrated cycle: %s" % self.__str__())

		# 	form Cycle’ by traversing Cycle (starting at newStart) and then randomly walking

		# 	Cycle ← Cycle’
		# return Cycle

	@staticmethod
	def select_start_node_from_unbalanced(unbalnodes: 'list[int]', graph: EulerianGraph) -> int:
		for node in unbalnodes:
			node_obj = graph.nodes[node]
			if node_obj.indegree < node_obj.outdegree:
				return node
		return None

	def random_walk(self, start) -> 'list[int]':
		path = list()
		path.append(start)
		chosen_edge = self.unexplored.get_random_unexplored_edge_for_source(start)
		current_node = chosen_edge.dest
		# print("random walk start: %s" % chosen_edge)
		self.unexplored.mark_traversal(chosen_edge)
		path.append(current_node)
		while current_node != start and self.unexplored.has_unexplored_edges(current_node):
			chosen_edge = self.unexplored.get_random_unexplored_edge_for_source(current_node)
			current_node = chosen_edge.dest
			self.unexplored.mark_traversal(chosen_edge)
			path.append(current_node)
			# print("current node: %s" % chosen_edge)
		return path

	def integrate_cycle(self, path: 'list[int]'):
		if path[0] != path[-1]:
			contains_last = path[-1] in self.path
			# types of conditions
			# 1->2->3->1 inserting 1->4
			if not contains_last:
				if self.path[-1] != path[0]:
					print("Cannot find location to insert %s into %s", file=sys.stderr)
					return
				else:
					for i in range(1, len(path)):
						self.path.append(path[i])
			# 1->2->3->4 inserting 2->4->3
			else:
				for i in range(0, len(self.path)-1):
					#find position where x->y for inserting x->...->y
					if self.path[i] == path[0] and self.path[i+1] == path[-1]:
						for j in range(1, len(path)-1):
							self.path.insert(i+j, path[j])
		else:
			first_node = path[0]
			assert first_node in self.path
			for i in range(0, len(self.path)):
				if self.path[i] == first_node:
					# print("inserting path '%s' into position %d in path '%s'" % (EulerianPath.convert_int_list_to_path_string(path), i, EulerianPath.convert_int_list_to_path_string(self.path)))
					for j in range(1, len(path)):
						self.path.insert(i + j, path[j])
					return

	@staticmethod
	def convert_int_list_to_path_string(int_list: 'list[int]') -> str:
		str_list = list()
		for item in int_list:
			str_list.append(str(item))
		return "->".join(str_list)

	def __str__(self):
		return EulerianPath.convert_int_list_to_path_string(self.path)

edges = list()  # type: list[NodeEdge]
matcher = re.compile("^(\d+) -> ([0-9,]+)$")
for line in sys.stdin:  # type: str
	# print(line.rstrip())
	match_o = matcher.match(line.rstrip())
	list_of_numbers = match_o.group(2).split(",")
	for num in list_of_numbers:
		edges.append(NodeEdge(int(match_o.group(1)), int(num)))

graph = EulerianGraph.construct_from_edges(edges)  # type EulerianGraph
# print("%s\n" % graph)
graph.validate_types()
cycle = EulerianPath(graph)
print("%s" % cycle)

