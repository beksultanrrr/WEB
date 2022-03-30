def  Xor( x, y):
  if x==True and y==False:
    return True;
  elif x==False and y==True:
      return True
  else:
    return False;

a,b=map(int,input().split())
if Xor(a,b)==True:
  print(1)
else:
  print(0)