n = int(input())
for i in range(n-1):
  for j in range(1, n):
    print(i*n+j,end=' ')
  print(i*n+n)
i = n-1
for j in range(1,n):
  print(i*n+j,end=' ')
print(i*n+n,end='')
