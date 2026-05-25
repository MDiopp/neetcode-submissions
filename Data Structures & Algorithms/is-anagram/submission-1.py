class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == None and t == None:
            return True
        elif s == None or t == None:
            return False
        elif len(s) != len(t):
            return False
        else:
            llist = list(s)             
            for i in range(len(t)):
                for j in range(len(s) - i):
                    if t[i] == llist[j]:
                        llist.pop(j)
                        break
            if not llist:
                return True
            else:
                return False

        