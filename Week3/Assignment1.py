a = input().split()
s = []
for e in a:
  if e[len(e)-1] != '4':
    s.append(e)
print(*s, end="")
