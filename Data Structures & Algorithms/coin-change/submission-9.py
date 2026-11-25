class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = (amount+1) * [-1]
        memo[0] = 0
        def memo_amount(memo, amount):
            # print(f'computing memo for amount {amount}')
            if amount in coins:
                return 1
            if amount < 0:
                return float('inf')
            if memo[amount] > -1:
                return memo[amount]
            x = 1 + min(memo_amount(memo, amount - c) for c in coins)
            memo[amount] = x
            # print(f'Setting a memo for amount {amount} to {x}')
            return x
        x = memo_amount(memo,amount)
        return -1 if x == float('inf') else x