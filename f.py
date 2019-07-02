r=int(input())
r==2
print("yes")
for i in range(2,r):
    d=r%i
    if d==0:
        print("no")
        break
    else:
        print("yes")
        break
