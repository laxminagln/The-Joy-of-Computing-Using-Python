(t1,t2,a,b) = (sorted(list(input().upper())),sorted(list(input().upper())),[],[])
for f in t1:
  if f.isalnum():
    a.append(f)
for f in t2:
  if f.isalnum():
    b.append(f)
if a==b:
  print("Yes",end="")
else:
  print("No",end="")
