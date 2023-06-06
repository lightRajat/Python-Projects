from time import sleep
                                                            
print("                                  Standard Calculator")                          #Introduction
sleep(1)
print("                                          v2.0")
sleep(0.75)
print("                                                          -By RJ")
sleep(1.25)

while True:                                                     #What's new prompt
    new=input("\nDo you want to see 'WHAT'S CHANGED' in v2.0? ").strip()
    if not(new.isalpha()):
        print("What???")
        sleep(1.5)
        continue
    else:
        if not("y" in new):
            sleep(0.15)
            print("Okay...")
            sleep(1.5)
            break
        else:
            sleep(1)
            print("\n1.   The name has been changed from NOOB CALCULATOR to STANDARD CALCULATOR.")
            sleep(3.25)
            print("2.    The whole program has entirely been changed. Now you can use this like a standard calculator by entering math expressions of any cosmic length.")
            sleep(6)
            print("3.    There is no restriction on entering number limit.")
            sleep(2.5)
            input("\nPress enter to continue")
            break

                                                                     #Manual Prompt           
manual="\nJust type the math expression in the prompt and it's done.\n You can use Addition(+), Subtraction(-), Multiplication(*), Division(/) and Brackets(())- all in a single go.\nTo End the program, just type 'bye' in the prompt.\nInteresting???"
while True:
    inst=input("\nDo you want to see HOW-TO manual of this standard calculator? ").strip()
    if not(inst.isalpha()):
        print("Please type something that I can predict...")
        sleep(1.75)
        continue
    else:
        if not("y" in inst):
            print("Okay...")
            sleep(1)
            break
        else:
            sleep(1)
            print(manual)
            sleep(5)
            input("\nPress Enter to continue")
            sleep(0.75)
            break

x=1
while True:                                                             #Main Program
    try:
        user=input("\nType the calculative expression: ")
        result=eval(user)
        print("You result is {}.".format(str(result)))
        sleep(1)
    except:
        if not("bye" in user.lower()):
            sleep(0.7)
            print("You can only enter math expressions like: 1.5+2*3/4-(54.36-45/4)+25.\nThis calculator follows basic math rules...")
            if x==1:
                x+=1
                sleep(3)
            else:
                sleep(0.75)
            continue
        else:
            print("See you soon...\n")
            sleep(1.5)
            print("You can give your valuable CONSTRUCTIVE FEEDBACK to us at the following address.\n")
            sleep(3.25)
            print("-\nRajat, 7355716011")
            sleep(1.5)
            print("HQ- My Sweet Home\nSGPGI, Lucknow")
            sleep(1.5)
            print("RJ Pvt Ltd")
            sleep(1.5)
            print("\n\nSorry, Pvt Ltd vali baat mazaak thi.")
            sleep(3)
            print("LOL")
            sleep(1.25)
            print("Byeeeee")
            sleep(2)
            exit()
