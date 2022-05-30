#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        zeroCount = arr.count(0)
        oneCount = arr.count(1)
        twoCount = n - zeroCount - oneCount
        arr.clear()
        arr.extend([0] * zeroCount + [1] * oneCount + [2] * twoCount)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends