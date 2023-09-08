def isleapyear(year):
  if (year% 4 == 0 and year % 100!=0)or year % 400 == 0:
    return True 
  else:
    return False 
    year=2012
year=(int(input("Enter the year:")))
if isleapyear (year):
  print('{}is a Leapyear'. format(year))
else:
  print('{} is not a Leapyear'. format(year))
