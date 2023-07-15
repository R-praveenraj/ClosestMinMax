#Given an array A, 
#find the size of the smallest subarray such that it contains 
#at least one occurrence of the maximum value of the array 
#and at least one occurrence of the minimum value of the array.
#Input    A = [1, 3, 2]   Output  2

def min_max(array):
    mini=float('inf')
    maxi=-float('inf')
    length=len(array)
    for i in range(length):
        if array[i]<mini:
            mini=array[i]
        elif array[i]>maxi:
            maxi=array[i]
    r_min=-1
    r_max=-1
    result=length
    for i in range(length):
        if array[i]==maxi:
            r_max=i
            if r_min>=0:
                result=min(result,i-r_min+1)
        elif array[i]==mini:
            r_min=i
            if r_max>=0:
                result=min(result,i-r_max+1)
    return result

array = [1, 3, 2]
print(min_max(array))