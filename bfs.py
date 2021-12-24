from collections import deque


class Solution:

    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        q = deque()
        v = set()
        q.append(0)
        ans = []
        while q:
            s = q.popleft()
            ans.append(s)
            for i in adj[s]:
                if i not in v:
                    q.append(i)
                    v.add(i)
        return ans
