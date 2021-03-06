__author__ = 'mgooch'


def PatternCount(text, pattern):
	count = 0
	for i in range(0, len(text) - len(pattern) + 1):
		if text[i:i + len(pattern)] == pattern:
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
	revcomp = revcomp.translate(str.maketrans("GATCgatc", "CTAGctag"))
	return revcomp


def PatternSearch(pattern, genome):
	positions = []
	i = genome.find(pattern)
	while (i != -1):
		positions.append(i)
		i = genome.find(pattern, i + 1)
	return positions


def PatternToNumber(pattern):
	return int(pattern.translate(str.maketrans("ACGT", "0123")), 4)


def NumberToPattern(number, k):
	num = number
	pattern = []
	while num != 0:
		remainder = num % 4  # assume K > 1
		num = num // 4  # integer division
		pattern.insert(0, "%d" % remainder)
	while len(pattern) < k:
		pattern.insert(0, '0')
	pattern = "".join(pattern)
	pattern = pattern.translate(str.maketrans("0123", "ACGT"))
	return pattern


def ComputingFrequencies(text, k):
	FrequencyArray = []
	for i in range(0, 4 ** k):
		FrequencyArray.append(0)
	for i in range(0, (len(text) - k + 1)):
		Pattern = text[i:(i + k)]
		j = PatternToNumber(Pattern)
		FrequencyArray[j] += 1
	return FrequencyArray


def FasterFrequentWords(text, k):
	FrequentPatterns = []
	FrequencyArray = ComputingFrequencies(text, k)
	maxCount = max(FrequencyArray)
	for i in range(0, 4 ** k):
		if FrequencyArray[i] == maxCount:
			Pattern = NumberToPattern(i, k)
			FrequentPatterns.append(Pattern)
	return FrequentPatterns


def ClumpFinding(genome, k, L, t):
	FrequentPatterns = []
	Clump = []
	for i in range(0, 4 ** k):
		Clump.append(0)
	for i in range(0, len(genome) - L + 1):
		text = genome[i:(i + L)]
		FrequencyArray = ComputingFrequencies(text, k)
		for j in range(0, 4 ** k):
			if FrequencyArray[j] >= t:
				Clump[j] = 1
	for i in range(0, 4 ** k):
		if Clump[i] == 1:
			Pattern = NumberToPattern(i, k)
			FrequentPatterns.append(Pattern)
	return FrequentPatterns


def BetterClumpFinding(genome, k, L, t):
	FrequentPatterns = []
	Clump = []
	for i in range(0, 4 ** k):
		Clump.append(0)
	text = genome[0:L]
	FrequencyArray = ComputingFrequencies(text, k)
	for i in range(0, 4 ** k):
		if FrequencyArray[i] >= t:
			Clump[i] = 1
	for i in range(1, len(genome) - L + 1):
		# Genome(i − 1, k)
		FirstPattern = genome[(i - 1):(i - 1 + k)]
		# print("First Pattern: %s" % FirstPattern)
		j = PatternToNumber(FirstPattern)
		FrequencyArray[j] -= 1
		# Genome(i + L − k, k)
		LastPattern = genome[(i + L - k):(i + L)]
		# print("Last Pattern: %s" % LastPattern)
		j = PatternToNumber(LastPattern)
		FrequencyArray[j] += 1
		if FrequencyArray[j] >= t:
			Clump[j] = 1
	for i in range(0, 4 ** k):
		if Clump[i] == 1:
			Pattern = NumberToPattern(i, k)
			FrequentPatterns.append(Pattern)
	return FrequentPatterns


# FindingFrequentWordsBySorting(Text , k)
#         FrequentPatterns ← an empty set
#         for i ← 0 to |Text| − k
#             Pattern ← Text(i, k)
#             Index(i) ← PatternToNumber(Pattern)
#             Count(i) ← 1
#         SortedIndex ← Sort(Index)
#         for i ← 1 to |Text| − k
#             if SortedIndex(i) = SortedIndex(i − 1)
#                 Count(i) = Count(i − 1) + 1
#         maxCount ← maximum value in Count
#         for i ← 0 to |Text| − k
#             if Count(i) = maxCount
#                 Pattern ← NumberToPattern(SortedIndex(i), k)
#                 add Pattern to the set FrequentPatterns
#         return FrequentPatterns
def Skew(genome):
	skew = 0
	genomeskew = []
	for i in range(0, len(genome)):
		genomeskew.append(skew)
		if genome[i] == 'G':
			skew += 1
		elif genome[i] == 'C':
			skew -= 1
	genomeskew.append(skew)
	return genomeskew


