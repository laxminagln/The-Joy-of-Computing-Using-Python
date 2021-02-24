(l1,t,l2,c) = (input(),"","","")
for e in list(l1):
  t+=chr((ord(e)-65+3)%26+65)
for e in list(t)[::-1]:
  l2+=e
for e in list(l2):
  if e=='A':
    c+='U'
  elif e=='B':
    c+='V'
  elif e=='C':
    c+='W'
  elif e=='D':
    c+='X'
  elif e=='E':
    c+='Y'
  elif e=='F':
    c+='Z'
  else:
    c+=chr(ord(e)-6)
print(c,end="")
