print("_____________________")
print(" ATM CASH DISPENSER") 
print("______________________")
total100 = total50 = total20 = total10 =total5 = total1 = 0 
customers = 0 
totalmoney = 0 
answer = "YES" 
while answer == "YES" : 
    name = input("ENTER YOUR NAME:-") 
    amount = int(input("ENTER YOUR AMOUNT:-"))
    money = amount 
    while money > 0 :
        if money >=100 :
         print("1 * 100")
         money = money-100
         total100 = total100+1 
        elif money>=50 :
           print("1*50") 
           money = money-50
           total50 = total50+1 
        elif money>=20 :
           print("1*20")
           money = money-20 
           total20 = total20+1 
        elif money>=10:
           print("1*10")
           money = money-10
           total10 = total10+1 
        elif money>=5 :
           print("1*5") 
           money = money-5
           total5 = total5+1
        elif money>= 1 :
           print("1*1")
           money = money-1
           total1 = total1+1 
    customers = customers +1 
    totalmoney = totalmoney+amount 
    answer = input("NEXT CUSTOMER ?(YES/NO):-") 
print("DAILY REPORT")
print("100 NOTES") 
for i in range (total100) :
   print("*",end="")
print() 
print("50 NOTES") 
for i in range (total50) :
   print("*",end="")
print() 
print("20 NOTES") 
for i in range (total20) :
   print("*",end="")
print() 
print("10 NOTES") 
for i in range (total10) :
   print("*",end="")
print() 
print("5 NOTES") 
for i in range (total5) :
   print("*",end="")
print() 
print("1 NOTES") 
for i in range (total1) :
   print("*",end="")
print() 
print("customers served",customers) 
print("totalmoney dispensed",totalmoney)
print("_____________________________________")
print("            ATM CLOSED")
print("_____________________________________") 
