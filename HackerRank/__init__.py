import re


class Operation:
    def __init__(self):
        example_list = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
        number = 2
        # print(self.lsitOfList(example_list, number))\
        a = [2, 5, 5, 15]
        result = self.ProblemArray(a, 7)
        print(result)

    def solve(self):
        print("In solve Method")
        arr = [-4, 3, -9, 0, 4, 1]
        count_negative = []
        count_positive = []
        count_zero = []
        size = len(arr)
        for i in arr:
            if i < 0:
                count_negative.append(i)

            if i == 0:
                count_zero.append(i)
            if i > 0:
                count_positive.append(i)

        print("Negative is {}".format(len(count_negative) / size))
        print("Zero is {}".format(len(count_zero) / size))
        print("Positive is {}".format(len(count_positive) / size))

    def findDiagonalSum(self):
        data = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
        size = len(data)
        for x in range(0, len(data)):
            d = (data[x][x])
            # print(d)

        for i in range(0, len(data)):
            d1 = data[i][size - 1 - x]
            # print(d1)

        ans = d - d1
        # print(ans)

        print(sum(data[x][x] for x in range(0, len(data))))
        print(sum(data[x][-1 * (x + 1)] for x in range(0, len(data))))
        print(abs(d - d1))

    def additionOFMertrics(self):
        # X = [[1, 2, 3],
        #      [4, 5, 6],
        #      [7, 8, 9]]
        #
        # Y = [[9, 8, 7],
        #      [6, 5, 4],
        #      [3, 2, 1]]
        #
        # result = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
        #
        # for i in result:
        #     print(i)

        arr = [1, 2, 3, 4, 5, 6, 7]
        size = len(arr)
        k = 3
        temp = []
        i = 0
        while i < k:
            temp.append(arr[i])
            i = i + 1

        print(temp)
        i = 0
        while k < size:
            arr[i] = arr[k]
            i = i + 1
            k = k + 1

        print(arr[:i] + temp)

    def primeFactor(self):
        input = 630
        factor = list()
        divider = 2
        while divider <= input:
            if input % divider == 0:
                factor.append(divider)
                input = input / divider
            else:
                divider += 1

        print(factor)

    def palindrome(self):
        inputData = "hell ok"
        forwordString = ''.join(re.findall(r'[a-z]+', inputData.lower()))
        backword = forwordString[::-1]
        print(forwordString)
        print(backword)
        if forwordString == backword:
            flag = True
        else:
            flag = False

        print(flag)

    def sortString(self):
        data = "banana ORANGE apple"
        words = data.split()

        words = [w.lower() + w for w in words]
        words.sort()

        words = [w[len(w) // 2:] for w in words]

    def lsitOfList(self, example_list, number):
        List = list()
        for i in range(len(example_list)):
            if example_list[i] == number:
                List.append([i])
            elif isinstance(example_list[i], list):
                for index in self.lsitOfList(example_list[i], number):
                    List.append([i] + index)
        return List

    def ProblemArray(self, nums: list[int], target: int) -> list[int]:
        print("In Function")
        print(nums)

        seen = {}

        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            elif num not in seen:
                seen[num] = i

        #for i in range(len(nums)-1):
         #   for j in range(i+1, len(nums)):
          #      if nums[i] + nums[j] == target:
           #         return [i, j]




if __name__ == "__main__":
    op = Operation()
