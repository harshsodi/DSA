# Runtime: 36 ms, faster than 87.39% of Python online submissions for Unique Email Addresses.
# Memory Usage: 11.9 MB, less than 58.49% of Python online submissions for Unique Email Addresses.

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        
        d = {}
        
        for email in emails:
            breakdown = email.split("@")
            
            lname = breakdown[0];
            domain = breakdown[1]
            
            lname = lname.split('+')[0]
            lname = "".join(lname.split('.'))
            
            final = lname + '@' + domain
            
            d[final] = d.get(final, 0) + 1
        
        return len(d.keys())