list = [1,2,3,4,5,6]
a=0

# # problem 1
# for i in range(len(list)):
    
#     if(a<list[i]):
#         a=list[i]

# print(a)


# # problem 2

# list2 = []

# for i in range(len(list)):
#     for j in range(len(list)):
#         a=0
#         if(a<list[j]):
#             a=list[j]
#     list2.append(a)
#     list.pop()
#     a=0
# print(list2)

# problem 3
# find second biggest number
biggest=[2,4,7,5,8,3]
arange=[]

a=0
for i in range(len(biggest)):
    a=biggest[i]
    for j in range(len(biggest)):
        if(a>biggest[j]):
            a=biggest[j]
    arange.append(a)
    
    a=0
print(arange)



