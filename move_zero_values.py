def linear_search(target,list):
    global count_zeros
    global finals
    for i in range(0, len(list)):
        if target == list[i]:
            count_zeros=count_zeros+1
        else:
            finals.append(list[i])
        
def verify(i):
    if i is not None:
        print("index found at ",i)
    else:
        print("index is not found")

def add_zeros():
    for j in range(count_zeros):
        finals.append(0)
    print(finals)

count_zeros=0
finals=[]
numbers=[0,1,2,3,4,5,6,0,7,8,9]
linear_search(0,numbers)
add_zeros()
# verify(result)




    