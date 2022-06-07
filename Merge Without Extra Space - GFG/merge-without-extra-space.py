#User function Template for python3
import math

class Solution:
    def merge(self, arr1, arr2, n, m): 
        #gap method
        gap = int(math.ceil((m + n) / 2))
        
        while (gap > 0):
                
            #pointers for gap
            i = 0
            j = gap
            
            while j < (n + m):
                
                if j < n and arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                
                elif i < n and j >= n and arr1[i] > arr2[j - n]:
                    arr1[i], arr2[j - n] = arr2[j - n], arr1[i]
                    
                elif i >= n and j >= n and arr2[i - n] > arr2[j - n]:
                    arr2[i - n], arr2[j - n] = arr2[j - n], arr2[i - n]
                    
                i += 1
                j += 1

            if gap == 1:
                gap = 0
            else:
                gap = int(math.ceil(gap / 2))
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n, m=map(int, (input().strip().split()))
        arr1=list(map(int , input().strip().split()))
        arr2=list(map(int , input().strip().split()))
        ob = Solution()
        ans=ob.merge(arr1, arr2, n, m)
        for x in arr1:
            print(x, end=" ")
        for x in arr2:
            print(x, end=" ")
        print()
        tc=tc-1
# } Driver Code Ends