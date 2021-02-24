(a,s) = (input().split(),0)
for i in range(len(a)):
  for j in range(i+1,len(a)):
    if(int(a[i])>int(a[j])):
      (a[i],a[j],s) = (a[j],a[i],s+1)
print(s,end="")
