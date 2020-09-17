n=int(input()) #4
n=5
for i in range(n*2):
    for j in range(i):
        print("*", end='')
    
    print("")
    for k in range(n*2-i):
        print("*", end='')
    print("")
        
