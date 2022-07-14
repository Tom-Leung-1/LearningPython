class Node:
    def __init__(self, val):
        self.val = val

if __name__ == "__main__":
    arr = [1, 5, 2, 0, 23]
    arr.sort()
    print(arr)
    arr2 = [14, 2, 66, 23, 1]
    arr3 = sorted(arr2, reverse=True)
    print(arr2)
    print("descending", arr3)
    # custom sort
    # descending
    descending_list = sorted(arr2, key=lambda x: -x)
    # sort objects
    arr4 = [Node(2), Node(21), Node(12), Node(3), Node(45), Node(33)]
    sorted_node = sorted(arr4, key=lambda x: x.val) # Sort with key
    print("descending", descending_list)
    for x in sorted_node:
        print(x.val)