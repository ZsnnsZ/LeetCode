def shell_sort(l):
	step = len(l)/2
	while step > 0:
		for i in range(step, len(l)):
			while i >= step and l[i-step] > l[i]:
				l[i], l[i-step] = l[i-step], l[i]
				i -= step
		step = step/2
		print l
	return l

if __name__ == '__main__':
	l = [4,1,34,26,10,3,7,32]
	shell_sort(l)