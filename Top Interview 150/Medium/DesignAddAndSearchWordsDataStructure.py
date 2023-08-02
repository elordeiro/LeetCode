class WordDictionary(object):
    def __init__(self):
        self.dict = {}
        self.is_word = False

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        if not word:
            self.is_word = True
            return
        if word[0] not in self.dict:
            self.dict[word[0]] = WordDictionary()
        self.dict[word[0]].addWord(word[1:])

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word:
            return self.is_word
        if word[0] == '.':
            for k in self.dict.keys():
                if self.dict[k].search(word[1:]):
                    return True
            return False
        else:
            if word[0] not in self.dict:
                return False
            else:
                return self.dict[word[0]].search(word[1:])



if __name__ == "__main__":
    sol = []
    sol.append(None)
    wordDictionary = WordDictionary()
    test_action = ["addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
    test_arguments = [["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]
    for action, arg in zip(test_action, test_arguments):
        if action == "addWord":
            sol.append(wordDictionary.addWord(arg[0]))
        else:
            sol.append(wordDictionary.search(arg[0]))
    print(sol)
