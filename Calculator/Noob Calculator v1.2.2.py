from time import sleep
                                                            
print("                                     Noob Calculator")                          #Introduction
sleep(1)
print("                                          v1.2.2")
sleep(0.75)
print("                                                          -By RJ")
sleep(1.25)

while True:                                                     #What's new prompt
    new=input("\nDo you want to see 'WHAT'S NEW' in v1.2? ").strip()
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
            print("\n1.   The name has been changed from BASIC CALCULATOR to NOOB CALCULATOR.")
            sleep(3.25)
            print("2.   Now you can use fractions too, instead of just plain numbers.")
            sleep(2.75)
            print("3.   AI, (or I should say, immitation of AI) has been improved, as you will notice soon.")
            sleep(4)
            print("4.   Capacity for calculating numbers has been increased to its double size.")
            sleep(3.5)
            print("5.   Looks has been improved a little bit.")
            sleep(2)
            print("6.   New instructions for the calculator has been added.")
            sleep(2.75)
            input("\nPress enter to continue")
            break

                                                                     #Manual Prompt           
manual="\nHI...\nThis is a basic calculator.\nYou fisrt have to choose which whether you want to perform Addition or Multplication.\nThen you can specify how many numbers you want to play with.\nThen, done. Your result will be printed.\nIf you want to subtract a thing in addition, you can just put a NEGATIVE symbol before the number.\n You can also use the negative sign in multiplication, which in that case will give you a negative result, if you use '-' symbol odd number of times.\nYou can also use fractions by entering numerator followed by a '/' symbol followed by denominator.\n You can use fractions in both the operations.\nIn sum, you can perform all the 4 major operations.\nYou can only use 20 numbers to calculate.That's all..."
while True:
    inst=input("\nDo you want to see HOW-TO manual of this noob calculator? ").strip()
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

while True:                                                     #Main Program
    print("\n\n1. Addition\n2. Multiplication")
    sleep(1.5)
    while True:                                                 #Prompt for which Operation
        try:                                                    #you want to perform
            op=int(input("\nType the serial number of the operator you want to perform: "))
        except:
            print("Enter a valid serial number (1 or 2)...")
            sleep(1)
            continue
        if op>0 and op<3:
            break
        else:
            print("Enter a valid serial number (1 or 2)...")
            sleep(1)
    while True:                                                 #Prompt for how many no.s
        try:                                                    #you want to perform the action with
            numbers=int(input("\nHow many numbers you want to perform the operation with: "))
        except:
            print("You must enter a valid positive integer...")
            sleep(1)
            continue
        if numbers<0:
            print("You must enter a positive number...")
            sleep(1)
            continue
        else:
            if numbers==0:
                print("Okay, Bye...")
                sleep(1)
                exit()
            else:
                if numbers>20:
                    print("That's way too much load on me...")
                    sleep(1)
                    continue
                else:
                    break
    nums=[]                                             #Stored numbers
    result=None                                         #Final Result of operation

    x=1                                                 #Prompts for asking and storing numbers in the nums[] list
    while x<=numbers:                                #Loop for the number of times the user wants the numebr prompts 
        if x==1:
            position="first"
            print("")
        elif x==2:
            position="next"
        elif x==numbers:
            position="last"
            
        while True:                                    #Loop for re-prompts if user inputs anything weird
            user=input("Enter your {} number: ".format(position))
            if "/" in user:
                if user.count("/")>1:
                    print("(You can use fractions like- 1/2, 4/6 or a/b)\n")
                    continue
                else:
                    try:
                        num, den=user.split("/")
                        nums.append(float(num)/float(den))
                        break
                    except:
                        print("You can only use numbers or inputs of the format- 1st num/2nd num (if you want to use fractions)...\n")
                        continue                
            else:
                try:
                    nums.append(float(user))
                    break
                except:
                    print("You can't use anything else other than numbers...\n")
                    continue
        x+=1
        
    if op==1:                                           #Do the main operation
        result=0                                        #...Addition                      
        for x in nums:
            result=result+x
    else:                                               #...Multiplication
        for x in nums:
            result=1
            for x in nums:
                result=result*x
                
    print("\n3...")                                           #Ending and Result
    sleep(0.5)
    print("2..")
    sleep(0.5)
    print("1.\n")
    sleep(0.5)
    print("And your resultant number is {}.\n".format(result))
    sleep(2)
    
    while True:                                                         #Restart Prompt
        rest=input("Do you want to restart the thing? ").strip()      
        if not(rest.isalpha()):
            print("I don't understand...\n")
            sleep(1)
            continue
        else:
            if not("y" in rest):
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
            else:
                print("As you wish...\n")
                sleep(1.5)
                break
    continue
