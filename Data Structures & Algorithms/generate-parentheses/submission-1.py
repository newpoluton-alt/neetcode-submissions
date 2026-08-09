class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.backtrack(ans, "", 0, 0, n)
        return ans

    def backtrack(self, ans, cur, ob, cb, mx_val):
        if(len(cur) == mx_val * 2):
            ans.append(cur)
            return

        if(ob < mx_val):
            self.backtrack(ans, cur + "(", ob+1, cb, mx_val)
        
        if(cb < ob):
            self.backtrack(ans, cur + ")", ob, cb+1, mx_val)
        