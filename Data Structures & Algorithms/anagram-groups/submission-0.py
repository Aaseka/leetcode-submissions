class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for i in strs:
            sort = ''.join(sorted(i))
            anagram[sort].append(i)
        
        return list(anagram.values())