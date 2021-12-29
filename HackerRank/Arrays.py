class ArrayPractice(object):
    def __init__(self):
        pass

    def duplicates(self, arr, N):
        print("In Array")
        for i in range(0, N):
            print(arr[i])


if __name__ == "__main__":
    arr = [0, 3, 1, 2]
    N = 4
    obj = ArrayPractice()
    obj.duplicates(arr, N)
