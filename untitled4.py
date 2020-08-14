a = int(input())

for i in range(1,a+2): 
    print((' '*(i-1)+'*'*(a+1-i))+('*'*(a+1-i)))
for i in range(1,a+1): 
    print(((a+1-(6-i))*'*')+(' '*(6-i)+'*'*a))
#for i in range(1,a+1): 
    #print(' '*(i-1)+'*'*(a+1-i))