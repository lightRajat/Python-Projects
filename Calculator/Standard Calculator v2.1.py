from time import sleep
                                                            
print("                                  Standard Calculator")                          #Introduction
sleep(1)
print("                                          v2.1")
sleep(0.75)
print("                                                          -By RJ")
sleep(1.25)

while True:                                                     #What's new prompt
    new=input("\nDo you want to see 'WHAT'S NEW' in v2.1? ").strip()
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
            sleep(0.7)
            print("\n1.    Now you can use Powers(x**y: x raise to the power y) and Roots(x**(1/a): square root of x if a=2; cube root of x if a=3 and so on.) or combination of both.")
            sleep(5)
            print("\n2.    Now you can use your previous result in the calculation by just typing 'Ans' in the prompt, where you need to type the previous answer.")
            sleep(1.5)
            print("\n3.    Type 'exit' instead of 'bye' to quit the program.")
            sleep(2)
            print("\n4.    Improvements in the system efficiency and bug fixes.")
            input("\nPress enter to continue")
            break

                                                                     #Manual Prompt           
manual="\nJust type the math expression in the prompt and it's done.\nYou can use Addition(+), Subtraction(-), Multiplication(*), Division(/), Powers/Roots(x**(a/b)) and Brackets(())- all in a single go.\nTo type your previous result in your calculation, just type 'Ans' instead.\nTo End the program, just type 'exit' in the prompt.\nInteresting???"
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
            sleep(0.7)
            print(manual)
            sleep(5)
            input("\nPress Enter to continue")
            sleep(0.75)
            break

x=1
while True:                                                             #Main Program
    user=input("\nType the calculative expression: ").strip().lower()
    if "ans" in user:
        user=user.replace("ans", str(result))
    try:
        result=eval(user)
        if "exit" in user:
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
            sleep(1.5)
            break
        else:
            print("You result is {}.".format(result))
            sleep(1)
    except:
        sleep(0.7)
        print("You can only enter math expressions like: 1.5+2*3/4-(54.36-45/4)+25.\nThis calculator follows basic math rules...")
        if x==1:
            x+=1
            sleep(3)
        else:
            sleep(0.75)
