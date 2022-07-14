if __name__ == "__main__":
    set1 = set([1,2,2,2,3,4])
    print(set1)
    set2 = {1,2,2,2,2,3}
    print(set2)
    set2.add(3)
    set2.add(8)
    set2.remove(2)
    print(set2)
