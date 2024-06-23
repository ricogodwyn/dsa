def linear_search(target,list):
    for i in range(0, len(list)):
        if target == list[i]:
            return i
        
def verify(i):
    if i is not None:
        print("index found at ",i)
    else:
        print("index is not found")

numbers=[0,1,2,3,4,5,6,7,8,9]
result=linear_search(1,numbers)
verify(result)




    