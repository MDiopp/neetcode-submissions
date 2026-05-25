class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        fw = {}
        sw = {}
        for char in s:
            fw[char] = fw.get(char, 0) + 1
        for char in t:
            sw[char] = sw.get(char, 0) + 1
        for char in s:
            if fw.get(char) != sw.get(char):
                return False
        return True


        