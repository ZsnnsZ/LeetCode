def bubble_sort(l):
	for i in range(len(l)):
		for j in range(i+1, len(l)):
			if l[i] > l[j]:
				l[i], l[j] = l[j], l[i]
		print l
	return l

if __name__ == '__main__':
	l = [34,4,15,26,10,3,7,32]
	bubble_sort(l)