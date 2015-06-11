__author__ = 'mgooch'
def PatternCount(text, pattern):
	count = 0
	for i in range(0, len(text)-len(pattern) + 1):
		if text[i:i+len(pattern)] == pattern:
			count += 1
	return count
def FrequentWords(text, k):
	frequentPatterns = []
	unique_patterns = {}
	maxCount = 0
	for i in range(0, len(text) - k + 1):
		pattern = text[i: i + k]
		if pattern not in unique_patterns:
			unique_patterns[pattern] = PatternCount(text, pattern)
			if unique_patterns[pattern] > maxCount:
				maxCount = unique_patterns[pattern]
	for pattern in unique_patterns:
		if unique_patterns[pattern] == maxCount:
			frequentPatterns.append(pattern)
	return frequentPatterns
def ReverseComplement(pattern):
	revcomp = pattern[::-1]
	revcomp=revcomp.translate(str.maketrans("GATCgatc", "CTAGctag"))
	return revcomp
def PatternSearch(pattern, genome):
	positions=[]
	i = genome.find(pattern)
	while(i != -1):
		positions.append(i)
		i = genome.find(pattern, i + 1)
	return positions
