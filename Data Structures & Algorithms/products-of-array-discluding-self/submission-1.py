# [1, 3, 4]
# [12, 4, 3]

# cases
# [0, 3, 4, 5] -> [60, 0, 0, 0]
# [0, 3, 4, 0] -> [0, 0, 0, 0]



class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zeroes_seen = 0

        for num in nums:
            if num == 0:
                zeroes_seen += 1
                if zeroes_seen == 2:
                    return [0] * len(nums)
                continue
            total_product *= num
        
        result = []

        for num in nums:
            if zeroes_seen > 0:
                if num != 0:
                    result.append(0)
                    continue
                else: 
                    result.append(total_product)
                    continue
            result.append(int(total_product / num))
        
        return result


        