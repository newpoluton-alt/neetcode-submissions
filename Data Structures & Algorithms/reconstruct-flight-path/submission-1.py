class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            adj[src].append(dst)      # descending → pop() yields smallest

        stack, res = ["JFK"], []
        while stack:
            while adj[stack[-1]]:
                stack.append(adj[stack[-1]].pop())
            res.append(stack.pop())   # airport is exhausted; record it
        return res[::-1]