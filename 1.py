input_=int(input())
res=0
i=0
while(input_>0):
    n=int(input_%3)
    res=res+int(n*(int(10**i)))
    input_=input_/3
    i=i+1
print(res)
