(a,k,q,maxi,mini) = (input().split(),int(input()),[],[],[])
for y in a:
  q.append(int(y))
(max_a,min_a) = (sorted(q,reverse=True),sorted(q))
for m in max_a:
  if m not in maxi:
    maxi.append(m)
for z in min_a:
  if z not in mini:
    mini.append(z)
print(maxi[k-1]+mini[k-1],end="")
