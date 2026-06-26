class Solution:

    def encode(self, strs: List[str]) -> str:
        fullstring = ""
        for string in strs:
            fullstring+= str(len(string))+"#"+string

        return fullstring


    def decode(self, s: str) -> List[str]:
        out = []
        start = 0
        
        while start < len(s):
            j = start
            while s[j]!="#":
                j+=1
            length = int(s[start:j])
            out.append(s[j+1:length+j+1])
            start = j+length+1
        return out
