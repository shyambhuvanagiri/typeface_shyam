valid_numbers=['0','1','2','5','6','8','9']
n=int(input())
list_=[]
x=1
y=1
while(y<=n):
    string_1=str(x)
    c=0
    for i in string_1:
        if(i in valid_numbers):
            c+=1
    if(c==len(string_1)):
        list_.append(string_1)
        y+=1
    x+=1
f=int(list_[len(list_)-1])
print(f)
