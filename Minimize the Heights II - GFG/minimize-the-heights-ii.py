#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        #referred solution
        
        arr.sort()
        ans = arr[-1] - arr[0]
        
        for i in range(1, n):
            #we compare adjacent elements
            #by decreasing current element and increasing previous element
            #to find possible min and max
            #difference is compared with ans to find least diff
            minEl = min(arr[0] + k, arr[i] - k)
            maxEl = max(arr[-1] - k, arr[i - 1] + k)
            
            #to avoid negative terms
            if minEl < 0:
                continue
            
            ans = min(ans, maxEl - minEl)
            
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends