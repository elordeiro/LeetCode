class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def getNext(self, root):
        while root:
            if root.left:
                return root.left
            if root.right:
                return root.right
            root = root.next
        return None
    
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root:
            if root.left:
                if root.right:
                    root.left.next = root.right
                else:
                    root.left.next = self.getNext(root.next)
            
            if root.right:
                root.right.next = self.getNext(root.next)

            self.connect(root.right)
            self.connect(root.left)
            return root

    def printTree(self, root):
        if root:
            try:
                print(f"val: {root.val}, next: {root.next.val}")
            except:
                print(f"val: {root.val}, next: {root.next}")
            self.printTree(root.left)
            self.printTree(root.right)



if __name__ == "__main__":
    sol = Solution()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(7)
    sol.printTree(root)
    print()
    root = sol.connect(root)
    sol.printTree(root)