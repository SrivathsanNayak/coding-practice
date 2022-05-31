#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        sumArray = arr[0]
        leftPtr = 0
        rightPtr = 1
        
        while rightPtr <= n:
            while sumArray > s and leftPtr < (rightPtr - 1):
                sumArray -= arr[leftPtr]
                leftPtr += 1
                
            if sumArray == s:
                return [leftPtr + 1, rightPtr]
                
            if rightPtr < n:
                sumArray += arr[rightPtr]
                
            rightPtr += 1
            
        return [-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends