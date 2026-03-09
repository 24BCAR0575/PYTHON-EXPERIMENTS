 #AIM:Demonstrate Various Data Types And Operators In Python.
a=10
b=5
print("\nEquation Assignment Operators:\n")
print((a+b)**2==(a**2+2*(a*b)+b**2))
print((a-b)**2==a**2-2*(a*b)+b**2)
print((a+b)*(a+b)==2*(a**2-b**2))
print((a+b)*(a-b)==a**2-b**2)
print(a**3+b**3==(a+b)*(a**2-a*b+b**2))

print("\nBitwise Operators:\n")
print((a|b)==(a^b)+(a&b))
print(a^(a&b)==(a|b)^b)
print(b^(a&b)==(a|b)^a)
print((a&b)^(a|b)==(a^b))

print("\nAddition using bitwise operators:\n")
print((a+b)==(a|b)+(a&b))
print((a+b)==(a^b)+2*(a&b))

print("\nSubtraction using bitwise operators:\n")
print((a-b)==(a^(a&b))-((a|b))^a)
print((a-b)==((a|b)^b)-((a|b))^a)
print((a-b)==(a^(a&b))-(b^(a&b)))
print((a-b)==((a|b)^b)-(b^(a&b)))

print("\nArithmetic Operators:\n")
c=20
d=15
print("Addition:",c+d)
print("Subtraction:",c-d)
print("Multiplication:",c*d)
print("Division:",c/d)
print("Modulus:",c%d)

print("\nRelational Operators:\n")
e=30
f=20
print("e>f:",e>f)
print("e>f:",e<f)
print ("e==f:",e==f)
print("e!=f:",e!=f)