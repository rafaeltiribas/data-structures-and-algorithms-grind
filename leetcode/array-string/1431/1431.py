class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = 0
        for i in range(len(candies)):
            if candies[i] > greatest:
                greatest = candies[i]

        result = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies >= greatest:
                result[i] = True
        
        return result