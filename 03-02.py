for i in range(0, 6):
    for j in range(0, 6):
        if i == 0 or i == 5 or j == 0 or j == 5:
            print ('* ', end='')
        else:
            print ('  ', end='')
    print()



for i in range(0, 6):
    for j in range(0, 6):
        if i >= j:
            print ('* ', end='')
        # else:
        #     print ('  ', end='')
    print()


for i in range(4, -1, -1):
    #i = i - 1
    for j in range(0, 5):
        if i >= j:
            print ('* ', end='')
        # else:
        #     print ('  ', end='')
    print()    


print (range(6, 0, -1))
print(list(range(6, 0, -1)))



# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * * 
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *


for i in range(0, 6):
    for j in range(0,6):
        if j >= 5 - i:
            print("* ", end = "")
        else:
            print("  ", end='')
    print()



#n - j - 1 => (n-1) - j
#2, 0 => 2 - 0
#0, 2 => 2 - 2
# 2, 2 => (3 - 1) - j 
# i = (n-1) - j
# j = (n-1) - i
# j = (6 - 1) - i


num1 = 1
for i in range(0, 6):

    for j in range(0, 6):
        if i >= j:
            print (num1, ' ', end='')
            num1 += 1
            
        # else:
        #     print ('  ', end='')
        
    print()
