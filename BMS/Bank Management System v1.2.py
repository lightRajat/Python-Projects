class BMS():

    sqlUser = None
    sqlPass = None
    credentials = []

    def __init__(self):
        self.getServerDetails()
        self.getCredentials()
        self.main()

    def getCredentials(self):
        from mysql.connector import connect

        con = connect(host = 'localhost', user = self.sqlUser, passwd = self.sqlPass, database = 'rajatbms')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM login_credentials;")
        for i in cursor.fetchall():
            self.credentials.append(i)

        con.close()

    def getServerDetails(self):
        with open("DataBase Server.txt", 'r') as f:
            content = f.read().split()
            self.sqlUser = content[1]
            self.sqlPass = content[3]

    def main(self):

        def logChecker(post, user, passwd):
            for i in self.credentials:
                if i[2] == user:
                    if i[1] == post:
                        if i[3] == passwd:
                            self.logWindow.destroy()
                            splashGUI()
                            break
            else:
                self.logPostEntryString.set("Select a Post")
                self.logUserEntry.delete(0, 'end')
                self.logPassEntry.delete(0, 'end')
                self.logWarning['text'] = "* Wrong Credentials..."

        def logGUI():
            
            self.logWindow = Tk()
            self.logWindow.title("Login")

            frame1 = Frame(master = self.logWindow)
            frame1.pack(fill = 'x', pady = 3, padx = 4)
            logPost = Label(master = frame1, text = "Post        :")
            logPost.pack(side = 'left')
            self.logPostEntryString = StringVar()
            self.logPostEntryString.set("Select a Post")
            logPostEntry = OptionMenu(frame1, self.logPostEntryString, *["Manager", "Teller", "Clerk", "Loan Officer", "Personal Banker"])
            logPostEntry.pack(side = 'left')

            frame2 = Frame(master = self.logWindow)
            frame2.pack(fill = 'x', pady = 3, padx = 4)
            logUser = Label(master = frame2, text = "User ID    :")
            logUser.pack(side = 'left')
            self.logUserEntry = Entry(master = frame2)
            self.logUserEntry.pack(side = 'left')

            frame3 = Frame(master = self.logWindow)
            frame3.pack(fill = 'x', pady = 3, padx = 4)
            logPass = Label(master = frame3, text = "Password :")
            logPass.pack(side = 'left')
            self.logPassEntry = Entry(master = frame3, show = '*')
            self.logPassEntry.pack(side = 'left')

            frame4 = Frame(master = self.logWindow)
            frame4.pack(fill = 'x', pady = 3, padx = 4)
            self.logWarning = Label(master = frame4, text = "", fg = 'red', font = ('Calibri', 11, 'italic'))
            self.logWarning.pack(side = 'left')
            logSubmit = Button(master = frame4, text = "Submit", command = lambda: logChecker(self.logPostEntryString.get(), self.logUserEntry.get(), self.logPassEntry.get()))
            logSubmit.pack(side = 'right')

            self.logWindow.mainloop()

        def splashGUI():
            splashWindow = Tk()
            splashWindow.title("Bonjour!")
            splashWindow.geometry('300x125')

            splashf1 = Frame(master = splashWindow)
            splashf1.pack(fill = 'x', pady = 5)
            splashf2 = Frame(master = splashWindow)
            splashf2.pack(fill = 'x', pady = 5)
            splashf3 = Frame(master = splashWindow)
            splashf3.pack(fill = 'x', pady = 5)

            splashNew = Button(master = splashf1, text = "New Account", command = newGUI)
            splashNew.pack()
            splashMoney = Button(master = splashf2, text = "Deposit / Withdrawal", command = monGUI)
            splashMoney.pack()
            splashLoan = Button(master = splashf3, text = "EMI Calculator", command = emiGUI)
            splashLoan.pack()

            splashWindow.mainloop()

        def newGUI():
            self.newWindow = Tk()
            self.newWindow.title("New Account")

            newf1 = Frame(master = self.newWindow)
            newf1.pack(fill = 'x', pady = 3, padx = 5)
            newf2 = Frame(master = self.newWindow)
            newf2.pack(fill = 'x', pady = 3, padx = 5)
            newf3 = Frame(master = self.newWindow)
            newf3.pack(fill = 'x', pady = 3, padx = 5)
            newf4 = Frame(master = self.newWindow)
            newf4.pack(fill = 'x', pady = 3, padx = 5)
            newf5 = Frame(master = self.newWindow)
            newf5.pack(fill = 'x', pady = 3, padx = 5)
            newf6 = Frame(master = self.newWindow)
            newf6.pack(fill = 'x', pady = 3, padx = 5)
            newf7 = Frame(master = self.newWindow)
            newf7.pack(fill = 'x', pady = 3, padx = 5)
            newf8 = Frame(master = self.newWindow)
            newf8.pack(fill = 'x', pady = 3, padx = 5)
            newf9 = Frame(master = self.newWindow)
            newf9.pack(fill = 'x', pady = 3, padx = 5)
            newf10 = Frame(master = self.newWindow)
            newf10.pack(fill = 'x', pady = 3, padx = 5)

            newName = Label(master = newf1, text = "Name :")
            newName.pack(side = 'left')
            newDOB = Label(master = newf2, text = "DOB :")
            newDOB.pack(side = 'left')
            newMobile = Label(master = newf3, text = "Mobile No. :")
            newMobile.pack(side = 'left')
            newMail = Label(master = newf4, text = "Email :")
            newMail.pack(side = 'left')
            newAddress = Label(master = newf5, text = "Address :")
            newAddress.pack(side = 'left')
            newId = Label(master = newf6, text = "ID Type :")
            newId.pack(side = 'left')
            newIdNo = Label(master = newf7, text = "ID No. :")
            newIdNo.pack(side = 'left')
            newNominee = Label(master = newf8, text = "Nominee Name :")
            newNominee.pack(side = 'left')
            newNomineeNo = Label(master = newf9, text = "Nominee ID :")
            newNomineeNo.pack(side = 'left')
            self.newWarning = Label(master = newf10, text = "All fields necessary", fg = 'red', font = ('Calibri', 11, 'italic'))
            self.newWarning.pack(side = 'left')

            self.newNameEntry = Entry(master = newf1)
            self.newNameEntry.pack(side = 'right')
            self.newDOBEntry = DateEntry(master = newf2)
            self.newDOBEntry.pack(side = 'right')
            self.newMobileEntry = Entry(master = newf3)
            self.newMobileEntry.pack(side = 'right')
            self.newMailEntry = Entry(master = newf4)
            self.newMailEntry.pack(side = 'right')
            self.newAddressEntry = Entry(master = newf5)
            self.newAddressEntry.pack(side = 'right')
            self.newIdEntryString = StringVar(newf6)
            self.newIdEntryString.set("Select an Id Type")
            self.newIdEntry = OptionMenu(newf6, self.newIdEntryString, *["Aadhaar Card", "Voter ID Card", "PAN Card", "Driving License", "Ration Card"])
            self.newIdEntry.pack(side = 'right')
            self.newIdNoEntry = Entry(master = newf7)
            self.newIdNoEntry.pack(side = 'right')
            self.newNomineeEntry = Entry(master = newf8)
            self.newNomineeEntry.pack(side = 'right')
            self.newNomineeNoEntry = Entry(master = newf9)
            self.newNomineeNoEntry.pack(side = 'right')
            self.newSubmit = Button(master = newf10, text = "Sumbit", command = lambda: createAcc(self.newNameEntry.get(), self.newDOBEntry.get_date(), self.newMobileEntry.get(), self.newMailEntry.get(), self.newAddressEntry.get(), self.newIdEntryString.get(), self.newIdNoEntry.get(), self.newNomineeEntry.get(), self.newNomineeNoEntry.get()))
            self.newSubmit.pack(side = 'right')

            self.newWindow.mainloop()

        def createAcc(name, dob, mobile, mail, add, idtype, idno, nom, nomno):

            def clearNewGUI(warning):
                widgets = [self.newNameEntry, self.newMobileEntry, self.newMailEntry, self.newAddressEntry, self.newIdNoEntry, self.newNomineeEntry, self.newNomineeNoEntry]
                for i in widgets:
                    i.delete(0, 'end')
                self.newIdEntryString.set("Select an Id Type")
                self.newWarning['text'] = warning

            def createAccNo():
                from mysql.connector import connect
                con = connect(host = 'localhost', user = self.sqlUser, passwd = self.sqlPass, database = 'rajatbms')
                cursor = con.cursor()
                cursor.execute("SELECT account_number FROM user_accounts;")
                AccNo = []
                for i in cursor:
                    AccNo.append(i[0])
                con.close()
                
                while True:
                    self.acc = ""
                    for i in range(15):
                        self.acc += str(randint(0,9))
                    if self.acc in AccNo:
                        continue
                    else:
                        break
                data.append(self.acc)

            data = [name, dob, mobile, mail, add, idtype, idno, nom, nomno]
            if "" in data:
                clearNewGUI("All fields necessary")
            elif len(name) > 30:
                clearNewGUI("Enter a Valid Name")
            elif not(mobile.isdigit()) or len(mobile) != 10:
                clearNewGUI("Enter 10 digit, numeric mobile number")
            elif ('@' not in mail) or (mail[-4:] != '.com') or (len(mail) > 30):
                clearNewGUI("Invalid Email")
            elif len(mail) > 125:
                clearNewGUI("Invalid Address")
            elif idtype == 'Select an Id Type':
                clearNewGUI("No ID Selected")
            elif len(nom) > 30:
                clearNewGUI("Enter Valid Nominee Name")
            elif not(nomno.isdigit()):
                clearNewGUI("Enter a valid Nominee ID")
            else:
                createAccNo()

                from mysql.connector import connect
                con = connect(host = 'localhost', user = self.sqlUser, passwd = self.sqlPass, database = 'rajatbms')
                cursor = con.cursor()
                cursor.execute("INSERT INTO user_accounts VALUES (DEFAULT, '{}', '{}', {}, '{}', '{}', '{}', {}, '{}', {}, {}, DEFAULT);".format(name, dob, mobile, mail, add, idtype, idno, nom, nomno, self.acc))
                con.commit()
                con.close()

                self.newWindow.destroy()
                winGUI()

        def winGUI():
            winWindow = Tk()
            winWindow.title("Congratulation")

            winLab1 = Label(master = winWindow, text = "Congratulations! Account Successfully Created.")
            winLab1.pack(fill = 'x', padx = 5, pady = 3)
            winLab2 = Label(master = winWindow, text = "Your Account Number is :")
            winLab2.pack(fill = 'x', padx = 5, pady = 3)
            winLab3 = Label(master = winWindow, text = "{}".format(self.acc), font = ('Comic Sans MS', 15, 'bold'))
            winLab3.pack(fill = 'x', padx = 5, pady = 3)
            winLab4 = Label(master = winWindow, text = "Please note down this number for further references.", fg = 'red', font = ('Calibri', 11, 'italic'))
            winLab4.pack(fill = 'x', padx = 5, pady = 3)
            winBut5 = Button(master = winWindow, text = "OK!", command = lambda: winWindow.destroy())
            winBut5.pack(fill = 'x', padx = 5, pady = 3)

            winWindow.mainloop()

        def monGUI():

            def sentNotif():
                self.monLog['text'] = "OTP sent to your registered mobile number"
            
            self.monWindow = Tk()
            self.monWindow.title("Deposit / Withdrawal")
            self.monWindow.geometry('350x175')

            monf1 = Frame(master = self.monWindow)
            monf1.pack(fill = 'x', padx = 5, pady = '3')
            monf2 = Frame(master = self.monWindow)
            monf2.pack(fill = 'x', padx = 5, pady = '3')
            monf3 = Frame(master = self.monWindow)
            monf3.pack(fill = 'x', padx = 5, pady = '3')
            monf4 = Frame(master = self.monWindow)
            monf4.pack(fill = 'x', padx = 5, pady = '3')
            monf5 = Frame(master = self.monWindow)
            monf5.pack(fill = 'x', padx = 5, pady = '3')

            monType = Label(master = monf1, text = "Transaction Type  :")
            monType.pack(side = 'left')
            monAcc = Label(master = monf2, text = "Account Number  :")
            monAcc.pack(side = 'left')
            monAmt = Label(master = monf3, text = "Amount               :")
            monAmt.pack(side = 'left')
            monPin = Label(master = monf4, text = "OTP                    :")
            monPin.pack(side = 'left')
            self.monLog = Label(master = monf5, text = "", fg = 'red', font = ('Calibri', 11, 'italic'))
            self.monLog.pack(side = 'left')

            self.monTypeEntryString = StringVar(monf1)
            self.monTypeEntryString.set("D / W ?")
            monTypeEntry = OptionMenu(monf1, self.monTypeEntryString, *["Deposit", "Withdrawal"])
            monTypeEntry.pack(side = 'right')
            self.monAccEntry = Entry(master = monf2, width = 25)
            self.monAccEntry.pack(side = 'right')
            self.monAmtEntry = Entry(master = monf3, width = 25)
            self.monAmtEntry.pack(side = 'right')
            monSend = Button(master = monf4, text = "Send OTP", command = sentNotif)
            monSend.pack(side = 'right')
            self.monPinEntry = Entry(master = monf4, show = '*', width = 15)
            self.monPinEntry.pack(side = 'right')
            monSubmit = Button(master = monf5, text = "Proceed", command = lambda: moneyTransfer(self.monTypeEntryString.get(), self.monAccEntry.get(), self.monAmtEntry.get(), self.monPinEntry.get()))
            monSubmit.pack(side = 'right')

            self.monWindow.mainloop()

        def moneyTransfer(montype, acc, amt, pin):

            def clearMonGUI(warning):
                widgets = [self.monAccEntry, self.monAmtEntry, self.monPinEntry]
                for i in widgets:
                    i.delete(0, 'end')
                self.monTypeEntryString.set("D / W ?")
                self.monLog['text'] = warning
                
            data = [montype, acc, amt, pin]
            valid = True
            if "" in data or montype == "D / W ?":
                clearMonGUI("Invalid Entries")
                valid = False
            else:
                for i in range(1, 4):
                    if not(data[i].isdigit()):
                        clearMonGUI("Invalid Entries")
                        valid = False
                        break

            if valid:
                from mysql.connector import connect
                con = connect(host = "localhost", user = self.sqlUser, passwd = self.sqlPass, database = 'rajatbms')
                cursor = con.cursor()
                cursor.execute("SELECT record_id FROM user_accounts WHERE account_number = {};".format(acc))
                found = False
                for i in cursor:
                    found = True
                if not(found):
                    clearMonGUI("User Not Found...")
                else:
                    findb = None
                    if montype == 'Deposit':
                        cursor.execute("UPDATE user_accounts SET balance = balance + {} WHERE account_number = {};".format(amt, acc))
                        con.commit()
                        findb = 'td'
                    else:
                        cursor.execute("SELECT balance FROM user_accounts WHERE account_number = {};".format(acc))
                        for i in cursor:
                            initBalance = i[0]
                        if initBalance < float(amt):
                            clearMonGUI("Failed. Current Balance: {}".format(initBalance))
                        else:
                            cursor.execute("UPDATE user_accounts SET balance = balance - {} WHERE account_number = {};".format(amt, acc))
                            con.commit()
                            findb = 'tw'
                if findb[0] == 't':
                    cursor.execute("SELECT balance FROM user_accounts WHERE account_number = {};".format(acc))
                    for i in cursor:
                        currBalance = i[0]
                    con.close()

                    self.monWindow.destroy()
                    transGUI(currBalance, findb[1], amt)

        def transGUI(balance, source, amt):
            if source == 'd':
                src = "Deposited"
            else:
                src = "Withdrawn"
            
            transWindow = Tk()
            transWindow.title("Transaction Complete")
            transWindow.geometry('220x120')

            l1 = Label(master = transWindow, text = "Amount Successfully {}".format(src))
            l1.pack(fill = 'x', padx = 5, pady = '3')
            l2 = Label(master = transWindow, text = "{} Amount : {}".format(src, amt))
            l2.pack(fill = 'x', padx = 5, pady = '3')
            l3 = Label(master = transWindow, text = "Current Balance : {}".format(balance))
            l3.pack(fill = 'x', padx = 5, pady = '3')
            b3 = Button(master = transWindow, text = "OK", command = transWindow.destroy)
            b3.pack(fill = 'x', padx = 5, pady = '3')

            transWindow.mainloop()

        def emiGUI():
            emiWindow = Tk()
            emiWindow.title("EMI Calculator")
            emiWindow.geometry('350x285')

            emif1 = Frame(master = emiWindow)
            emif1.pack(fill = 'x', padx = 5, pady = 3)
            emif2 = Frame(master = emiWindow)
            emif2.pack(fill = 'x', padx = 5, pady = 3)
            emif3 = Frame(master = emiWindow)
            emif3.pack(fill = 'x', padx = 5, pady = 3)
            emif4 = Frame(master = emiWindow)
            emif4.pack(fill = 'x', padx = 5, pady = 3)
            emif5 = Frame(master = emiWindow)
            emif5.pack(fill = 'x', padx = 5, pady = 3)
            self.emiResult1 = Label(master = emiWindow, text = "Monthly Loan EMI : --", font = ('Comic Sans MS', 14, 'bold'))
            self.emiResult1.pack(fill = 'x', padx = 5, pady = 2)
            self.emiResult2 = Label(master = emiWindow, text = "Interest Amount : --", font = ('Comic Sans MS', 14, 'bold'))
            self.emiResult2.pack(fill = 'x', padx = 5, pady = 2)
            self.emiResult3 = Label(master = emiWindow, text = "Total Amount Payable : --", font = ('Comic Sans MS', 14, 'bold'))
            self.emiResult3.pack(fill = 'x', padx = 5, pady = 2)

            emiType = Label(master = emif1, text = "Loan Type           :")
            emiType.pack(side = 'left')
            emiAmt = Label(master = emif2, text = "Loan Amount       :")
            emiAmt.pack(side = 'left')
            emiRate = Label(master = emif3, text = "Interest Rate (pa) :")
            emiRate.pack(side = 'left')
            emiTime = Label(master = emif4, text = "Loan Tenure        :")
            emiTime.pack(side = 'left')
            self.emiLog = Label(master = emif5, text = "", fg = 'red', font = ('Calibri', 11, 'italic'))
            self.emiLog.pack(side = 'left')

            self.emiTypeEntryString = StringVar(emif1)
            self.emiTypeEntryString.set("Select")
            emiTypeEntry = OptionMenu(emif1, self.emiTypeEntryString, *["Home", "Car", "Personal"])
            emiTypeEntry.pack(side = 'right')
            self.emiAmtEntry = Entry(master = emif2)
            self.emiAmtEntry.pack(side = 'right')
            self.emiRateEntry = Entry(master = emif3)
            self.emiRateEntry.pack(side = 'right')
            self.emiTimeEntry = Entry(master = emif4, width = 9)
            self.emiTimeEntry.pack(side = 'right')
            self.emiTimeFormatString = StringVar(emif4)
            self.emiTimeFormatString.set("Months")
            emiTimeFormat = OptionMenu(emif4, self.emiTimeFormatString, *["Months", "Years"])
            emiTimeFormat.pack(side = 'right')
            emiSumbit = Button(master = emif5, text = "Calculate", command = lambda: emiCalc(self.emiTypeEntryString.get(), self.emiAmtEntry.get(), self.emiRateEntry.get(), self.emiTimeEntry.get(), self.emiTimeFormatString.get()))
            emiSumbit.pack(side = 'right')

            emiWindow.mainloop()

        def emiCalc(ltype, amt, rate, time, timef):

            def clearEmiGUI(log):
                widgets = [self.emiAmtEntry, self.emiRateEntry, self.emiTimeEntry]
                for i in widgets:
                    i.delete(0, 'end')
                self.emiTypeEntryString.set("Select")
                self.emiTimeFormatString.set("Months")
                self.emiLog['text'] = log

            data = [amt, rate, time]
            if "" in data or ltype == "Select":
                clearEmiGUI("Invalid Entries")
            else:
                try:
                    amt, rate, time = float(amt), float(rate), float(time)
                    if timef == "Years":
                        time *= 12
                    rate /= 1200
                    emi = ((1 + rate)**time) * rate * amt / (((1 + rate)**time) - 1)
                    total = emi * time
                    intAmt = total - amt
                    self.emiResult1['text'] = "Monthly {} Loan EMI : {}".format(ltype, int(emi))
                    self.emiResult2['text'] = "Interest Amount : {}".format(int(intAmt))
                    self.emiResult3['text'] = "Total Amount Payable : {}".format(int(total))
                except:
                    clearEmiGUI("Invalid Entries")

        from tkinter import Tk, Frame, Label, Entry, Button, OptionMenu, StringVar
        from tkcalendar import DateEntry
        from random import randint

        logGUI()

BMS()
