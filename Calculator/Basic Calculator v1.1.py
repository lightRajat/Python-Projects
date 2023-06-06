from time import sleep
                                                            
print("This is a basic Calculator...")                          #Introduction
sleep(1)
print("             v1.1")
sleep(1)
print("                       -By Rajat Raj")
sleep(1)

while True:                                                     #Main Program
    print("\n\n1. Addition\n2. Multiplication")
    sleep(1)
    while True:                                                 #Prompt for which Operation
        try:                                                    #you want to perform
            op=int(input("Type the serial number of the operator you want to perform: "))
        except:
            print("Enter a valid serial number from 1 to 2...")
            sleep(1)
            continue
        if op>0 and op<3:
            break
        else:
            print("Enter a valid serial number from 1 to 2...")
            sleep(1)
    while True:                                                 #Prompt for how many no.s
        try:                                                    #you want to perform the action with
            noOfSums=int(input("How many numbers you want to perform the operation with: "))
        except:
            print("You must enter a valid positive integer...")
            sleep(1)
            continue
        if noOfSums<0:
            print("You must enter a positive number...")
            sleep(1)
            continue
        else:
            if noOfSums==0:
                print("Okay, Bye...")
                sleep(1)
                exit()
            else:
                if noOfSums>10:
                    print("That's way too much load on me...")
                    sleep(1)
                    continue
                else:
                    break
    nums=[]                                             #Stored numbers
    firstSent="Enter your first number: "
    nextSent="Enter your next number:"
    result=None
    x=0

    nums.append(float(input(firstSent)))            #Prompts for storing numbers
    while x<noOfSums:
        nums.append(float(input(nextSent)))
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
                
    print("3...")                                           #Ending and Result
    sleep(0.5)
    print("2..")
    sleep(0.5)
    print("1.")
    sleep(0.5)
    print("And your resultant number is {}.".format(result))
    sleep(2)
    
    rest=input("Do you want to resetart the thing? ")       #Restart prompt
    if "y" in rest:
        print("As you wish...")
        sleep(1)
        continue
    else:
        print("Okay, Byee...")
        sleep(1.5)
        exit()
    
    
