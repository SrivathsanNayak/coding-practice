#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		#referred editorial soln
		minVal = maxVal = maxProd = arr[0]
		
		for i in range(1, n):
		    if arr[i] < 0:
		        minVal, maxVal = maxVal, minVal
		    
		    maxVal = max(arr[i], maxVal * arr[i])
		    minVal = min(arr[i], minVal * arr[i])
		    maxProd = max(maxProd, maxVal)
		    
	    return maxProd

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends