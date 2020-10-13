#Write a program to remove duplicate elements in a list.

#function to remove duplicates
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: #iterate through each element in the original list
        if num not in final_list: #add list element into final_list if it is not repeats 
            final_list.append(num) 
    return final_list 
       
list1 = [2, 4, 10, 20, 5, 2, 20, 4]  
print("List after removing duplicates: ",Remove(list1)) #calls ficntion to remove duplicates