def build_heap(l, size):
    for i in range(0, size / 2)[::-1]:
        adjust_heap(l, i, size)


def adjust_heap(l, i, size):
    lt = 2 * i + 1
    rt = 2 * i + 2
    max_ = i
    if i < size / 2:
        if lt < size and l[lt] > l[max_]:
            max_ = lt
        if rt < size and l[rt] > l[max_]:
            max_ = rt
        if max_ != i:
            l[max_], l[i] = l[i], l[max_]
            adjust_heap(l, max_, size)


def heap_sort(l):
    size = len(l)
    build_heap(l, size)
    for i in range(0, size)[::-1]:
        l[0], l[i] = l[i], l[0]
        adjust_heap(l, 0, i)
    	print l

if __name__ == '__main__':
    l = [4, 1, 34, 26, 10, 3, 7, 32]
    heap_sort(l)
