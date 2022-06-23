#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        if 0 in arr:
            return True
        
        #using prefix sum concept
        #if prefix (running) sum repeats in array or it is 0
        #then there is subarray with 0 sum
        
        psum = 0
        s = set()
        for i in arr:
            psum += i
            if psum == 0 or psum in s:
                return True
            s.add(psum)
        return False
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends