n=int(input('enter number: '));
ls = []
for i in range(2,n+1):
    for j in range(2,i):
        if i % j ==0:
            break
    else:
        ls.append(i)

print(ls)

