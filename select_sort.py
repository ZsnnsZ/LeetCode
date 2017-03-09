def select_sort(l):
	for i in range(len(l)):
		min_index = i
		for j in range(i+1, len(l)):
			if l[min_index] > l[j]:
				min_index = j
		l[min_index], l[i] = l[i], l[min_index]
		print l
	return l

if __name__ == '__main__':
	l = [34,4,15,26,10,3,7,32]
	select_sort(l)