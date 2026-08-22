# at each stage which possible project generates the most profit
# ratio doesn't matter, only pure numbers
# we can sort the projects by 'net profit' defined as profits - capital
# then at each stage, we can choose the greatest 'net profit' project based on our current capital
# at the end of k steps, we will have the largest possible final capital

# how will we search through the net profit data
# we could iterate through it each time
# could do some type of hashing? -> extension

# how will make sure the elements are distinct
# create a set of chosen projects, make sure we're not in that set

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        chosen = set()

        net_profit = [(x1, x2) for x1, x2 in zip(profits, capital)]

        net_profit = sorted(net_profit, reverse = True)

        total, i = 0, 0

        while total < k and i < len(net_profit):
            profit, nec_capital = net_profit[i]
            if w >= nec_capital and i not in chosen:
                w += profit
                chosen.add(i)
                total += 1
                i = 0
            else:
                i += 1

    
        return w
        






        