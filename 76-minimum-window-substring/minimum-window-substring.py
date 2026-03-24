class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        map = defaultdict(int)
        for ch in t:
            map[ch]+=1
        target = len(t)
        start = 0
        left=0
        ans=float('inf')
        for end in range(len(s)):
            if s[end] in map:
                map[s[end]]-=1
                if map[s[end]]>=0:
                    target-=1
            while target==0:
                if end-start+1<ans:
                    ans=end-start+1
                    left=start
                if s[start] in map:
                    map[s[start]]+=1
                    if map[s[start]]>0:
                        target+=1
                start+=1
        return "" if ans==float('inf') else s[left:left+ans]
        