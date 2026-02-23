
d=int(input("Enter a decimal number: "))
r=""
while d > 0:
  r =str(d%2)+r
  d//=2
print(r)
