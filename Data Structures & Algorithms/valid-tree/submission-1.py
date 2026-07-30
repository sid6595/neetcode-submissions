class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # what makes a tree invalid
        # multiple disjoint sets, cycles
        # union find
        if len(edges) != n-1:
            return False

        parent = [i for i in range(n)]
        rank = [1] * (n)

        def find(n):
            if n != parent[n]:
                parent[n] = find(parent[n])
            
            return parent[n]
        
        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return False # means they have the same root
            
            if rank[pa] > rank[pb]:
                parent[pb] = pa
                rank[pa] += rank[pb]
            else:
                parent[pa] = pb
                rank[pb] += rank[pa]
            
            return True
        
        for u, v in edges:
            if union(u, v):
                continue
            else:
                return False

        return True