class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = [0]*26
        count_window = [0]*26
        n = len(s1)
        for i in s1:
            count_s1[ord(i) - ord('a')] += 1
        
        l = 0
        if len(s1)>len(s2):
            return False
        
        for r in range(len(s2)):
            count_window[ord(s2[r]) - ord('a')] += 1

            if(r-l+1)>n:
                count_window[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            if (r-l+1) == n:
                if count_s1 == count_window:
                    return True
            
        return False

