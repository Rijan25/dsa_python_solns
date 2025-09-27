class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        profit=0
        for num in prices:
            profit=max(profit,num-buy)
            buy=min(buy,num)
        return profit        


        # buy=prices[0]
        # profit=0
        # for num in prices:
        #     profit=max(profit,num-buy)
        #     buy=min(buy,num)
        # return profit            





        # buy=prices[0]
        # profit=0
        # for num in prices:
        #     profit=max(profit,num-buy)
        #     buy=min(buy,num)
        # return profit    

       
          

        #Brute Force Approach 
        # profit=[]
        # for l in range(len(prices)-1):
        #     for r in range(l,len(prices)):
        #         profit.append(prices[r]-prices[l])
        # return max(profit,default=0)        
            
        



               

        