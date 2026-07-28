class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 1)
        postfix = [1] * (len(nums) + 1)

        output = []

        # prefix
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] * nums[i]
        
        #postfix
        for i in range(len(nums) - 1, -1, -1):
            postfix[i-1] = postfix[i] * nums[i]
        
        for i, num in enumerate(nums):
            output.append(prefix[i] * postfix[i])
        
        return output

        