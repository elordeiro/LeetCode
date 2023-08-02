class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        
        char_count = 0
        word_count = 0
        line = []
        page = []
        for word in words:
            n = len(word)
            line_len = char_count + (word_count - 1)
            if line_len + n < maxWidth:
                line.append(word)
                char_count += n
                word_count += 1
            else:
                new_line = ""
                space_count = maxWidth - char_count
                if word_count == 1:
                    line[0] += ' ' * (maxWidth - char_count)
                else:
                    spaces = space_count // (word_count - 1)
                    space_list = []
                    for i in range(word_count-1):
                        space_list.append(' ' * spaces)
                        space_count -= spaces
                    i = 0
                    while space_count > 0:
                        space_list[i] += ' '
                        space_count -= 1
                        i+= 1
                for i, w in enumerate(line):
                    new_line += w
                    if i < word_count - 1:
                        new_line += space_list[i]
                page.append(new_line)
                line = [word]
                char_count = n
                word_count = 1
        
        new_line = ""
        for word in line:
            new_line += word + " "
        new_line = new_line.strip()
        new_line += ' ' * (maxWidth - len(new_line))
        page.append(new_line)
        return page
    
"everything else we do"

if __name__ == "__main__":
    sol = Solution()
    words = ["What","must","be","acknowledgment","shall","be"]
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    words = ["ask   not   what","your country can","do  for  you ask","what  you can do","for your country "]
    maxWidth = 16
    print(sol.fullJustify(words, maxWidth))
