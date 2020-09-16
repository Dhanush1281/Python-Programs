from math import sqrt
a =float (input("Enter 1st variable:"))
b =float (input("Enter 2nd variable:"))
c =float (input("Enter 3rd variable:"))
d = b*b- 4*a*c
if d==0 :
  x1 = x2= -b/(2*a)
  print("Roots are equal")
  print("Root1:", x1)
  print("Root2:", x2)
elif d>0 :
  x1 =(((-b) + sqrt(d))/(2*a))
  x2 =(((-b) - sqrt(d))/(2*a))
  print("Roots are real and distinct")
  print("Root1:", x1)
  print("Root2:", x2)
elif d<0 :
  x1 = x2 = -b / (2 * a)
  i = sqrt(-d) / (2 * a)
  print("Roots are Complex:\nRoot1 = %.2f+i%.2f \nRoot2 = %.2f-i%.2f" %(x1, i, x2, i))