def MinimumSkew(genome):
	skewlist = Skew(genome)
	minimum = min(skewlist)
	# print(minimum)
	min_indexes = []
	for i in range(0, len(skewlist)):
		if (skewlist[i] == minimum):
			min_indexes.append(i)
	return min_indexes


def HammingDistance(seq1, seq2):
	assert (len(seq1) == len(seq2))
	hamdist = 0
	for i in range(0, len(seq1)):
		if (seq1[i] != seq2[i]):
			hamdist += 1
	return hamdist


def ApproximatePatternSearch(pattern, genome, d):
	positions = []
	for i in range(0, len(genome) - len(pattern) + 1):
		pattern2 = genome[i:i + len(pattern)]
		if HammingDistance(pattern, pattern2) <= d:
			positions.append(i)
	return positions


def ApproximatePatternCount(genome, pattern, d):
	count = 0
	for i in range(0, len(genome) - len(pattern) + 1):
		pattern2 = genome[i:i + len(pattern)]
		if HammingDistance(pattern, pattern2) <= d:
			count += 1
	return count


# def ComputingApproximateFrequencies(text, k, d):
# 	FrequencyArray = []
# 	for i in range (0, 4 ** k):
# 		FrequencyArray.append(0)
# 	for i in range(0, (len(text) - k + 1)):
# 		Pattern = text[i:(i + k)]
# 		for j in range(0, 4 ** k):
# 			Pattern2 = NumberToPattern(j,k)
# 			if(HammingDistance(Pattern,Pattern2) <= d):
# 				FrequencyArray[j] += 1
# 	return FrequencyArray
def FrequentApproximateWords(text, k, d):
	FrequentPatterns = []
	possiblePatternCounts = []
	for i in range(0, 4 ** k):
		pattern = NumberToPattern(i, k)
		possiblePatternCounts.append(ApproximatePatternCount(text, pattern, d))
	maxCount = max(possiblePatternCounts)
	for i in range(0, 4 ** k):
		if possiblePatternCounts[i] == maxCount:
			Pattern = NumberToPattern(i, k)
			FrequentPatterns.append(Pattern)
	return FrequentPatterns


def FrequentApproximateSequences(text, k, d):
	FrequentPatterns = []
	possiblePatternCounts = []
	seen = {}
	for i in range(0, 4 ** k):
		possiblePatternCounts.append(0)
	for i in range(0, 4 ** k):
		pattern = NumberToPattern(i, k)
		patternRC = ReverseComplement(pattern)
		if not (pattern in seen or patternRC in seen):
			seen[pattern] = 1
			count = ApproximatePatternCount(text, pattern, d)
			countRC = 0
			if pattern != patternRC:
				seen[patternRC] = 1
				countRC = ApproximatePatternCount(text, patternRC, d)
			possiblePatternCounts[i] = (count + countRC)
			if pattern != patternRC:
				possiblePatternCounts[PatternToNumber(patternRC)] = (count + countRC)
	maxCount = max(possiblePatternCounts)
	for i in range(0, 4 ** k):
		if possiblePatternCounts[i] == maxCount:
			Pattern = NumberToPattern(i, k)
			FrequentPatterns.append(Pattern)
	return FrequentPatterns


def Neighbors(Pattern, d):
	bases = ['A', 'C', 'G', 'T']
	if d == 0:
		return Pattern
	if len(Pattern) == 1:
		return bases
	Neighborhood = []
	SuffixNeighbors = Neighbors(Pattern[1:], d)
	for Text in SuffixNeighbors:
		if HammingDistance(Pattern[1:], Text) < d:
			for nucleotide in bases:
				Neighborhood.append("%s%s" % (nucleotide, Text))
		else:
			Neighborhood.append("%s%s" % (Pattern[0], Text))
	return Neighborhood


def ContainsApproximatePattern(genome, pattern, d):
	count = 0
	for i in range(0, len(genome) - len(pattern) + 1):
		pattern2 = genome[i:i + len(pattern)]
		if HammingDistance(pattern, pattern2) <= d:
			return True
	return False


def MotifEnumeration(dna, k, d):
	kmer_patterns = []
	neighbor_patterns = []
	patterns = []
	kmer_seen = {}
	neighbor_seen = {}
	# for each k-mer Pattern in Dna
	# GENERATE list of k-mers in dna kmer_patterns
	# print("\n\nGenerating initial k-mers")
	for seq in dna:
		print("current sequence: %s" % seq)
		for i in range(0, len(seq) - k + 1):
			pattern = seq[i:i + k]  # for instance seq of length 12 kmer size 9 at position 2
			print("current pattern: %s" % pattern)
			if pattern not in kmer_seen:
				# print("added pattern: %s" % pattern)
				kmer_seen[pattern] = 1
				kmer_patterns.append(pattern)

	for kmer in kmer_patterns:
		# check neighbors
		# for each k-mer Pattern’ differing from Pattern by at most d mismatches
		neighbors = Neighbors(kmer, d)
		# generate neighbors of existing kmer_patterns
		for neighbor in neighbors:
			# print("\tcurrent neighbor: %s" % neighbor)
			if neighbor not in neighbor_seen:
				# print("\tadded neighbor: %s" % neighbor)
				neighbor_seen[neighbor] = 1
				neighbor_patterns.append(neighbor)
		if kmer not in neighbor_seen:
			neighbor_seen[kmer] = 1
			neighbor_patterns.append(kmer)
	# for each kmer-pattern neighbor in dna:
	for kmer in neighbor_patterns:
		success = True
		# if Pattern' appears in each string from Dna with at most d mismatches
		for seq in dna:
			if not ContainsApproximatePattern(seq, kmer, d):
				success = False
				break
		if success:
			# add Pattern' to Patterns
			patterns.append(kmer)
	return sorted(patterns)


def CountMotifs(motifs):
	counts = {'A': [], 'G': [], 'C': [], 'T': []}
	Bases = ['A', 'C', 'G', 'T']
	for base in Bases:
		for i in range(0, len(motifs[0])):
			counts[base].append(0)
	for motif in motifs:
		for i in range(0, len(motif)):
			counts[motif[i]][i] += 1
	return counts


def ProfileMotifs(motifs):
	counts = CountMotifs(motifs)
	for base in counts:
		for i in range(0, len(motifs[0])):
			counts[base][i] = float(counts[base][i]) / float(len(motifs))
	return counts


def Consensus(motifs):
	counts = CountMotifs(motifs)
	consensus = []
	Bases = ['A', 'C', 'G', 'T']
	countdict = {}
	for i in range(0, len(motifs[0])):
		countdict['A'] = counts['A'][i]
		countdict['C'] = counts['C'][i]
		countdict['G'] = counts['G'][i]
		countdict['T'] = counts['T'][i]
		consensus.append(max(countdict.keys(), key=lambda k: countdict[k]))
		# print("max value %d for base: %s" % (counts[consensus[i]][i], consensus[i]))
	return "".join(consensus)

def Entropy(motifs):
	import math
	profile = ProfileMotifs(motifs)
	logsum = 0.0
	# print("")
	for i in range(0, len(motifs[0])):
		for base in profile:
			if profile[base][i] != 0:
				logsum += -1 * (profile[base][i] * math.log(profile[base][i], 2))
	return logsum

def MotifHammingDistance(pattern, motifs):
	score = 0
	# print("HAMMINGDISTANCE:")
	for motif in motifs:
		# print("\tmotif: %s" % motif)
		score += HammingDistance(pattern, motif)
	return score

def ScoreMotifs(motifs):
	return MotifHammingDistance(Consensus(motifs), motifs)

def DistanceBetweenPatternAndStrings(Pattern, Dna):
	k = len(Pattern)
	distance = 0
	for Text in Dna:
		hammingdistance = float('+inf')
		# for each k-mer Pattern’ in Text
		for i in range(0, len(Text) - k + 1):
			Pattern_ = Text[i:i + k]
			hdist = HammingDistance(Pattern, Pattern_)
			if hammingdistance > hdist:
				hammingdistance = hdist
		distance += hammingdistance
	return distance

def MedianString(dna, k):
	distance = float('+inf')
	median = ""
	for i in range(0, 4 ** k):
		pattern = NumberToPattern(i, k)
		patstrdist = DistanceBetweenPatternAndStrings(pattern, dna)
		if distance > patstrdist:
			distance = patstrdist
			median = pattern
	return median

def SeqProbabilityProfile(sequence, profile):
	prob = 1.0
	for i in range(0, len(sequence)):
		base = sequence[i]
		prob *= profile[base][i]
	return prob

def ProfileProbableKmer(dna, k, profile):
	seen = {}
	probseq = ""
	probval = -0.1
	# print("scanning %s |%d| for kmers of size %d" % (dna, len(dna), k))
	for i in range(0, len(dna) - k + 1):
		# print("i: %d, i+ k: %d" % (i, i + k))
		pattern = dna[i:i + k]
		if pattern not in seen:
			# print("new pattern: %s" % pattern)
			seen[pattern] = 1
			prob = SeqProbabilityProfile(pattern, profile)
			if prob > probval :
				probval = prob
				probseq = pattern
	return probseq

def GreedyMotifSearch(dna, k, t):
	bestmotifs = []
	firstseq_motifs = []
	for seq in dna:
		bestmotifs.append(seq[0:k])

	for i in range(0,len(dna[0]) - k + 1):
		firstseq_motifs.append(dna[0][i:i+k])
		# print("appending motif: %s" % firstseq_motifs[i])
	for motif in firstseq_motifs:
		motifs = []
		motifs.append(motif)
		for i in range(1, t):
			motifsprofile = ProfileMotifs(motifs)
			motifs.append(ProfileProbableKmer(dna[i], k, motifsprofile))
		# print("best motifs:\n%s" % "\n".join(bestmotifs))
		# print("current motifs:\n%s" % "\n".join(motifs))
		if ScoreMotifs(motifs) < ScoreMotifs(bestmotifs):
			bestmotifs = motifs
	return bestmotifs

def ProfileMotifsLaplace(motifs):
	counts = CountMotifs(motifs)
	# for base in counts:
	# 	print("%s: " % base, end="")
	# 	for i in range(0, len(counts[base])):
	# 		print("%d" % counts[base][i], end="\t")
	# 	print("")

	for base in counts:
		for i in range(0, len(motifs[0])):
			counts[base][i] = float(counts[base][i]+1) / float(len(motifs)+2)
	return counts

def GreedyMotifSearchLaplace(dna, k, t):
	bestmotifs = []
	firstseq_motifs = []
	for seq in dna:
		bestmotifs.append(seq[0:k])

	for i in range(0,len(dna[0]) - k + 1):
		firstseq_motifs.append(dna[0][i:i+k])
		# print("appending motif: %s" % firstseq_motifs[i])
	for motif in firstseq_motifs:
		motifs = []
		motifs.append(motif)
		for i in range(1, t):
			motifsprofile = ProfileMotifsLaplace(motifs)
			motifs.append(ProfileProbableKmer(dna[i], k, motifsprofile))
		# print("best motifs:\n%s" % "\n".join(bestmotifs))
		# print("current motifs:\n%s" % "\n".join(motifs))
		if ScoreMotifs(motifs) < ScoreMotifs(bestmotifs):
			bestmotifs = motifs
	return bestmotifs

def MotifsFromProfile(profile, dna):
	motifs = []
	for seq in dna:
		motifs.append(ProfileProbableKmer(seq, len(profile['A']), profile))
	return motifs

import random


def RandomKmersFromSequences(dna, k):
	kmers = []
	for seq in dna:
		i = random.randint(0, len(seq) - k)
		kmer = seq[i:i+k]
		kmers.append(kmer)
	return kmers


def RandomizedMotifSearch(dna, k, t):
	motifs = RandomKmersFromSequences(dna, k)
	bestmotifs = motifs
	bestScore = ScoreMotifs(bestmotifs)
	while True:
		profile = ProfileMotifsLaplace(motifs)
		motifs = MotifsFromProfile(profile, dna)
		score = ScoreMotifs(motifs)
		if score < bestScore:
			bestmotifs = motifs
			bestScore = score
		else:
			return [bestmotifs, bestScore]


def RandomizedMotifSearchBestOfN(dna, k, t, n):
	(bestmotifs, bestscore) = RandomizedMotifSearch(dna, k, t)
	for j in range(1, n):
		(motifs, score) = RandomizedMotifSearch(dna, k, t)
		if score < bestscore:
			bestmotifs = motifs
			bestscore = score
	return bestmotifs

def RandomKmersFromSequence(seq, k):
	i = random.randint(0, len(seq) - k)
	kmer = seq[i:i+k]
	return kmer

def SeqKmerProbability(seq, k, profile):
	probability = []
	for i in range(0, len(seq) - k + 1):
		kmer = seq[i:i+k]
		probability.append(SeqProbabilityProfile(kmer, profile))
	return probability
import numpy

def GibbsRandomKmer(seq, profile, k):
	kmerprob = SeqKmerProbability(seq, k, profile)
	probsum = 0
	for prob in kmerprob:
		probsum += prob
	for i in range(0, len(kmerprob)):
		kmerprob[i] /= probsum
	i = numpy.random.choice(len(kmerprob), p=kmerprob)
	return seq[i:i+k]

def GibbsSampler(dna, k, t, n):
	motifs = RandomKmersFromSequences(dna, k)
	bestmotifs = list(motifs)
	for j in range(0, n):
		# print("Starting motifs:\n%s\n" % "\n".join(motifs))
		i = random.randint(0, t-1)
		# print("i: %d" % i)
		motifi = motifs[i]
		motifs.pop(i)
		# print("truncated motifs:\n%s\n" % "\n".join(motifs))
		profile = ProfileMotifsLaplace(motifs)
		motifi = GibbsRandomKmer(dna[i], profile, k)
		motifs.insert(i, motifi)
		# print("new motifs:\n%s\n" % "\n".join(motifs))
		if ScoreMotifs(motifs) < ScoreMotifs(bestmotifs):
			bestmotifs = list(motifs)
	return bestmotifs