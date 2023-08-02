from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        ans = []

        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                deque.appendleft(q, i)

        while q:
            curr = deque.popleft(q)
            ans.append(curr)
            for course in adj[curr]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    q.append(course)

        return len(ans) == numCourses

if __name__ == "__main__":
    sol = Solution()
    numCourses = 2
    prerequisites = [[1,0],[1,2],[0,1]]
    prerequisites = [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]
    prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]
    prerequisites = [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]
    prerequisites = [[2,0],[1,0],[3,1],[3,2],[1,3]]
    prerequisites = [[0,1]]
    prerequisites = [[1,0],[0,1]]
    print(sol.canFinish(numCourses, prerequisites))