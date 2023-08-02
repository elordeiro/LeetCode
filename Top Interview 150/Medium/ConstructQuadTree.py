import time

class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def is_leaf(grid):
            return all(all(cell == grid[0][0] for cell in row) for row in grid)

        def construct_helper(grid):
            n = len(grid)
            if n == 1:
                return Node(grid[0][0], True, None, None, None, None)

            if is_leaf(grid):
                return Node(grid[0][0], True, None, None, None, None)

            half_n = n // 2
            tl = construct_helper([row[:half_n] for row in grid[:half_n]])
            tr = construct_helper([row[half_n:] for row in grid[:half_n]])
            bl = construct_helper([row[:half_n] for row in grid[half_n:]])
            br = construct_helper([row[half_n:] for row in grid[half_n:]])

            return Node(tl.val, False, tl, tr, bl, br)

        if not grid:
            return

        return construct_helper(grid)


def printQuadTree(head, i):
    if not head:
        return
    print(f"i: {i}, isLeaf: {head.isLeaf}, val: {head.val}")
    printQuadTree(head.topLeft, i+1)
    printQuadTree(head.topRight, i+1)
    printQuadTree(head.bottomLeft, i+1)
    printQuadTree(head.bottomRight, i+1)
    return


if __name__ == "__main__":
    sol = Solution()
    grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
    start_time = time.time()
    sol.construct(grid)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.10f} seconds")