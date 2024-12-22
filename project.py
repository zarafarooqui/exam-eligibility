    # if percentage < 75 :- Not Eligible
    #if percentage > 75 :- Eligible
num = int(input("Enter number to check:"))
if num>75:
 print("The student is able to sit in exams")
 if num%2==0:
    print("Number is even")
 else :
    print("Number is odd")
else:
   print("The student is  not able to sit in exams")

