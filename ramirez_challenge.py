"""
write a program that will ask the user to enter in three legs of a triangle and then test it
"""
a = int(input('please enter side a:'))
b = int(input('please enter side b:'))
c = int(input('please enter side c:'))

if (a**2 + b**2 == c**2):
    print("this is a right triangle")

else:
    print("this is NOT a right triangle")
    
if (a**2 + b**2 == c**2):
    print("this is an obtuse triangle")

else:
    print("this is NOT an obtuse triangle")

if (a**2 + b**2 == c**2):
    print("this is an acute triangle")
    
else:
    print("this is NOT an acute triangle")