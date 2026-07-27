totalchores = 5 
originalcount = totalchores 
print(f"you have {originalcount} chores to finish today") 
completedcounts = 0
chorenumber = 1 
while chorenumber <= totalchores : 
    if chorenumber ==1 : next_chore = "make a bed" 
    elif chorenumber ==2 : next_chore = "pack your toys inside the drawer"
    elif chorenumber ==3 : next_chore = "chop the vegetables" 
    elif chorenumber ==4 : next_chore = "iron the clothes"
    else : nextchore = "sweep and mop the house " 
    ans = input(f"HAVE YOU FINISHED {next_chore} ? (yes/no) :-") 
    if ans =="yes":
        completedcounts += 1 
        chorenumber += 1 
        print("GREAT JOB CHORE COMPLETED")
    else: 
        print("FINISH THE CHORE ELSE YOU ARE A LOSER")
    print("CHORES REMAINING",totalchores - completedcounts )  

    testvalue = 0 
safetycounter = 0  
while testvalue <= 0:
    print("this condition never changes") 
    safetycounter+=1 
    if safetycounter ==200:
        print("stop being here on purpose")
        break 
