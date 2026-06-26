class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            length = len(word)
            s = s + f'{length}#' + word

        return s

    def decode(self, s: str) -> List[str]:
        res = []
        

        i = 0
        while i<len(s):
            num = ''
            while s[i]!='#':
                num += s[i]
                i+=1
            length = int(num)
            res.append(s[i+1:i+length+1])

            i+=length+1

        return res
            

