# Runtime: 672 ms, faster than 99.15% of Python online submissions for Expression Add Operators.
# Memory Usage: 12.3 MB, less than 25.00% of Python online submissions for Expression Add Operators.

class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        
        n = len(num)
        ans = []
        
        def f(index, curr_op, prev_op, val, expr):
            # print expr
            if index == n:
                if val == target and curr_op == 0:
                    # print "Found"
                    ans.append(expr[1:])
                return
            
            curr_op = curr_op*10 + int(num[index])
            str_op = str(curr_op)
            
            #add
            f(index+1, 0, curr_op, val + curr_op, expr + "+" + str_op)
            
            #subtract
            if expr:
                f(index+1, 0, -curr_op, val - curr_op, expr + "-" + str_op)
            
            #multiply
            if expr:
                f(index+1, 0, curr_op * prev_op, val - prev_op + (curr_op*prev_op), expr + "*" + str_op)
            
            # do nothing
            if curr_op > 0:
                f(index+1, curr_op, prev_op, val, expr)
        
        f(0,0,0,0,"")
        return ans