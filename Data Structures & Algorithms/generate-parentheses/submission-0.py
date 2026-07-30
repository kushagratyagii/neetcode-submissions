class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        tray = []

        def backtrack(n_open,n_closed):
            if n_open == n_closed == n:
                res.append("".join(tray))
                return

            if n_open < n:
                tray.append("(")
                backtrack(n_open+1,n_closed)
                tray.pop()
            
            if n_closed < n_open :
                tray.append(')')
                backtrack(n_open,n_closed+1)
                tray.pop()
            
        backtrack(0,0)
        return res