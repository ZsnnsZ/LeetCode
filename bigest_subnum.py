def bigest_subnum(l):
	this_num = 0
	max_num = 0
	for i in range(len(l)):
		this_num = max(this_num+l[i], 0)
		if this_num > max_num:
			max_num = this_num
	return max_num

if __name__ == '__main__':
	l = [4,-3,5,-2,-1,2,6,-2]
	print bigest_subnum(l)
