from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Always returns a string (even for [] and [""])
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # 1) read the length up to '#'
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])   # length as an int
            j += 1                 # move past '#'

            # 2) read exactly 'length' characters
            res.append(s[j:j + length])

            # 3) jump index to the start of the next chunk
            i = j + length

        return res
