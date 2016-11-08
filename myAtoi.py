class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
         
        # 1.continuous non-numeric symbols behind number：
        # '+-2' expects 0
        
        # 2.discards the rest behind the first number
        # '1+111' expects 1
        # '123adfsaf' expects 123
        
        # 3.overflow:
        # '2147483648' expects 2147483647
        # '-2147483648' expects 2147483648
        
        # 4.sign of the number
        
        ret = 0
        sign = 1 # store positive or negative
        count = 0 # store the number of non-numeric symbols,if non-numeric symbols appear after number,break
        for c in str:
            count += 1
            if '0'<= c <= '9':
                ret *= 10
                ret += int(c)
            # if there is sign, sign must appear first
            elif c == '+' and count == 1:
                sign = 1
            elif c == '-' and count == 1:
                sign = -1
            elif c == ' ' and count == 1:
                count -=1
            else:
                break
        if ret > 2147483647 and sign == 1:
            return 2147483647
        elif ret > 2147483648 and sign == -1:
            return -2147483648
        else:
            return int(sign*ret)