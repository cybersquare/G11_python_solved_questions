# Write the program in Python to shift the negative numbers to left and the positive numbers to right so that the resultant list will be as follows :
# Original list [-2,1,-3,-15,16,-17,5,-3,-6]
# Output should be [1,16,5,-6,-3,-17,-15,-3,-2]

# Function to rearrange numbers
def rearrange(arr, n ) :
    j = 0
    for i in range(0, n) :
        if (arr[i] > 0) :
            temp = arr[i]
            arr[i] = arr[j]
            arr[j]= temp
            j = j + 1
    print(arr)
 
# Main program
arr = [-2,1,-3,-15,16,-17,5,-3,-6]
n = len(arr)
rearrange(arr, n)
