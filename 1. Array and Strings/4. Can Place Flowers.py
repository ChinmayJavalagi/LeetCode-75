'''
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if n>len(flowerbed):
            return False
        if n==0:
            return True
        p = 0 
        for i in range(len(flowerbed)-1):
            if p==0 and flowerbed[i]==0 and  flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
            p = flowerbed[i]
            if n==0:
                return True
        if n==1 and p==0 and flowerbed[-1]==0:
            return True
        else:
            return False
