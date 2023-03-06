"""Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
"""
def biggie_size(listEl):
    for element in range(0, len(listEl)):
        if listEl[element] > 0:
            listEl[element] = "big"
    return listEl

print(biggie_size([-1, 3, 5, -5]))

"""Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. 
(Note that zero is not considered to be a positive number).
Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
"""
def count_positives(nums):
    count=0
    for element in range(0,len(nums)):
        if nums[element] > 0:
            nums[len(nums)-1]=count
            count+=1
    return nums
print(count_positives([1,6,-4,-2,-7,-2]))

"""Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
Example: sum_total([1,2,3,4]) should return 10
Example: sum_total([6,3,-2]) should return 7 """
def sum_total(nums):
    sum=0
    for element in range(0,len(nums)):
        sum+= nums[element]
    return sum
print(sum_total([1,2,3,4]))    

"""
Average - Create a function that takes a list and returns the average of all the values.x
Example: average([1,2,3,4]) should return 2.5

"""
def average(nums_list):
    avg=0
    sum=0
    for element in nums_list:
        sum+=element
    avg = sum/len(nums_list)
    return avg
print(average([1,2,3,54]))

"""Length - Create a function that takes a list and returns the length of the list.
Example: length([37,2,1,-9]) should return 4
Example: length([]) should return 0
"""
def length(arr):
    return len(arr)
print(length([]))

"""Minimum - Create a function that takes a list of numbers and returns the minimum value in the list.
 If the list is empty, have the function return False.
Example: minimum([37,2,1,-9]) should return -9
Example: minimum([]) should return False
"""
def minimum(list_num):
    if not list_num:
        return False
    min = list_num[0]
    for num in list_num:
        if num < min:
            min = num
    return min

print(minimum([])) 

"""Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty,
have the function return False.
Example: maximum([37,2,1,-9]) should return 37
Example: maximum([]) should return False"""

def maximum(listEl):
    if not listEl:
        return False
    max = listEl[0]
    for num in listEl:
        if num > max:
            max=num
        return max
print(maximum([]))

"""Ultimate Analysis - Create a function that takes a list and returns a 
dictionary that has the sumTotal, average, minimum, maximum and length of the list.
Example: ultimate_analysis([37,2,1,-9]) should return
 {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
""" 
def ultimate_analysis(listEl):
    sumTotal = 0
    minimum = listEl[0]
    maximum = listEl[0]
    for num in listEl:
        sumTotal += num
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    length = len(listEl)
    average = sumTotal / length
    my_dict = {'sumTotal': sumTotal, 'average': average, 'minimum': minimum, 'maximum': maximum, 'length': length}
    return my_dict

print(ultimate_analysis([37,2,1,-9]))
    
"""Reverse List - Create a function that takes a list and return that list with values reversed.
 Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]"""

def reverse_list(listEl):
    i=0 
    j=len(listEl)-1
    while(i<j):
        temp=listEl[i]
        listEl[i]=listEl[j]
        listEl[j]=temp
        i+=1
        j-=1
    return listEl
print(reverse_list([37,2,1,-9]))
        
        
    