class Calculator:

    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    sign = ['+', '-', '*', '/']
    
    def __init__(self, title = "Calculator", font = ('Comic Sans MS', 15, 'bold')):
        self.title = title
        self.font = font
        self.firstCalc = 'yes'
        self.expression = ['0']
        self.lastChr = 'num'

    def run(self):

        def negate():
            if display['text'] != '0':
                if display['text'][-1] not in self.sign:
                    if display['text'][-1] in self.nums:
                        req = self.expression[-1]
                        self.expression[-1] = '-' + req

                        string = display['text']
                        i = string.rfind(req)
                        string = string[:i] + '(-' + req + ')'
                        display['text'] = string
                    else:
                        self.expression[-1] = self.expression[-1][1:]

                        i = display['text'].rfind('(')
                        display['text'] = display['text'][:i] + display['text'][i+2:-1]

        def clear():
            display['text'] = '0'
            self.firstCalc = 'yes'
            self.lastChr = 'num'
            self.expression.clear()
            self.expression.append('0')

        def delete():
            if len(display['text']) == 1:
                clear()
            else:
                string = display['text']
                display['text'] = string[:-1]
                self.expression[-1] = self.expression[-1][:-1]
                if self.expression[-1] == '':
                    del self.expression[-1]

                if self.expression[-1][-1] in self.nums:
                    self.lastChr = 'num'
                else:
                    self.lastChr = 'sign'

        def equal():
            string = ''
            for i in self.expression:
                string += i
            result = str(eval(string))
            display['text'] = result
            self.expression.clear()
            self.expression.append(result)

            if display['text'] == '0':
                self.firstCalc = 'yes'

        def bind(button, key_func):
            # Visual Feedback
            from time import sleep
            button.config(relief = 'sunken')
            window.update_idletasks()
            sleep(0.1)
            button.config(relief = 'raised')
            
            process(button, key_func)

        def create(position, text, *args):
            # Button Creation
            button = Button(master = window, font = self.font, text = text)
            button.grid(row = position[0], column = position[1], sticky = 'nsew')            

            # Number Type Button
            if len(args) == 0:
                key = text
                key_func = key
            # Sign Type Button
            elif len(args) == 1:
                button.config(bg = 'gray')
                key = args[0]
                key_func = key
            # Function Type Button
            else:
                button.config(bg = 'orange')
                key = args[0]
                key_func = args[1]
                
            # Color of Equals Sign
            if len(args) == 3:
                button.config(bg = 'red')

            # Bindings
            window.bind(key, lambda event: bind(button, key_func))
            button.config(command = lambda: bind(button, key_func))

            return button

        def resizeButtons(rows, columns):
            for i in range(1, rows + 1):
                window.rowconfigure(i, weight = 1)
            for i in range(1, columns + 1):
                window.columnconfigure(i, weight = 1)

        def show(string, showType):
            if showType == 'change':
                display['text'] = display['text'][:-1]
            display['text'] += string

        def process(button, key_func):
            if button['bg'] == 'orange' or button['bg'] == 'red':
                key_func()
            else:
                if button['bg'] == 'gray':
                    currentChr = 'sign'
                else:
                    currentChr = 'num'

                if self.lastChr != currentChr:
                    self.expression.append(key_func)
                    show(button['text'], 'append')
                else:
                    if self.firstCalc == 'no' and self.lastChr == 'num':
                        self.expression[-1] += key_func
                        show(button['text'], 'append')
                    else:
                        self.expression[-1] = key_func
                        show(button['text'], 'change')

                self.lastChr = currentChr
                self.firstCalc = 'no'

        ## GUI Design
        from tkinter import Tk, Button, Label, Frame

        # Main Window
        window = Tk()
        window.title(self.title)
        window.geometry('330x415')

        # Widgets
        resizeButtons(7, 4)
        
        display = Label(master = window, font = self.font, text = "0")
        display.grid(row = 1, column = 1, columnspan = 4)
        b0 = create((7, 2), "0")
        b1 = create((6, 1), "1")
        b2 = create((6, 2), "2")
        b3 = create((6, 3), "3")
        b4 = create((5, 1), "4")
        b5 = create((5, 2), "5")
        b6 = create((5, 3), "6")
        b7 = create((4, 1), "7")
        b8 = create((4, 2), "8")
        b9 = create((4, 3), "9")
        bPoint = create((7, 3), ".")
        
        bAdd = create((3, 4), "+", "+")
        bSub = create((4, 4), "-", "-")
        bMul = create((5, 4), "x", "*")
        bDiv = create((6, 4), "{}".format(chr(247)), "/")

        bEqual = create((7, 4), "=", "<Return>", equal, "equals")
        bClear = create((3, 2), "C", "c", clear)
        bDelete = create((3, 3), '{}'.format(chr(9003)), '<BackSpace>', delete)
        bPlusMinus = create((7, 1), '{}'.format(chr(177)), 'n', negate)
        
        # Mainloops And Event Handlers
        window.mainloop()

calc1 = Calculator("Calculator")
calc1.run()
