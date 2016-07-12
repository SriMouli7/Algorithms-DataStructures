# Implemented
#   -MAX_HEAPIFY
#   -BUILD_MAX_HEAP
#   -HEAP_SORT

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def parent(i):
    return i // 2


def max_heapify(A,i):
    l = left(i)
    # print 'left(%d) - %d' %(i,l)
    r = right(i)
    # print 'right(%d) - %d' %(i,r)
    if l < len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        max_heapify(A,largest)

def build_max_heap(A):
    for i in range(len(A)//2 - 1, -1, -1):
        max_heapify(A,i)
    # print 'After build_max_heap'
    # print A


def heap_sort(A,l):
    build_max_heap(A)
    for i in range(l):
        # last = len(A)
        # temp = A[0]
        # A[0] = A[last-1]
        # A[last-1] = temp
        # print A[last-1]
        # A.remove(A[last-1])
        # if l>=0:
        #     max_heapify(A,0)
        print extract_max(A)


def extract_max(A):
    max = A[0]
    A[0] = A[len(A)-1]
    A[len(A) - 1] = max
    A.remove(max)
    max_heapify(A,0)
    # print A
    return max

A = [5,2,4,6,1,3]


# print "Before MAx_heapify"
# print A
# max_heapify(A,1)
# print "After Max_heapify"
# print A
# print "Before Build"
# print A
# build_max_heap(A)
# print "After Heap"
# print A
# build_max_heap(A)
# for i in range(0,len(A)):
#     print extract_max(A)

print 'Before Sort'
print A
heap_sort(A,len(A))
print "After heap sort"
print A
