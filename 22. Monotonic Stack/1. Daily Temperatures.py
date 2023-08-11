class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][0]<temperatures[i]:
                stackTop, j = stack.pop()
                res[j] = i-j
            stack.append([temperatures[i],i])  
        return res
