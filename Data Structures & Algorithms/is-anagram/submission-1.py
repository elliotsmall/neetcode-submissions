class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = {}
        t_set = {}
        if not len(s) - 1 == len(t) - 1:
            return False
        for char in s:
            s_set[char] = s_set.get(char, 0) + 1
        for char in t:
            t_set[char] = t_set.get(char, 0) + 1
        return s_set == t_set
        