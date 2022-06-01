class Solution:
    def duplicates(self, arr, n): 
    	seen = set()
    	dup = [x for x in arr if x in seen or seen.add(x)]
    	
    	if len(dup) == 0:
    	    return [-1]
    	else:
    	    return sorted(list(set(dup)))
    	    

#{ 
#  Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends