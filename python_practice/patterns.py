num = 10

for i in range(num):
    a=num-i
    b=i
    if(i>=5):
        a=i
        b=num-i
    for k in range(a):
        print(" ",end='')
    
    for j in range(b):
        print("* ",end='')
    print("")