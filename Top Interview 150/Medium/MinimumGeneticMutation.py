import copy
class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        if endGene not in bank:
            return -1
        bank = set(bank)
        letters = set(['A', 'C', 'G', 'T'])
        steps = 0
        q = [startGene]
        while q:
            s = len(q)
            while s > 0:
                new_gene = q.pop(0)
                if new_gene == endGene:
                    return steps
                bank.discard(new_gene)
                for i, char in enumerate(new_gene):
                    curr = new_gene
                    for l in letters.difference(char):
                        curr = curr[:i] + l + curr[i+1:]
                        if curr in bank:
                            q.append(curr)
                s -= 1
            steps += 1
        return -1





if __name__ == "__main__":
    sol = Solution()
    startGene, endGene, bank = "AACCGGTT", "AACCGCTA", ["AACCGGTA","AACCGCTA","AAACGGTA"] # 2
    startGene, endGene, bank = "AAAAAAAA", "CCCCCCCC", ["AAAAAAAA","AAAAAAAC","AAAAAACC","AAAAACCC","AAAACCCC","AACACCCC","ACCACCCC","ACCCCCCC","CCCCCCCA","CCCCCCCC"]
    startGene, endGene, bank = "AACCGGTT", "AACCGGTA", ["AACCGGTA"] 
    print(sol.minMutation(startGene, endGene, bank))