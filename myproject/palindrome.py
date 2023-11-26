n = int(input("enter the number:"))  # check the number is palindrome or not
temp = n
rev = 0
while n > 0:
    digit = temp % 10
    rev = (rev * 10) + digit
    n = n// 10
if temp == rev:
    print("the given number is palindrome:", rev)
else:
    print("not a palindrome")
