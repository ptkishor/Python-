# 1. What are Numerical Types?
# Numerical types are Python data types used to store and perform operations on numbers.

# Python mainly provides three numerical types:
# 1. Integer (int)
# 2. Floating-point (float)
# 3. Complex (complex)


#Integer (int) Data Type
# An integer is a whole number without a decimal point.

a = 10
b = -5
c = 0

print(type(a))


#Floating-point (float) Data Type
# A floating-point number is a number that has a decimal point.

x = 10.5
y = -3.45
z = 3.0

print(type(x))


#Complex (complex) Data Type
# A complex number is a number that has a real part and an imaginary part.


a = 2 + 3j

print(type(a))
print(a.real)
print(a.imag)


#Type Conversion

s = 10
d = float(s)

print(d)
print(type(d))


f = 10.5
i = int(f)

print(i)
print(type(i))


a = 2 + 3j
b = 20.5
c = 200

print(type(a))
print(a.real)
print(a.imag)

print(type(b))
print(b.real)
print(b.imag)

print(type(c))
print(c.real)
print(c.imag)

x = int(b)
y = float(c)

print(x)
print(y)

print("Type of x:", type(x))
print("Type of y:", type(y))
