st=int(input("Enter a long digit character "))
count=0
while st >0:
  count+=1
  st //= 10
print("number of digits: ",count)
