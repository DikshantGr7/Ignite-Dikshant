#Day 1 Python Basics

#Variables
x = 5
user_name = "Dikshant"
#Dynamic Typing
#Naming conventions : case-sensitive,no spaces,no keywords,should not start with a number,can use underscore
snake_case_variable = "snake case"
PascalCaseVariable = "Pascal case"
camelCaseVariable = "camel case"

#Data Types
a = 5
print(type(a))
b = 5.0
print(type(b))
c = -1+4j
print(type(c))
d = "Hello World"
print(type(d))
e = True
print(type(e))

#Type Casting(Explicit Type Conversion)
f = str(a)
print(type(f),f)
g = int(b)
print(type(g),g)

#Implicit and Explicit Type Conversion
print(a + b)

#Operators

#Arithmetic Operators
z = 10
k = 13
l = 10
print(z+k,z-k,z*k,z/k,z%k,z**k,z//k)

#Comparison Operators
print(z>k,z<k,z>=k,z<=k,z==k,z!=k)

#Logical Operators
print(5>2 and 3>2)
print(not(3<2))
print(5>2 or 3<2)

#Assignment Operators
z += 5
k -= 3
print(z,k)
z *= 3
k /= 2
print(z,k)
z **=2
print(z)

#Membership Operators 
j = "Jack of all trades"
print("Jock"in j,"Jack "not in j)

#Identity Operators
print(z is k,z is not k)

p = 10
print(p == l)

#Bitwise Operators
q = 6
w = 3
print(q & w,q | w,q^w,q<<w,q>>w)
flags = 0b0100 
flags |= 0b0001 
print(flags)
flags &= ~0b0100 
print(flags)
flags <<= 2    
print(flags)
# BITWISE AND (&): Returns 1 only if both corresponding bits are 1; otherwise returns 0.
# BITWISE OR (|): Returns 1 if at least one of the corresponding bits is 1; otherwise returns 0.
# BITWISE XOR (^): Returns 1 if the corresponding bits are different; returns 0 if they are identical.
# BITWISE NOT (~): Inverts all bits (0 to 1, 1 to 0), evaluating mathematically to -(x + 1) due to two's complement.
# BITWISE LEFT SHIFT (<<): Shifts bits to the left by n positions, appending zeros on the right (multiplies by 2^n).
# BITWISE RIGHT SHIFT (>>): Shifts bits to the right by n positions, discarding overflow bits (floor divides by 2^n).

#walrus operator(: =)
if (n := len(input("Type something: "))) > 0:
    print(f"You entered {n} characters.")

if (n := int(input("Enter a number:"))) >= 18:
    print("You are eligible to vote")


#Ternary Operators
age = int(input("Enter your age :"))
print("You are eligible to vote" if age >= 18 else "You are a minor")