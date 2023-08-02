class Trie(object):
    def __init__(self):
        self.dict = {}
        self.is_word = False

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        if len(word) > 0:
            if word[0] not in self.dict:
                self.dict[word[0]] = Trie()
                self.dict[word[0]].insert(word[1:])
            else:
                self.dict[word[0]].insert(word[1:])
        else:
            self.is_word = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word:
            return self.is_word
        if word[0] in self.dict:
            return self.dict[word[0]].search(word[1:])

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        if not prefix:
            return False
        if len(prefix) > 1:
            if prefix[0] in self.dict:
                return self.dict[prefix[0]].startsWith(prefix[1:])
            return False
        return prefix in self.dict

            
        
if __name__ == "__main__":
    sol = []
    obj = Trie()
    sol.append(None)
    sol.append(obj.insert("hotdog"))
    # sol.append(obj.search("apple"))
    # sol.append(obj.search("app"))
    sol.append(obj.startsWith("dog"))
    # sol.append(obj.insert("app"))
    # sol.append(obj.search("app"))
    print(sol)