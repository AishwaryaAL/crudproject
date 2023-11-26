factors = []
n = int(input("enter the number:"))
for i in range(1, n + 1):
    if (n % i == 0):
        factors.append(i)
if len(factors) == 2:
    print("the prime number")
else:
    print("not a prime number")

#factorial number
#create github account
