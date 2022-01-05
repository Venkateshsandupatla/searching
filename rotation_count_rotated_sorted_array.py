#https://www.geeksforgeeks.org/find-rotation-count-rotated-sorted-array/
'''
Consider an array of distinct numbers sorted in increasing order. The array has been rotated (clockwise) k number of times. Given such an array, find the value of k.
Examples: 
 

Input : arr[] = {15, 18, 2, 3, 6, 12}
Output: 2
Explanation : Initial array must be {2, 3,
6, 12, 15, 18}. We get the given array after 
rotating the initial array twice.

Input : arr[] = {7, 9, 11, 12, 5}
Output: 4

Input: arr[] = {7, 9, 11, 12, 15};
Output: 0

'''

#to know the how many times rotation has done we have to find the pivot of this array
#if the pivot index of the array is 1 we have to do 1+1 = 2 is the count of rotation
# if the pivot is last element in the array then the array is not rotated.
# Lets find the pivot
def pivot(arr)->int:
      start = 0
      end = len(arr)-1
      while start<end:
          mid = start + (end-start)//2
          if (arr[mid]>arr[mid+1] and mid<end):
              return mid
          elif (arr[mid]<arr[mid-1] and mid>start):
              return mid-1
          elif arr[mid] <= arr[start]:
              end = mid-1
          elif arr[mid]>arr[start]:
              start = mid + 1
      return -1         


arr = [15,18,2,3,6,12]
arr1 = [7, 9, 11, 12, 15]
answer = pivot(arr1)
if pivot==-1:
    #array is not rotated
    print(answer+1)

else:
    print(answer+1)




