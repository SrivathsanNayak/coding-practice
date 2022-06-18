class Solution:
            
    def inversionCount(self, arr, n):
        
        def mergeSort(arr, temparr, left, right):
        
            invCount = 0
        
            if left < right:
            
                mid = (left + right) // 2
                invCount += mergeSort(arr, temparr, left, mid) #left subarray
                invCount += mergeSort(arr, temparr, mid + 1, right) #right subarray
            
                invCount += merge(arr, temparr, left, mid + 1, right) #merge both arrays
            
            return invCount
            
        
        def merge(arr, temparr, left, mid, right):
            
            i = left #starting index of left subarray
            j = mid #starting index of right subarray
            k = left #starting index of merged subarray
            invCount = 0
        
            while i <= (mid - 1) and j <= right:
            
                if arr[i] <= arr[j]:
                    temparr[k] = arr[i]
                    i += 1
                    k += 1
            
                else:
                    #inversion
                    temparr[k] = arr[j]
                    invCount += (mid - i)
                    #all elements after the particular position in left subarray will be greater than right subarray elements
                    j += 1
                    k += 1
        
            #copy remaining elements of left subarray into merged array
            while i <= (mid - 1):
                temparr[k] = arr[i]
                i += 1
                k += 1
            
            #copy remaining elements of right subarray into merged array
            while j <= right:
                temparr[k] = arr[j]
                j += 1
                k += 1
            
            #copy merged sorted array into original array
            for i in range(left, right + 1):
                arr[i] = temparr[i]
            
            return invCount
 
            
        #using merge sort
        temparr = [0] * n
        return mergeSort(arr, temparr, 0, n - 1)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends