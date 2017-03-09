import math
def radix_sort(l, radix=10):
    # ceil(x),This is the smallest integral value >= x.
    k = int(math.ceil(math.log(max(l), radix)))
    print k
    bucket = [[] for i in range(radix)]
    for i in range(1, k+1):
        for j in l:
            bucket[j/(radix**(i-1)) % (radix**i)].append(j)
        del l[:]
        for z in bucket:
            l += z
            del z[:]
        print l
    return l

if __name__ == '__main__':
    l = [34,4,15,26,10,3,7,32]
    radix_sort(l)