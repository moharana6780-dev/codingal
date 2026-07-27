testvalue = 0 
safetycounter = 0  
while testvalue <= 0:
    print("this condition never changes") 
    safetycounter+=1 
    if safetycounter ==200:
        print("stop being here on purpose")
        break 
