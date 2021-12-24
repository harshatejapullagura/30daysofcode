def dfsOfGraph(self, V, adj):
    # code here
    def dfs(V, processed, adj, result):
        processed.add(V)
        result.append(V)
        for n in adj[V]:
            if n not in processed:
                dfs(n, processed, adj, result)  # go for  first found child

    processed = set()
    result = []
    dfs(0, processed, adj, result)
    return result
