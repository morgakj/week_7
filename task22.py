# task on operators
# first task oon equal to == operator
print("(confirming password using == comparism operator)")
password = int(input("Enter your password to set security on your device\n>>>>>>>>>>"))
confirm_password = int(input("Re-entered your password to confirm\n>>>>>>>>>"))
if password == confirm_password:
    print("successully login")
else:
    print("access denied entered your password again to login")
print("OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
score = float(input("Please enter your score\n>>>>>>>>>>"))
if score >= 70 and score <=100:
    print("Your grade is A (distiction)")

elif score >=60 and score <70:
    print("your grade is :B (very good)")
elif score >=50 and score <60:
    print("your grade is:C (credit)")
elif score >= 45 and score <50:
    print("your grade is:D (pass)")

else:
    print("your grade: F9 (fail)")
# admission in university base on jamb score
jamb_score = int(input("please enter your jamb score to now the course that you will be ligible to stody"))
if jamb_score >=250 and score <400:
    print("you are ligible to study course like: medicine, Nursing Engineering,Law,pharmacy and lab technician")
elif jamb_score >=180 and score < 200:
    print("you are ligible like: computer science physics, social sudies, languages,educations, chemistry")
else:
    print(" you are not legible")

