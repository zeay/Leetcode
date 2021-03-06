class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2
        
        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]
        
        dp[0][0] = True
        
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
                    
        return dp[-1][-1]