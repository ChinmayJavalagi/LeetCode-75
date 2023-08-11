
'''
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
'''

class Solution(object):
    def asteroidCollision(self, asteroids):
        s = []
        for a in asteroids:
            while s and a<0 and s[-1]>0:
                diff = a+s[-1]
                if diff>0:
                    a = 0
                elif diff<0 :
                    s.pop()
                else:
                    a = 0
                    s.pop()
            if a:
                s.append(a)
        return s
