class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        
        while right != len(prices):
            print(right , left, len(prices), prices,prices[left],prices[right])

            if prices[left] > prices[right]:
                left = right
                
            elif prices[right] - prices[left] > profit:
                profit = prices[right] - prices[left]

            right +=1
        
        return profit