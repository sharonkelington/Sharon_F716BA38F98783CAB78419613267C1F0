#Finding factorial
def fact(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact(n-1)
number=5
result=fact(number)
print("The factorial of {} is {}".format(number,result))