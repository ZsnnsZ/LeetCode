def insert_sort1(l):
	for i in range(1, len(l)):
		tmp = l[i]
		j = i - 1
		# while j >= 0:
		# 	if l[j] > tmp:
		# 		l[j+1] = l[j]
		# 		l[j] = tmp
		# 	else:
		# 		break
		# 	j -= 1
		# print l

		while j >= 0 and l[j] > tmp:
			l[j+1] = l[j]
			j -= 1
		l[j+1] = tmp
		print l

		# for j in range(i, -1, -1):
		# 	if l[j-1] > tmp:
		# 		l[j] = l[j-1]				
		# 	else:
		# 		break
		# l[j] = tmp
		# print l

		# for j in range(i, 0, -1):
		# 	if l[j-1] > tmp:
		# 		l[j] = l[j-1]
		# 		l[j-1] = tmp				
		# 	else:
		# 		break
		# print l
	return l

if __name__ == '__main__':
	l = [34,4,15,26,10,3,7,32]
	insert_sort1(l)