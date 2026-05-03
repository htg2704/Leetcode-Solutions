class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal)!=len(s):
            return False
        s2 = s*2
        goal2 = goal*2
        return True if goal in s2 and s in goal2 else False
        