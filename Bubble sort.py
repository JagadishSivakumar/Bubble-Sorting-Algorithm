def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

nlist = []
l=int(input("Enter the length of the list"))
for i in range(l):
    k=int(input("List Value"))
    nlist.append(k)
print("Your list is" ,nlist)
    
bubbleSort(nlist)
print(nlist)
