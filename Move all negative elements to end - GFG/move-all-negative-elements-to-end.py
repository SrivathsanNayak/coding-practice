#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        j = 0
        temp = [None] * n
        for i in range(n):
            if arr[i] > 0:
                temp[j] = arr[i]
                j += 1
        for i in range(n):
            if arr[i] < 0:
                temp[j] = arr[i]
                j += 1
        for i in range(n):
            arr[i] = temp[i]
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends