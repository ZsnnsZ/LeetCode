def merge_sort(l):
	if len(l) <= 1:
		return l
	mid = len(l) / 2
	left = merge_sort(l[:mid])
	right = merge_sort(l[mid:])
	return merge(left, right)

def merge(left, right):
	i, j = 0, 0
	result = []
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result += left[i:]
	result += right[j:]
	return result

if __name__ == '__main__':
    l = [4, 1, 34, 26, 10, 3, 7, 32]
    print merge_sort(l)
