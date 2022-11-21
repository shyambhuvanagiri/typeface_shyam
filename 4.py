m=[]
for e in range(4):
  l=list(map(int,input().split()))
  m.append(l)
li=[]
for i in range(0,4):
  for j in range(0,5):
    if(m[i][j]==0):
      k=[]
      k.append(i)
      k.append(j)
      li.append(k)
o=[]
o.append(li[0])
t=o[0][0]
t1=o[0][1]
for i in range(t1+1,5):
  if(m[t][i]==1):
    t2=[]
    t2.append(t)
    t2.append(i)
    o.append(t2)
l1=len(li)
w=li[l1-1][0]
for i in range(0,5):
  w1=[]
  if(m[w][i]==0):
    w21=[]
    w21.append(w)
    w21.append(i)
    w1.append(w21)
o.append(w1[0])
w2=len(o)
w3=o[w2-1][1]
for i in range(w3+1,5):
  t11=[]
  if(m[w][i]==1):
    t12=[]
    t12.append(w)
    t12.append(i)
    t11.append(t12)
o.append(t11[0])
    break
print(o)
