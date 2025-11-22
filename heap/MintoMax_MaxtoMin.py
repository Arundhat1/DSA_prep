import heapq
def max_to_min_heap(max_heap):
    min_heap = [-x for x in max_heap]
    heapq.heapify(min_heap)
    return min_heap


def min_to_max_heap(min_heap):
    # min_heap is already heapified
    max_heap = [-x for x in min_heap]
    heapq.heapify(max_heap)
    return max_heap
