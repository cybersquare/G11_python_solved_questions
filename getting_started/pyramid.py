# Create a pyramid of stars using Python

rows = 2

n = 2*rows
# number of spaces 
k = n - 2

# outer loop to handle number of rows 
for i in range(0, n, 2): 
    
    # inner loop to print spaces 
    for j in range(0, k): 
        print(end=" ") 
    
    # decrementing k after each loop 
    k = k - 1
    
    # inner loop to print stars
    for j in range(0, i+1): 
        
        # printing stars 
        print("*", end="") 
    
    # ending line after each row 
    print("\r") 
  

