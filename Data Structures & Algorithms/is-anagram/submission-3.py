class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = {}
        t_set = {}
        if not len(s) - 1 == len(t) - 1:
            return False
        for i in range(len(s)):
           s_set[s[i]] = 1 + s_set.get(s[i], 0)
           t_set[t[i]] = 1 + t_set.get(t[i], 0)
        return s_set == t_set
        