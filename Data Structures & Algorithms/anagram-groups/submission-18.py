class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for i in strs:
            key = "".join (sorted(i))
            hashmap.setdefault(key, []).append(i)
        return sorted(hashmap.values())
        


        