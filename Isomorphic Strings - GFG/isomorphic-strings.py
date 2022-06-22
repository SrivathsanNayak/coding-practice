#User function Template for python3

class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,s,t):
        
        if len(s) != len(t):
            return False
        else:
            d = {}
            c = ''
            for i in range(len(s)):
                if s[i] in d.keys() and d[s[i]] != t[i]:
                    return False
                elif s[i] not in d.keys() and t[i] in d.values():
                    return False
                elif s[i] not in d.keys():
                    d[s[i]] = t[i]
            return True

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        s=str(input())
        p=str(input())
        ob = Solution()
        if(ob.areIsomorphic(s,p)):
            print(1)
        else:
            print(0)
# } Driver Code Ends