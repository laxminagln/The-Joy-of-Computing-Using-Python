l1 = input().split()
l2 = input().split()
s1 = ''.join(l1)
s2 = ''.join(l2)
if s2.find(s1) != 0:
    print("No")
else:
    print("Yes")
