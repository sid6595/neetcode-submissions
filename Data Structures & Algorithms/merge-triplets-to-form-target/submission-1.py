#given: list of list of ints
# each is a triplet
# target is the triplet we want to obtain

# perform repeated operation to try and get the target
# all numbers in triplet are positive

# examples
# [2,5,6],[1,4,4],[5,7,5] ; [5,4,6] -> false

# approach
# iterate through triplet one time and with beginning result as None
# add number to triplet if one or more numbers are equal to target and all others are less
# a number greater than target can't be added

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = None

        if not triplets:
            return False

        satisfy = True

        for triplet in triplets:
            new_result = [0] * 3
            for i in range(3):
                if triplet[i] > target[i]:
                    new_result = [0] * 3
                    break
                new_result[i] = triplet[i]
            
            if result:
                result = [max(result[0], new_result[0]), max(result[1], new_result[1]), max(result[2], new_result[2])]
            else:
                result = new_result
                
            
            

        


        if result and result == target:
            return True
        return False
        