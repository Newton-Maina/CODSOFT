from tkinter import *
from tkinter import messagebox
from math import log, pi, e, sin, tan, cos, log

from django.db.models.expressions import result
from libpasteurize.fixes.fix_future_builtins import expression
from virtualenv.discovery.cached_py_info import clear

calc_window = Tk()
calc_window.title('Calculator')
calc_window.geometry('350x720')
calc_window.resizable(0, 0)
calc_window.iconbitmap('images/icon.ico')


def about():
    license_text = 'MIT License'
    messagebox.showinfo('About',f"\n\nMade by Newton Maina \n\n{license_text}")

def buttonClick(item):
    global expression
    inputText.set(inputText.get()+(str(item)))

def buttonClear():
    global expression
    expression=""
    inputText.set(inputText.get()[0:-1])

def allClear():
    inputText.set("")

def exponent():
    inputText.set(inputText.get() + '^')

def equalButton():
    results = ""
    try:
        expression = inputText.get()
        if '^' in expression:
            base, exp = expression.split('^')
            result = float(base) ** float(exp)
        else:
            result = eval(expression)
        inputText.set(result)
    except:
        inputText.set("Error...")

menubar = Menu(calc_window, bg="black", fg="white")
filemenu = Menu(menubar, tearoff=0,  bg="black", fg="white")
filemenu.add_command(label="Copy")
filemenu.add_command(label="Paste")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=calc_window.quit)
menubar.add_cascade(label="Edit", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0, bg="black", fg="white")
helpmenu.add_command(label="About" , command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

expression=""
inputText=StringVar()

inputFrame = Frame(calc_window, width=310, height=50, bd=0, highlightbackground="black", highlightthickness=2, highlightcolor="gray")
inputFrame.pack(side=TOP)

inputField = Entry(inputFrame, textvariable=inputText, font=('arial', 24), width=50, fg="white", bg="black", bd=0, justify=RIGHT)
inputField.grid(row=0, column=0)
inputField.pack(ipady=43)

mainFrame = Frame(calc_window, width=310, height=273, bg="black")
mainFrame.pack()

ac = PhotoImage(file='images/ac.png')
acImage = ac.subsample(4,4)
Button(mainFrame, image=acImage, text="AC", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: allClear()).grid(row=0, column=0, padx=1, pady=1)

clear = PhotoImage(file='images/clear.png')
clearImage = clear.subsample(4,4)
Button(mainFrame, image=clearImage, text="Clear", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClear()).grid(row=0, column=1, padx=1, pady=1)

expan_btn = PhotoImage(file='images/exponent_btn.png')
expan_btnImage = expan_btn.subsample(4,4)
Button(mainFrame, image=expan_btnImage, text="Exp", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: exponent()).grid(row=0, column=2, padx=1, pady=1)

divide_btn = PhotoImage(file='images/divide.png')
divideImage = divide_btn.subsample(4,4)
Button(mainFrame, image=divideImage, text="/", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick("/")).grid(row=0, column=3, padx=1, pady=1)

seven_btn = PhotoImage(file='images/seven.png')
sevenImage = seven_btn.subsample(4,4)
Button(mainFrame, image=sevenImage, text="7", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick(7)).grid(row=1, column=0, padx=1, pady=1)

eight_btn = PhotoImage(file='images/eight.png')
eightImage = eight_btn.subsample(4,4)
Button(mainFrame, image=eightImage, text="8", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick(8)).grid(row=1, column=1, padx=1, pady=1)

nine_btn = PhotoImage(file='images/nine.png')
nineImage = nine_btn.subsample(4,4)
Button(mainFrame, image=nineImage, text="9", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick(9)).grid(row=1, column=2, padx=1, pady=1)

multi_btn = PhotoImage(file='images/multi.png')
multiImage = multi_btn.subsample(4,4)
Button(mainFrame, image=multiImage, text="*", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick("*")).grid(row=1, column=3, padx=1, pady=1)

four_btn = PhotoImage(file='images/four.png')
fourImage = four_btn.subsample(4,4)
Button(mainFrame, image=fourImage, text="4", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick(4)).grid(row=2, column=0, padx=1, pady=1)

five_btn = PhotoImage(file='images/five.png')
fiveImage = five_btn.subsample(4,4)
Button(mainFrame, image=fiveImage, text="5", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick(5)).grid(row=2, column=1, padx=1, pady=1)

six_btn = PhotoImage(file='images/six.png')
sixImage = six_btn.subsample(4,4)
Button(mainFrame, image=sixImage, text="6", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick(6)).grid(row=2, column=2, padx=1, pady=1)

minus_btn = PhotoImage(file='images/minus.png')
minusImage = minus_btn.subsample(4,4)
Button(mainFrame, image=minusImage, text="-", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick("-")).grid(row=2, column=3, padx=1, pady=1)

one_btn = PhotoImage(file='images/one.png')
oneImage = one_btn.subsample(4,4)
Button(mainFrame, image=oneImage, text="1", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick(1)).grid(row=3, column=0, padx=1, pady=1)

two_btn = PhotoImage(file='images/two.png')
twoImage = two_btn.subsample(4,4)
Button(mainFrame, image=twoImage, text="2", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick(2)).grid(row=3, column=1, padx=1, pady=1)

three_btn = PhotoImage(file='images/three.png')
threeImage = three_btn.subsample(4,4)
Button(mainFrame, image=threeImage, text="3", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick(3)).grid(row=3, column=2, padx=1, pady=1)

add_btn = PhotoImage(file='images/plus.png')
addImage = add_btn.subsample(4,4)
Button(mainFrame, image=addImage, text="+", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick("+")).grid(row=3, column=3, padx=1, pady=1)

zero_btn = PhotoImage(file='images/0.png')
zeroImage = zero_btn.subsample(4,4)
Button(mainFrame, image=zeroImage, text="0", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

point = PhotoImage(file='images/point.png')
pointImage = point.subsample(4,4)
Button(mainFrame, image=pointImage, text=".", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick(".")).grid(row=4, column=2, padx=1, pady=1)

equal_btn = PhotoImage(file='images/equal.png')
equalImage = equal_btn.subsample(4,4)
Button(mainFrame, image=equalImage, text="=", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: equalButton()).grid(row=4, column=3, padx=1, pady=1)

bracket1 = PhotoImage(file='images/bracket1.png')
bracket1Image = bracket1.subsample(4,4)
Button(mainFrame, image=bracket1Image, text="(", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick("(")).grid(row=5, column=0, padx=1, pady=1)

bracket2 = PhotoImage(file='images/bracket2.png')
bracket2Image = bracket2.subsample(4,4)
Button(mainFrame, image=bracket2Image, text="(", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick(")")).grid(row=5, column=1, padx=1, pady=1)

pie = 3.1415
pi = PhotoImage(file='images/pi.png')
piImage = pi.subsample(4,4)
Button(mainFrame, image=piImage, text="pi", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick(pie)).grid(row=5, column=2, padx=1, pady=1)

eie = 2.7182
ee = PhotoImage(file='images/eie.png')
eeImage = ee.subsample(4,4)
Button(mainFrame, image=eeImage, text="e", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick(eie)).grid(row=5, column=3, padx=1, pady=1)

sin_btn = PhotoImage(file='images/sin_btn.png')
sinImage = sin_btn.subsample(4,4)
Button(mainFrame, image=sinImage, text="sin", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick("sin(")).grid(row=6, column=0, padx=1, pady=1)

cos_btn = PhotoImage(file='images/cos_btn.png')
cosImage = cos_btn.subsample(4,4)
Button(mainFrame, image=cosImage, text="cos", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick("cos(")).grid(row=6, column=1, padx=1, pady=1)

tan_btn = PhotoImage(file='images/tan_btn.png')
tanImage = tan_btn.subsample(4,4)
Button(mainFrame, image=tanImage, text="tan", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick("tan(")).grid(row=6, column=2, padx=1, pady=1)

log_btn = PhotoImage(file='images/log_btn.png')
logImage = log_btn.subsample(4,4)
Button(mainFrame, image=logImage, text="log", fg="black",
       bd=0, bg="black", cursor="hand2",
       command=lambda: buttonClick("log(")).grid(row=6, column=3, padx=1, pady=1)

calc_window.config(bg="black", menu=menubar)
calc_window.mainloop()