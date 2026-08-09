class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if k == 0 and len(s) < 2 or len(set(s)) == 1:
            return len(s)
        
        frequencyNums = {sl: 0 for sl in list(set(s))}
        
        l = 0
        answer = 0
        fNums = 0

        for r in range(len(s)):
            frequencyNums[s[r]] += 1
            fNums = max(fNums, frequencyNums[s[r]])

            if (r - l + 1) - fNums <= k:
                answer = max(answer, sum(list(frequencyNums.values())))
            else:
                while((r - l + 1) - fNums > k):
                    frequencyNums[s[l]] -= 1
                    l += 1            

        return answer