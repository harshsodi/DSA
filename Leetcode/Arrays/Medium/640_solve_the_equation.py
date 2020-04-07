# Runtime: 16 ms, faster than 74.83% of Python online submissions for Solve the Equation.
# Memory Usage: 12.8 MB, less than 50.00% of Python online submissions for Solve the Equation.

class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        
        def brkdown(s):
            
            sm = 0
            num_x = 0
            
            curr_sym = 1
            curr_st = ""
            
            for ch in s:
                if ch == "x":
                    if curr_st == "":
                        num = 1
                    else:
                        num = int(curr_st)
        
                    num_x += curr_sym * num
                    curr_st = ""
            
                elif ch == "-":
                    if curr_st != "":
                        # print "adding", curr_sym * int(curr_st), ch
                        sm += curr_sym * int(curr_st)
                    curr_sym = -1
                    curr_st = ""
                
                elif ch == "+":
                    if curr_st != "":
                        # print "adding", curr_sym * int(curr_st), ch
                        sm += curr_sym * int(curr_st)
                    curr_sym = 1
                    curr_st = ""
            
                else:
                    curr_st += ch
            
            if curr_st != "":
                sm += curr_sym * int(curr_st)
            
            return [sm, num_x]
        
        hs = equation.split("=")
        lhs_ = hs[0]
        rhs_ = hs[1]
        
        lhs = brkdown(lhs_)
        rhs = brkdown(rhs_)
        
        print lhs, rhs
        
        totx = lhs[1] - rhs[1]
        totnum = rhs[0] - lhs[0]
        
        if totx == 0:
            if totnum == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        
        return "x=" + str(totnum/totx)