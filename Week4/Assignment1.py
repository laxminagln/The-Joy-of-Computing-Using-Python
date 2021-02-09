a = int(input())
b = int(input())
n = max(a,b)
for i in range(1,n+1):
  if a%i==0 and b%i==0:
    maxi = i
print(maxi)
