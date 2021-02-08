(N, q, a) = (input(), [], [])
q = N.split(" ")
for e in q:
  if e not in a:
    a.append(e)
for i in range(0, len(a)):
  if i != len(a)-1:
    print(a[i], end=" ")
  else:
    print(a[i], end="")
