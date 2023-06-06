from time import sleep
import math

print("                                     Scientific Calculator  -by RJ\n")
sleep(0.5)
print("\nType 'A' for About.")
print("Type '..' for typing previous result in the caculation.")
print("'Enter' to Exit.\n")
sleep(0.5)

def showCredits():                                              ##Browser Interface Function
    print("\n\n\n                                  Scientific Calculator")             #Introduction
    sleep(1)
    print("                                          v3.2")
    sleep(0.75)
    print("                                                          -By Rajat")
    sleep(1.25)

    manual="\nUse Addition(+), Subtraction(-), Multiplication(*), Division(/) and Brackets(())\nUse .. to replace with previous answer.\nPress Enter without any input to exit.\nUse % to divide a number by 100\nUse ^ or ** to raise a number to a power\nUse a number between |x| to find its Modulus or Absolute Value\nUse trig Functions like by putting the angle in brackets: sin(x), cos(x) or tan(x). If you are using degrees in your calculation, just type 'd' in front a number: 45d, -180d or 90d etc, otherwise the number in trig brackets will be considered as radians.\nWrite 'pi' or 'PI' or 'Pi' or 'pI' to use Pi constant, 'e' or 'E' to use e constant and 'tau' or 'tu' for tau constant.\nUse ! after a number to raise its factorial.\nUse all of the above in combination of complex calculations to see the magic of computers."
    while True:
        guide=input("\nType 'help', 'whatsNew', 'feedback' or Enter to exit: ").strip().lower()
        if guide=="":                                                               #Exit
            break
        elif "help" in guide:                                                       #Manual
            sleep(0.7)
            print(manual)
            sleep(5)
            input("\nPress Enter to continue")
            sleep(0.75)
        elif "whatsnew" in guide:                                                 #Whats-new?
            sleep(0.7)
            print("\nUnder Development...See you soon.\n")
            input("\nPress enter to continue")
        elif "feedback" in guide:                                               #Feedback.
            print("\nYou can give your valuable CONSTRUCTIVE FEEDBACK to us at the following address.\n")
            sleep(3.25)
            print("\nRajat, 7355716011")
            sleep(1.5)
            print("HQ- My Sweet Home\nSGPGI, Lucknow")
            sleep(1.5)
            print("RJ Pvt Ltd")
            sleep(1.5)
            print("\n\nSorry, Pvt Ltd vali baat mazaak thi.")
            sleep(3)
            print("LOL")
            input("\nPress Enter to continue")
        else:
            print("'{}' is not recognised as a valid input. Try Again.".format(guide))

def findSym(x,y,z):                                                      ##Function to find index of a 
    s="a"                                                                   ##symbol
    if z==0:
        for d in range(0,y+1):
            if x[y-d]=="+" or x[y-d]=="-" or x[y-d]=="*" or x[y-d]=="/":
                s=y-d
                break
        if s=="a":
            s=-1
    else:
        for d in range(0,len(x)-y):
            if x[y+d]=="+" or x[y+d]=="-" or x[y+d]=="/" or x[y+d]=="*":
                s=y+d
        if s=="a":
            s=len(user)
    return s

def findall(x,y):                                                       ##Find All Occurence Function                                                        
    i=0
    while True:
        i=x.find(y,i)
        if i==-1:
            return
        yield i
        i+=len(y)
            
x=1
while True:                                           ##Main Program
    user=input("\nType the calculative expression: ").strip().lower()       
    if user=="":                                                    #Exit
        print("Bye.")
        sleep(0.5)
        break
    elif user=="a":                                                 #Go to browser interface
        showCredits()
    else:
                                                                                            ##Indexes..
        listp=[]
        liste=[]
        listt=[]
        listd=[]
        if "pi" in user or "p" in user:                                 #Pi                                        
            user=user.replace("pi","p")
            listp=list(findall(user,"p"))
        if "e" in user:                                                 #e                                          
            liste=list(findall(user,"e"))
                                                                         #Tau
        if "tau" in user or "t" in user:
            user=user.replace("tau","t")
            listt=list(findall(user,"t"))
        if "d" in user:                                                 #Degrees to radians                                     
            listd=list(findall(user,"d"))

        for o in listp:                                                             ##Replacement..
            user=user.replace(user[o],"math.pi")
        for o in liste:
            user=user.replace(user[o],"math.e")
        for o in listt:
            if not(user[o+1]=="a"):
                user=user.replace(user[o],"math.tau")
        for o in listd:
            if user[o-1]==")":
                s=user.rfind("(",0,o)
                org=user[s:o+1]
                rep=user[s+1:o-1]
            else:
                s=user.rfind("(",0,o)
                org=user[s+1:o+1]
                rep=user[s+1:o]
            user=user.replace(org,"math.radians({})".format(rep))

        if ".." in user:                                                        #Replace ..                                           
            try:
                user=user.replace("..","({})".format(str(result)))
            except:
                print("You are calculating for the first time.\n")
                sleep(1)
                continue
        if "%" in user:                                                        #Replace %
            user=user.replace("%","/100")

        trig=['sin','cos','tan']                                                #Replace Trig Functions
        for t in trig:
            occ=list(findall(user,t))
            for o in occ:
                user=user[:o]+"math."+user[o:]
        
        while "^" in user or "**" in user:                                    #Replace ^
            user=user.replace("**","^")
            i=user.find("^")
            if user[i-1]==")":
                s=user.rfind("(",0,i)
                num=user[s+1:i-1]
            else:
                s=findSym(user,i,0)+1
                num=user[s:i]
            if user[i+1]=="(":
                e=user.find(")",i)+1
                exp=user[i+2:e-1]
            else:
                e=findSym(user,i,1)
                exp=user[i+1:e]
            user=user.replace(user[s:e],"math.pow({},{})".format(num,exp))
        
        try:                                                                    #Replace !
            while "!" in user:
                i=user.find("!")
                if user[i-1]==")":
                    b=user.rfind("(",0,i)
                    user=user.replace(user[b:i+1],"math.factorial({})".format(user[b+1:i-1]))
                else:
                    symbol=['+','-','*','/']
                    for o in symbol:
                        s=user.rfind(o,0,i)
                        if not(s==-1):
                            break
                    user=user.replace(user[s+1:i+1],"math.factorial({})".format(user[s+1:i]))
                print(user)
        except:
            print("You did not use factorial(!) correctly.Try Again.")
            continue
        try:                                                                    #Replace |
            while "|" in user:
                e=user.rfind("|")
                s=user.rfind("|",0,e)
                user=user.replace(user[s:e+1],"math.fabs({})".format(user[s+1:e]))
        except:
            print("You used the modulus (|) incorrectly.")
            continue            
                
        try:                                                                    #Calculation
            result=eval(user)
            print("You result is {}".format(round(result,10)))
        except:
            print("You did something wrong.")
            if x==1:
                x+=1
                sleep(3)
                                                                                                                                                                                                                                                                                                                                                                                                                                                     