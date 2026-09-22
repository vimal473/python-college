def fectorial(n):
    if n <= 1:
        return 1
  else:
       return n * factorial(n - 1)

num = 30
result = factorial(num)

print("Factorial of",num,"=",result)
