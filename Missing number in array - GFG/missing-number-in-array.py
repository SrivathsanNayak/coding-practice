#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        return (list(set(array) ^ set(list(range(1, n+1))))[0])
        #calculates symmetric difference
        #compares list of 1 to n numbers
        #and given array

#{ 
#  Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends