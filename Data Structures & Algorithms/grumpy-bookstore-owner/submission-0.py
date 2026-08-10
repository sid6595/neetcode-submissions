# fixed interval sliding window
# at each interval, how does this affect the number of total satisfied customers

# calculate satisfied customers for each interval : O(n^2)
# prefix sums? 

# how do we only do the calculations once

# calculate prefix and postfix from each point using the grumpy metrics
# sum the prefix from beginning of window, actual from the window, and postfix from end of window


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        prefix, postfix = [0] * len(customers), [0] * len(customers)

        # [1, 0, 1]  # [0, 0, 0]
        # [0, 1, 1], [1, 1, 0]

        # generate prefix sums, we want the total before index i
        for i in range(1, len(customers)):
            prefix[i] = prefix[i-1] - customers[i-1] * (grumpy[i-1] - 1)

        # generate postfix sums, we want the total after index i
        for i in range(len(customers)-2, -1, -1):
            postfix[i] = postfix[i+1] - customers[i+1] * (grumpy[i+1] - 1)
        
        # now let's go through each window and track best
        best = 0
        l, r = 0, minutes - 1

        while r < len(customers):
            window_sum = 0
            for i in range(l, r+1):
                window_sum += customers[i]
            best = max(best, prefix[l] + window_sum + postfix[r])
            r += 1
            l += 1
        
        return best

        