class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_greater = [-1] * len(nums2)

        stack = []
        posi = defaultdict(int)
        for i in range(len(nums2)):
            posi[nums2[i]] = i
            while stack and nums2[i] > stack[-1][0]:
                prev_num, pos = stack.pop()
                nums2_greater[pos] = nums2[i]
            stack.append([nums2[i], i])
        
        res = []

        for i in range(len(nums1)):
            res.append(nums2_greater[posi[nums1[i]]])
        
        return res
        

        