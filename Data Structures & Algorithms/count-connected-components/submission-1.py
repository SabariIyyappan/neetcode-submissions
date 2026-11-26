import collections
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        preMap = collections.defaultdict(list)
        for edge in edges:
            preMap[edge[0]].append(edge[1])
            preMap[edge[1]].append(edge[0])
        
        visited = set()
        def dfs(number):
            if number in visited:
                return 
            visited.add(number)
            for child in preMap[number]:
                dfs(child)
        
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        
        return count
