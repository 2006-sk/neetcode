class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        in_degree = [0] * numCourses

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            in_degree[crs] += 1

        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        res = []

        while queue :
            crs = queue.popleft()
            res.append(crs)

            for neighbour in adj[crs]:
                in_degree[neighbour] -= 1

                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
        return res if len(res) == numCourses else[]

