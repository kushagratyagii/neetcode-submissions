class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei = collections.defaultdict(list) 
        res = 1
        visit = set()
        q = deque([beginWord])
        if beginWord not in wordList:
            wordList.append(beginWord)
        visit.add(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[0:j] + '*' + word[j+1:]
                nei[pattern].append(word)

        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[0:j] + '*' + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0