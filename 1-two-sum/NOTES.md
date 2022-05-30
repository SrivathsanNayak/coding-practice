We use enumerate(nums) here to go through both index and value of nums array.
​
The traversed index-value pairs are stored in the seen dictionary.
​
If the remaining number is already in the dictionary, both indices are returned.
​
Otherwise, the remaining value is added to the seen dictionary.