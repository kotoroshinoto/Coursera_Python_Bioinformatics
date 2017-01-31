import sys


def construct_universal_dict(ksize: int) -> dict:
	str_queue = list()
	str_queue.append('0')
	str_queue.append('1')
	for i in range(0, ksize-1):
		curr_items = len(str_queue)
		for y in range(0, curr_items):
			item = str_queue.pop(0)
			str_queue.append(item + '0')
			str_queue.append(item + '1')
	univ_dict = dict()
	for item in str_queue:
		univ_dict[item] = 0
	return univ_dict


def explode_into_kmers(binstr: str, ksize: int):
	result = list()
	for i in range(0, len(binstr)-ksize+1):
		# print("found kmer %s" % binstr[i:i+ksize])
		result.append(binstr[i:i+ksize])
	return result


def count_kmer_list(kmerlist: list, kmersize) -> dict:
	univ_dict_counter = construct_universal_dict(kmersize)
	for item in kmerlist:
		# print("found kmer %s" % item)
		univ_dict_counter[item] += 1
	return univ_dict_counter


def is_universal_binary_string(binstr, ksize):
	kmer_list = explode_into_kmers(binstr, ksize)
	univ_dict_counts = count_kmer_list(kmer_list, ksize)
	for item in univ_dict_counts:
		# print("%s : %d" % (item, univ_dict_counts[item]))
		if univ_dict_counts[item] != 1:
			return False
	return True

kmersize = int(sys.stdin.readline().rstrip())

for line in sys.stdin:
	binstr = line.rstrip()
	if binstr != "":
		print("%s : %s" % (binstr, is_universal_binary_string(binstr, 3)))

