# def bubbleSort(nlist):
#     for passnum in range(len(nlist)-1,0,-1):
#         for i in range(passnum):
#             if nlist[i]>nlist[i+1]:
#                 temp = nlist[i]
#                 nlist[i] = nlist[i+1]
#                 nlist[i+1] = temp

# nlist = []
# l=int(input("Enter the length of the list"))
# for i in range(l):
#     k=int(input("List Value"))
#     nlist.append(k)
# print("Your list is" ,nlist)
    
# bubbleSort(nlist)
# print(nlist)



# maybe this'll be easier to understand
def bubSort(arr):
    n=len(arr)
    # i is for n-1 rounds
    # j is used in each iteration to go till (len-1-i) position
    for i in range(n):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

t=int(input())
for z in range(t):
    li = [int(x) for x in input().split()]
    bubSort(li)
    print(li)
