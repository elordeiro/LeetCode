import random

class RandomizedSet(object):

    def __init__(self):
        self.randomset = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.randomset:
            self.randomset.append(val)
            return True
        return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.randomset:
            self.randomset.remove(val)
            return True
        return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.randomset)


# Your RandomizedSet object will be instantiated and called as such:
if __name__ == "__main__":
    obj = RandomizedSet()
    results = []
    results.append(obj.remove(0))
    results.append(obj.remove(0))
    results.append(obj.insert(0))
    results.append(obj.getRandom())
    results.append(obj.remove(0))
    results.append(obj.insert(0))
    # results.append(obj.getRandom())
    print(results)
    print(obj.randomset)