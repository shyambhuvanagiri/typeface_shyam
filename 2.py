string_1=input()
string_2=input()
len_string_2=len(string_2)
c=string_2[len_string_2-1]
count=0;
for i in range(0,len(string_1)):
  if(string_1[i]==c):
    count+=1
print(count)
