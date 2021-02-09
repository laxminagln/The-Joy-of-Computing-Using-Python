m = int(input())
n = int(input())
if m+n<=20 and m>n:
  m1=1
  n1=1
  for i in range(1,m+1):
    m1 = m1*i
  for j in range(1,m+2-n):
    n1 = n1*j
  print(int(m1*(m+1)*m1/n1))
else:
  print('invalid')
