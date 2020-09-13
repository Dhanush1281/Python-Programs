name = input("Enter the name:")
unit = float (input("Enter the units:"))
m=100
if (unit<=200):
  charge = ((unit*0.80) + m)
  if (charge > 400):
      charge = ((charge) + (charge*0.15))
elif (unit<=300 and unit>200):
  x= float (unit-200)
  charge = ((200*0.80) + (x*0.90) + (m))
  if (charge > 400):
      charge = ((charge) + (charge*0.15))
elif (unit>300):
  x = unit-300
  charge = ((200*0.80) + (100*0.90) + (x*1) + (m))
  if (charge > 400):
      charge = ((charge) + (charge*0.15))
print("Name:", name)
print("Unit:", unit)
print("Charge:", charge)
