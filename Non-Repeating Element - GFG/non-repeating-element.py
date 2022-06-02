#User function Template for python3
from collections import Counter

class Solution:
    def firstNonRepeating(self, arr, n): 
        
        d = dict()
        for i in arr:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        
        for i in arr:
            if d[i] == 1:
                return i
        
        return -1


#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict 

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr, n))
    
# } Driver Code Ends