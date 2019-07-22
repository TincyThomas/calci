from tkinter import *
win = Tk()
win.title("My calculator")
win.resizable(0, 0)
operator = ""
fn = StringVar()


def btnclick(num):
    global operator
    operator = operator+str(num)
    fn.set(operator)


def btnequal():
    global operator
    result = str(eval(operator))
    fn.set(result)
    operator = ""

def btnclear():
    global operator
    operator = ""
    fn.set("")


text = Entry(win, font=("Arial", 19), insertwidth=3, bd=40, bg="dark khaki", fg="red", textvariable=fn)
text.grid(columnspan=4)

btn1 = Button(win, padx=16, pady=16, bd=8, fg="black", font=("Arial", 19), text='7', command=lambda: btnclick(7))
btn1.grid(row=1, column=0)
btn2 = Button(win, padx=16, pady=16, bd=8, fg="black", font=("Arial", 19), text='8', command=lambda: btnclick(8))
btn2.grid(row=1, column=1)
btn3 = Button(win, padx=16, pady=16, bd=8, fg="black", font=("Arial", 19), text='9', command=lambda: btnclick(9))
btn3.grid(row=1, column=2)
btnadd = Button(win, padx=16, pady=16, bd=8, fg="black", font=("Arial", 19), text='+', command=lambda: btnclick('+'))
btnadd.grid(row=1, column=3)

btn4 = Button(win, padx=16, pady=16, bd=8, fg="black", font=("Arial", 19), text='4', command=lambda: btnclick(4))
btn4.grid(row=2, column=0)
btn5 = Button(win, padx=16, pady=16, bd=8, fg="black", font=("Arial", 19), text='5', command=lambda: btnclick(5))
btn5.grid(row=2, column=1)
btn6 = Button(win, padx=16, pady=16, bd=8, fg="black", font=("Arial", 19), text='6', command=lambda: btnclick(6))
btn6.grid(row=2, column=2)
btnsub = Button(win, padx=16, pady=16, bd=8, fg="black", font=("Arial", 19), text='-', command=lambda: btnclick('-'))
btnsub.grid(row=2, column=3)

btn7 = Button(win, padx=16, pady=16, bd=8, fg="black", font=("Arial", 19), text='1', command=lambda: btnclick(1))
btn7.grid(row=3, column=0)
btn8 = Button(win, padx=16, pady=16, bd=8, fg="black", font=("Arial", 19), text='2', command=lambda: btnclick(2))
btn8.grid(row=3, column=1)
btn9 = Button(win, padx=16, pady=16, bd=8, fg="black", font=("Arial", 19), text='3', command=lambda: btnclick(3))
btn9.grid(row=3, column=2)
btnmul = Button(win, padx=16, pady=16, bd=8, fg="black", font=("Arial", 19), text='*', command=lambda: btnclick('*'))
btnmul.grid(row=3, column=3)

btn10 = Button(win, padx=16, pady=16, bd=8, fg="black", font=("Arial", 19), text='0', command=lambda: btnclick(0))
btn10.grid(row=4, column=0)
btnequal = Button(win, padx=16, pady=16, bd=8, fg="black", font=("Arial", 19), text='=', command=btnequal)
btnequal.grid(row=4, column=1)
btncan = Button(win, padx=16, pady=16, bd=8, fg="black", font=("Arial", 19), text='C', command=btnclear)
btncan.grid(row=4, column=2)
btndiv = Button(win, padx=16, pady=16, bd=8, fg="black", font=("Arial", 19), text='/', command=lambda: btnclick('/'))
btndiv.grid(row=4, column=3)

win.mainloop()
