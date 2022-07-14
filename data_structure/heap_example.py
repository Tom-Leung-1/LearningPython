import heapq

class Node:
    def __init__(self, val):
        self.val = val

if __name__ == "__main__":
    print("------")
    min_heap = [16,2, 4, 9, 1]
    heapq.heapify(min_heap) # min heap
    heapq.heappush(min_heap, 15)
    while len(min_heap):
        print(min_heap)
        print(heapq.heappop(min_heap))
    print("------")
    max_heap = [6, 2, 8, 1, 10]
    max_heap = [-x for x in max_heap]
    heapq.heapify(max_heap)
    heapq.heappush(max_heap, -100)
    while len(max_heap):
        print(max_heap) # values are to be inverted
        print(-heapq.heappop(max_heap))
    print("-------")
    list = [Node(1), Node(19), Node(2), Node(7)]
    heap_elts = [(item.val, item) for item in list]
    heapq.heapify(heap_elts)  # you specifically asked about heapify, here it is!
    while len(heap_elts) > 0:
        print(heapq.heappop(heap_elts)[1].val)  # element 1 is the original tuple


