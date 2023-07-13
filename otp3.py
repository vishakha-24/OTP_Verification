import random as r
a=r.randrange(0,99999)
print("Your OTP",a)
b=int(input("Enter your OTP:-"))
if b==a:
    print("Login done")
else:
    print("Login fail")


      
