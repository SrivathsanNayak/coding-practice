class Solution(object):
    def sortSentence(self, s):
        l = s.split()
        d = {int(word[-1]):str(word[:-1]) for word in l}
        return ' '.join(str(d[x]) for x in sorted(d))
        