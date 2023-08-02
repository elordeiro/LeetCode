class Node(object):
    def __init__(self, key=-1, val=-1, prev=None, next=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.quantity = 0
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self._remove(self.cache[key])
        new_node = Node(key, value)
        self._add(new_node)
        self.cache[key] = new_node
        if self.quantity > self.capacity:
            node = self.tail.prev
            self._remove(node)
            self.cache.pop(node.key)
        
    def _add(self, node):
        self.quantity += 1
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def _remove(self, node):
        self.quantity -= 1
        node.prev.next = node.next
        node.next.prev = node.prev
        del node


def printList(head):
    if head is None:
        return
    print((head.key, head.val))
    printList(head.next)

if __name__ == "__main__":
    capacity = 2
    obj = LRUCache(capacity)
    sol = []
    sol.append(None)
    test_cases = [[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

    for i, test in enumerate(test_cases):
        print(f"i is: {i}")
        if len(test) == 1:
            print(f"action is: get({test[0]})")
            sol.append(obj.get(test[0]))
        else:
            print(f"action is: put({test[0]}, {test[1]})")
            sol.append(obj.put(test[0], test[1]))
        print(f"quantity: {obj.quantity}")
        printList(obj.head)
        print("----------")

    # sol.append(obj.put(2, 1))
    # sol.append(obj.put(2, 2))
    # sol.append(obj.get(2))
    # sol.append(obj.put(1, 1))
    # sol.append(obj.put(4, 4))
    # sol.append(obj.get(2))
    # sol.append(obj.get(1))
    # sol.append(obj.get(4))


    print(sol)
    