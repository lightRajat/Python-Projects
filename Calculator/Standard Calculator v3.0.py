from time import sleep
import math

print("                                     Standard Calculator  -by RJ\n\nType 'A' for About.\nType '..' for typing previous result in the caculation.\n'Enter' to Exit.\n\n")

def showCredits():                                              ##Browser Interface Function
    print("\n\n\n                                  Standard Calculator")             #Introduction
    sleep(1)
    print("                                          v2.2")
    sleep(0.75)
    print("                                                          -By Rajat")
    sleep(1.25)

    manual="\nJust type the math expression in the prompt and it's done.\nYou can use Addition(+), Subtraction(-), Multiplication(*), Division(/), Powers/Roots(x**(a/b)) and Brackets(())- all in a single go.\nTo type your previous result in your calculation, just type '..' instead.\nTo End the program, just type 'exit' in the prompt.\nInteresting???"
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
            print("\n1.    Now, don't wait for your mind to suck in the age loading interface of the pervious version. Open it and quickly get your calculation done with our new look, optimised for fast processing.")
            sleep()
            print("\n2.    Instead of going to the alphabet section to type 'Ans', quickly type '..' for getting the previous result.")
            sleep()
            print("\n3.    Type 'A' for Credits and Help. Press Enter, leaving the prompt blank to exit quickly.")
            sleep()
            print("\n4.    Now, this calculator supports '%' symbol which means dividing any number by 100 (i.e. 25%*200=50)")
            sleep()
            print("\n5.    Now you can type '^' symbol too, to raise a number to a power. '**' symbol is still usable to raise number to a power.")
            sleep()
            print("\n6.    So called (mimicked AI) has been improved as you will notice.")
            sleep()
            print("\n7.    Now you can use Factorial and Modulus too.")
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
            sleep(1.25)
            input("\nPress Enter to continue")
        else:
            print("'{}' is not recognised as a valid input. Try Again.".format(guide))
    
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
        if ".." in user:                                                        #Replace ..                                           
            try:
                user=user.replace("..","({})".format(str(result)))
            except:
                print("You are calculating for the first time.\n")
                sleep(1)
                continue
        if "%" in user:                                                        #Replace %
            user=user.replace("%","/100")
        if "^" in user:                                                         #Replace ^
            user=user.replace("^","**")
        try:                                                                    #Replace !
            while "!" in user:
                i=user.find("!")
                if user[i-1]==")":
                    b=user.rfind("(",0,i)
                    user=user.replace(user[b:i+1],"(math.factorial({}))".format(user[b+1:i-1]))
                else:
                    symbol=['+','-','*','/']
                    for o in symbol:
                        s=user.rfind(o,0,i)
                        if not(s==-1):
                            break
                    user=user.replace(user[s+1:i+1],"(math.factorial({}))".format(user[s+1:i]))
        except:
            print("You did not use factorial(!) correctly.Try Again.")
            continue
        try:                                                                    #Replace |
            while "|" in user:
                e=user.rfind("|")
                s=user.rfind("|",0,e)
                user=user.replace(user[s:e+1],"abs({})".format(user[s+1:e]))
        except:
            print("You used the modulus (|) incorrectly.")
            continue
        try:                                                                    #Calculation
            result=eval(user)
            print("You result is {}.".format(result))
        except:
            print("You can only enter math expressions like: 1.5+2*3/4-(54.36-45/4)+25.\nThis calculator follows basic math rules...")
            if x==1:
                x+=1
                sleep(3)
