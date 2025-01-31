# list1 = [1, 3, 4, 5, 7]
# list2 = [1, 9]

# flag = False
# for i in list2:
#     if i not in list1:
#         flag = True
#         break

# if flag == False:
#     print ("Is a subset")
# else:
#     print ("Not a subset")
# #O(n square), O(1)





#Target = 14
list1 = [1, 3, 5, 6, 7, 10, 11, 12, 19] #2 pointer approach
# Initially 1 + 19 = 
# 3 + 12 = 
# 3 + 11 = 14

low = 0
high = len(list1) - 1
target = 14


while low < high:
    sum = list1[low] + list1[high]
    if sum == target:
        print("Target found", low, high)
        break
    elif sum > target:
        high -= 1
    else:
        low = low + 1

#T.C - o(nlogn). S.C - O(1)


#Matrix examples

mat1 = [
    [1, 5, 67], 
    [2.2, 3, -2], 
    [4, 9, 10]
    ]

#Matrix sum
# sum = 0
# for i in mat1:
#     print (i)
#     # #print(str(i))
#     for j in i:
#         sum += j

# mat1 = [
#     [1, 2.2, 4], 
#     [5, 3, 9], 
#     [67, -2, 10],
#     # [5, 3, -3]
#     ]



for i in range(len(mat1)):
    print("Check")
    for j in range(i):
        mat1[i][j], mat1[j][i] = mat1[j][i], mat1[i][j]

print(mat1)


for i in range(len(mat1)):
    for j in range(len(mat1)):
        if j < i:
            mat1[i][j], mat1[j][i] = mat1[j][i], mat1[i][j]

print(mat1)
