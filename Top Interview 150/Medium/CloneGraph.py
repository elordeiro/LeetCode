class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return
        self.visited = set()
        self.dict = {}
        self.create_dict(node)
        return self.dict[node]
    
    def create_dict(self, node):
        if node in self.visited:
            return
        self.visited.add(node)
        self.dict[node] = Node(val=node.val)
        for neighbor in node.neighbors:
            self.create_dict(neighbor)
            self.dict[node].neighbors.append(self.dict[neighbor])

visited = set()
def printGraph(node):
    if node in visited:
        return
    visited.add(node)
    print(node.val)
    for neighbor in node.neighbors:
        printGraph(neighbor)

if __name__ == "__main__":
    sol = Solution()
    node1 = Node(val=1)
    node2 = Node(val=2)
    node3 = Node(val=3)
    node4 = Node(val=4)
    node1.neighbors =  [node2, node4]
    node2.neighbors =  [node1, node3]
    node3.neighbors =  [node2, node4]
    node4.neighbors =  [node1, node3]
    printGraph(node1)
    print()
    visited = set()
    new_node = sol.cloneGraph(node1)
    node1.val = 999
    printGraph(new_node)