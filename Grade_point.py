marks = input ("Enter Marks:")
m = float (marks)
if (m >= 90):
  print("Outstanding")
  print("Grade Point = 10")
elif (m >= 80):
  print("Excellent")
  print("Grade Point = 9")
elif (m >= 70):
  print("Very Good")
  print("Grade Point = 8")
elif (m >= 60):
  print("Good")
  print("Grade Point = 7")
elif (m >= 50):
  print("Above Average")
  print("Grade Point = 6")
elif (m >= 45):
  print("Average")
  print("Grade Point = 5")
elif (m >= 40):
  print("Poor")
  print("Grade Point = 4")
elif (m < 40):
  print("Fail")
else:
  print("Enter correct marks")
