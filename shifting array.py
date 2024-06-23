def shift_left(list):
    print(list[1:]+[list[0]])
    
def shift_right(list,rep):
    for j in range(len(list)):
        for i in range(rep):
            list[j]=[list[j][-1]]+list[j][:-1]
        return list
    
def shift_down(list,rep):
    for j in range(rep):
        list=[list[-1]]+list[:-1]
    return list
numbers_2d = [
    [0, 1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10, 11],
    [12, 13, 14, 15, 16, 17]
]
shifted_numbers=shift_down(numbers_2d,1)
print(shifted_numbers)
