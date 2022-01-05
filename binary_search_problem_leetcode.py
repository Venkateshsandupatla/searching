#Question
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#You must write an algorithm with O(log n) runtime complexity.
'''
    Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0

Input nums = [1,3] , target =0
output =0
'''


def code(arr , target):
    start = 0
    end = len(arr)-1
    while start<end:
        middle = (start + end)//2
        if arr[middle] == target:
            print("The position of number is {}".format(middle))
            break
        elif arr[middle]<target:
             start = middle+1
             middle = (start + end)//2
        elif arr[middle]>target:
             end = middle-1
             middle = (start + end)//2
        
    if start == end:
        if target>arr[start]:
            print("It will be in the position {}".format(start+1))
        else:
            print("It will be in the position {}".format(start))
        
    elif start>end:  # if start >end
        print("It will be in the position {}".format(start))


array = [1,3,5,6]
code(array,0)