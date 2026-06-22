class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {'b':0, 'a':0,'l':0, 'o':0, 'n':0}
        for c in text:
            if c in d:
                d[c]+=1
        m1,m2 = min(d['b'], d['a'], d['n']), min(d['l'],d['o'])//2
        return min(m1,m2)

        