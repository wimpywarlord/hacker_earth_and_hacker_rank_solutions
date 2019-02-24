def prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    print ('\t',f)
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True
z=prime(100)
if z==True:
    print("WORKS")
else:
    print("FAIL")
