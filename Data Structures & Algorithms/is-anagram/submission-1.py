class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def counts(s: str) -> dict:
            ret = {}
            for c in s:
                if c not in ret:
                    ret[c] = 1
                ret[c] +=1
            return ret
        
        s_counts, t_counts = counts(s), counts(t)
        return set(t_counts.keys()) == (s_counts.keys()) and all(t_counts.get(k,0) == v for k,v in s_counts.items())