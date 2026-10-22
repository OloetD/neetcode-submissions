class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for str in strs:
            str_ = ''.join(sorted(str))

            res.setdefault(str_, []).append(str)
        return list(res.values())