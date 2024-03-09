from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = defaultdict(int)
        for outd, ind in trust:
            count[outd] -= 1
            count[ind] += 1
        for i in range(1, n+1):
            if count[i] == n-1:
                return i
        
        return -1
