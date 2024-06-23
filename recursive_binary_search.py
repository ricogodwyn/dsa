def recursive_binary_search(list,target):
    if len(list) == 0:
        return False
    elif target not in numbers:
         return False
    else:
        midpoint=len(list)//2
        if list[midpoint] == target: #compare hasil index dengan target list[midpoint] berarti nilai dalam index
            return True
        else:
            if list[midpoint]<target:
                return recursive_binary_search(list[midpoint:],target)
            else:
                return recursive_binary_search(list[:midpoint], target)
def verify(result):
        print("target found: ", result)
    

numbers = [0,1,2,3,4,5,6,7,8]
result = recursive_binary_search(numbers,9)
verify (result)
        