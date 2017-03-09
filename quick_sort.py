# def quick_sort(l, left, right):
#     if left >= right:
# 		return l
#     key = l[left]
#     low = left
#     high = right
#     while left < right:
#         while left < right and l[right] >= key:
#             right -= 1
#         l[left] = l[right]
#         while left < right and l[left] <= key:
#             left += 1
#         l[right] = l[left]
#     l[right] = key
#     # print l
#     quick_sort(l, low, left - 1)
#     quick_sort(l, left + 1, high)
#     return l
def quick_sort(l, left, right):
	if left >= right:
		return
	else:
		key = partition(l, left, right)
		quick_sort(l, left, key)
		quick_sort(l, key+1, right)

def partition(l, left, right):
	i = left - 1
	for j in range(left, right):
		if l[j] <= l[right]:
			i += 1
			l[i], l[j] = l[j], l[i]
	l[i+1], l[right] = l[right], l[i+1]
	return i

if __name__ == '__main__':
    l = [34,4,15,26,10,3,7,32]
    quick_sort(l, 0, len(l)-1)
    print l
