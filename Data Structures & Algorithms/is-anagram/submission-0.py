class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = {}
        str2 = {}
        x1 = len(s)
        x2 = len(t)

        if x1 != x2:
            return False
        
        ## hashmap for s
        for i in s:
            if i in str1:
                str1[i] += 1
            else:
                str1[i] = 1
        
        ## hashmap for t
        for i in t:
            if i in str2:
                str2[i] += 1
            else:
                str2[i] = 1
        
        if str1 == str2:
            return True
        
        return False
