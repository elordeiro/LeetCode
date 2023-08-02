class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        self.graph = {}
        self.visited = set()
        for i, (a, b) in enumerate(equations):
            if a in self.graph:
                self.graph[a].append((b, values[i]))
            else:
                self.graph[a] = [(b, values[i])]
            if b in self.graph:
                self.graph[b].append((a, 1 / values[i]))
            else:
                self.graph[b] = [(a, 1 / values[i])]
        sol = []
        for s, e in queries:
            sol.append(self.DFS(s, e, 1))
            self.visited = set()
        return sol

    def DFS(self, start, end, val):
        if start not in self.graph:
            return -1
        if start in self.visited:
            return -1
        self.visited.add(start)
        for vertex, weight in self.graph[start]:
            if vertex == end:
                return val * weight
            ret = self.DFS(vertex, end, val*weight)
            if ret != -1:
                return ret
        return -1







if __name__ == "__main__":
    sol = Solution()
    # equations = [["a","b"],["b","c"]]
    # values = [2.0,3.0]
    # queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    equations = [["a","b"],["b","c"],["bc","cd"]]
    values = [1.5,2.5,5.0]
    queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    print(sol.calcEquation(equations, values, queries))