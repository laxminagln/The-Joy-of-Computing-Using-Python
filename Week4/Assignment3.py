n = int(input())
k=1
for i in range(1,n+1):
  for j in range(i,i+i):
    print(k**2,end=" ")
    k+=1
  print("")
