class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []

        for index, number in enumerate(nums):
            A.append([number, index])

        A.sort()

        start, end = 0, len(nums) - 1
        while start < end:
            sum = A[start][0] + A[end][0]
            print(sum)
            if sum < target:
                print("a", sum)
                start += 1
            elif sum > target:
                print("b", sum)
                end -= 1
            else:
                print("c", sum)
                return [min(A[start][1], A[end][1]), max(A[start][1], A[end][1])]
        