def binary_search(list,target):
    first=0
    last=len(list)-1 #dalam kasus ini jika tidak dikurangi 1 maka len akan equal to 9
    while first<=last:
        midpoint=last+first//2
        if list[midpoint]<target:
            first=midpoint+1 #jika tidak dikurangi atau di tambah maka first tak akan ketemu last and vice versa 

        elif list[midpoint] == target:
            print("correct")
            return midpoint
        
        elif list[midpoint]>target:
            last=midpoint-1 #jika tidak dikurangi 1 maka index 0 tidak akan pernah ketemu

    return None
    
def verify(index):
    if index is not None:
        print("target found at index: ", index)
    else:
        print("target not found in list")
        

list= [0,1,2,3,4,5,6,7,8]
hasil = binary_search(list, 5)
verify(hasil)