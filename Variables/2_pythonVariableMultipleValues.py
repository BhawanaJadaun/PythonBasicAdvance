# Many Value to Multiple variable
x = "orange"
y = "banana"
z = "apple"
x,y,z = "orange","banana","apple"
print(x)
print(y)
print(z)
x = y = z = "orange"
print(x)
print(y)
print(z)
fruits = ["orange","banana","apple"]
x,y,z = fruits
print(x)
print(y)
print(z)
# Output Variable
x = "My name is sharad"
print(x)
x = "my"
y = "name"
z = "is sharad"
print(x,y,z)
x = "my "
y = "name "
z = "is sharad"
print(x + y + z)
x = "10 " #TypeError: can only concatenate str (not "int") to str (we can add str and int)
y = 20
z = 30
print(x * y + z)