class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7
        
        def countUpTo(num: str) -> int:
            n = len(num)
            
            @cache
            def dp(pos: int, digitSum: int, tight: bool, started: bool) -> int:
                if digitSum > max_sum:
                    return 0
                if pos == n:
                    return 1 if started and digitSum >= min_sum else 0
                
                limit = int(num[pos]) if tight else 9
                result = 0
                
                for d in range(0, limit + 1):
                    newStarted = started or d > 0
                    newSum = digitSum + d if newStarted else 0
                    newTight = tight and (d == limit)
                    result = (result + dp(pos + 1, newSum, newTight, newStarted)) % MOD
                
                return result
            
            return dp(0, 0, True, False)
        
        def decrement(num: str) -> str:
            num = list(num)
            i = len(num) - 1
            while i >= 0 and num[i] == '0':
                num[i] = '9'
                i -= 1
            if i >= 0:
                num[i] = str(int(num[i]) - 1)
            result = ''.join(num).lstrip('0')
            return result if result else '0'
        
        ans = (countUpTo(num2) - countUpTo(decrement(num1)) + MOD) % MOD
        return ans