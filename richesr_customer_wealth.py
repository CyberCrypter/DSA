class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # i=0,j=0
        result = []
        sum = 0
        n = len(accounts)
        for i in range(len(accounts)):
            for j in range(len(accounts[i])):
                sum += accounts[i][j]
                result.append(sum)
            sum = 0
        
        largest = result[0]
        for num in result:
            if num > largest:
                largest = num

        return largest
                


        