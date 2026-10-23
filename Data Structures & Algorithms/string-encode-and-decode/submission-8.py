class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ''
        for s in strs:
            out += str(len(s))+'#'+s
        return out
    def decode(self, s: str) -> List[str]:
        i = 0
        cur = ''
        out = []
        while i < len(s):
            if s[i] == '#':
                j = i + 1 + int(cur)
                out.append(s[i+1:j])
                cur = ''
                i = j
            else:
                cur+=s[i]
                i+=1
            
        return out