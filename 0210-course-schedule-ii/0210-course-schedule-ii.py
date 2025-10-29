from collections import deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {i: [] for i in range(numCourses)}
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return order if len(order) == numCourses else []
