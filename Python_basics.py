a=int(input('enter the first number:'))
b=int(input('enter the second number:'))
add=a+b
print(add)
sub=a-b
print(sub)
div=a/b
print(div)
mul=a*b
print(mul)
mod=a//b
print(mod)
pow=a**b
print(pow)

#greater number
num1=int(input('enter the first number:'))
num2=int(input('enter the second number:'))
if num1 != num2:
    if num1> num2:
        print(f"{num1} is greater than {num2}")
    else:
         print(f"{num2} is greater than {num1}")
else:
    print("both numbers are equal")

#even odd number
num=int(input('enter the number:'))
if (num %2==0):
    print(f"{num} number is even")
else:
    print(f"{num} is odd number")
        
