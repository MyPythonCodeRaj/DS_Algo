def recursive_binary_search(list,target):
    if len(list)==0:
        return False
    else:
        midpoint = len(list)//2
    
    if list[midpoint] == target:
        return True
    elif list[midpoint] < target:
        return recursive_binary_search(list[midpoint+1:], target)
    else:
        return recursive_binary_search(list[:midpoint],target)


def verify(check):
    if check:
        print("Target found")
    else:
        print("Target not found in list")
        
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result_1 = recursive_binary_search(numbers,8)
verify(result_1)

result_2 = recursive_binary_search(numbers,11)
verify(result_2)
