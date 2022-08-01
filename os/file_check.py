import os

print("A")

if __name__ == "__main__":
    temp = os.path.abspath("./")
    print(temp)
    file = os.listdir(temp)[0]
    try:
        print(os.listdir(file))
    except:
        print("exception occur")

print("C")