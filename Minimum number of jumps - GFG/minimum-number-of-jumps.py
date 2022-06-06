#User function Template for python3
class Solution:
	def minJumps(self, arr, n):
	    #code here
	    
	    if n == 1:
	        return 0
	    
	    if arr[0] == 0:
	        return -1
	        
	    maxReach = steps = arr[0]
	    jumps = 1
	    
	    for i in range(1, n):
	        #reached last index
	        if i == (n - 1):
	            return jumps
	            
	        #the maximum we can reach to, from our current position
	        maxReach = max(maxReach, i + arr[i])
	        steps -= 1
	        #keeps track of how much we can move from current position
	        
	        #reached furthest possible position
	        if steps == 0:
	            jumps += 1
	            #moved ahead of what is possible
	            if i >= maxReach:
	                return -1
	            
	            #updating steps
	            steps = maxReach - i
	            
	    return -1
	            
	        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends