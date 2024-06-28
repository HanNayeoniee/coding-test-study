# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = sys.maxsize
        
        # 포인터를 오른쪽으로 이동하면서 이전 상태 지점을 기준으로 가격 차이 계산
        for i in range(len(prices)):
            buy = min(buy, prices[i])
            profit = max(profit, prices[i]-buy)
        
        return profit