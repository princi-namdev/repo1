#Gender=input("Enter Gender :--")
#if Gender=="Female":
#   print("You are allowed")
#else:
#   print("sorry you are not allowed")

#week={1:"sunday",2:"monday",3:"tuesday",4:"wednesday",5:"thursday"
      #,6:"friday",7:"saturday"}
#number=int((input("Please enter week number(Between 1-7):")))
#print("Today is", week[number])


day=int(input("Enter the number(1 to 7):--"))
if(day==1):
    print("sunday")
elif(day==2):
    print("monday")
elif(day==3):
    print("tuesday")
elif(day==4):
    print("wednesday")
elif(day==5):
    print("thusrday")
elif(day==6):
    print("friday")
elif(day==7):
    print("saturday")
else:
    print("Not valid")



#marks=int(input("Enter Marks:-"))
#if(marks>=75):
#   print("A grade")
#elif(marks>=60):
#   print("B grade")
#elif(marks>=33):
#    print("C grade")
#else:
#   print("Not pass")

#age=int(input("Enter number:-"))
#if(age<=18):
#   print("Child")
#elif(age>=18 and age<=35):
#   print("Adult")

#abc=int(input("Enter the number:-"))
#if(abc%2==0):
#    print("Even")
#else:
 #    print("odd")

xyz=int(input("Enter the number:--"))
if(xyz%5==0):
    print("Number divisible by 5")
else:
    print("Not valid")

#a=19.5467457
#print("this num is{:.2f}.format{a}")
#print("the num is {a:2f}")

age=int(input("Enter your age:-"))
if(age>=18):
    print("Eligible for Voting")
else:
    print("Not Eligible for Voting")
