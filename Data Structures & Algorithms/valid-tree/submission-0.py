from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(list[int])

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for nei in adjList[node]:
                if nei == parent:
                    continue
                
                if not dfs(nei, node):
                    return False
            
            return True
        
        return dfs(n-1, -1) and len(visited) == n
                

                
