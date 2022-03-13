# #while
# x=0
# while (x<5):
#   print(x)
#   x=x+1

# #for
# for x in range(5,10):
#   print(x)

days=["Mon","Tues","Wed","Thurs","Fri"]

#break stops at wed
# for d in days:
#   if(d=="Wed"):break
#   print(d)

#continue skips wed and keeps going
for d in days:
  if(d=="Wed"):continue
  print(d)