from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

root=Tk()

root.title("Our project")
root.config(bg="aqua")
root.attributes('-fullscreen', True)

def minimize_window():
  root.iconify()

def maximize_window():
  root.attributes('-fullscreen', not root.attributes('-fullscreen'))

def close_window():
  root.destroy()

minimize_button = Button(root, text='-', command=minimize_window)
minimize_button.place(x=root.winfo_screenwidth() - 70, y=5)

maximize_button = Button(root, text='❐', command=maximize_window)
maximize_button.place(x=root.winfo_screenwidth() - 50, y=5)

close_button = Button(root, text='X', command=close_window)
close_button.place(x=root.winfo_screenwidth() - 30, y=5)

heading=Label(root, text="WELCOME TO OUR ADVANCED CALCULATOR ", font="vani 27 bold", bg="gray15", fg="gold", relief=GROOVE, justify=CENTER)
heading.pack()

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
    
def bt_clearone(): 
    global expression 
    global a
    a=input_text.get()
    expression = "" 
    for i in range(0,len(a)-1):
        expression=expression+a[i]
    input_text.set(expression)
 
def bt_equal():
    global expression
    result = str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    input_text.set(result)
    expression = ""
 
expression = ""
# 'StringVar()' :It is used to get the instance of input field
input_text = StringVar()
# Let us creating a frame for the input field
input_frame = Frame(root, width=55, height=50, bd=2, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.place(x=220, y=150)
#Let us create a input field inside the 'Frame'
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=24, bg="#eee", bd=10, justify=RIGHT, state=DISABLED)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field 
#Let us creating another 'Frame' for the button below the 'input_frame'
btns_frame = Frame(root, width=60, height=272.5, highlightbackground="black", highlightthickness=2)
btns_frame.place(x=220, y=230)
# first row
clear = Button(btns_frame, text = "AC", fg = "white", width = 22, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 2, padx = 1, pady = 1)
clear = Button(btns_frame, text = "C", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: bt_clearone()).grid(row = 0, column = 2, padx = 1, pady = 1)
divide = Button(btns_frame, text = "/", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
# second row
 
seven = Button(btns_frame, text = "7", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

# third row
 
four = Button(btns_frame, text = "4", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1) 
five = Button(btns_frame, text = "5", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

# fourth row
 
one = Button(btns_frame, text = "1", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fourth row
 
zero = Button(btns_frame, text = "0", fg = "white", width = 22, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(btns_frame, text = ".", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(btns_frame, text = "=", fg = "white", width = 10, height = 3, bd = 2, bg = "black", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)


commandheading=Label(root, text="FOLLOW THIS COMMAND ", font="vani 19 bold", bg="gray15", fg="white", relief=GROOVE)
commandheading.place(x=1000, y=60)

a=scrolledtext.ScrolledText(root, wrap=WORD, font="Arial 15 bold", width=40, height=10,bg="skyblue")
a.place(x=950, y=160)

a.insert('insert', "~ Press 1 - Binary Calculator\n")
a.insert('insert', "~ Press 2 - BMI Calculator\n")
a.config(state=DISABLED)

# Variable
a1=IntVar()

def enter1():
    if a1.get()==1:
# ------------------------------------------------------------------------------------------------------------------------------------------------------
        # Binary Calculator
        
        bc=Toplevel()
        bc.title("Binary calculator")
        bc.geometry("1620x950")
        bc.config(bg="aqua")
        bc.attributes('-fullscreen', True)

        def minimize_window():
            bc.iconify()

        def maximize_window():
            bc.attributes('-fullscreen', not bc.attributes('-fullscreen'))

        def close_window():
            bc.destroy()
        
        minimize_button = Button(bc, text='-', command=minimize_window)
        minimize_button.place(x=bc.winfo_screenwidth() - 70, y=5)

        maximize_button = Button(bc, text='❐', command=maximize_window)
        maximize_button.place(x=bc.winfo_screenwidth() - 50, y=5)

        close_button = Button(bc, text='X', command=close_window)
        close_button.place(x=bc.winfo_screenwidth() - 30, y=5)


        heading=Label(bc, text="WELCOME TO OUR BINARY CALCULATOR ", font="vani 27 bold", bg="gray15", fg="gold", relief=GROOVE, justify=CENTER)
        heading.pack()

        commandheading=Label(bc, text="FOLLOW THIS COMMAND ", font="vani 19 bold", bg="gray15", fg="white", relief=GROOVE)
        commandheading.place(x=1000, y=60)

        b=scrolledtext.ScrolledText(bc, wrap=WORD, font="Arial 15 bold", width=40, height=10,bg="skyblue")
        b.place(x=100, y=140)

        b.insert('insert', "~ Press 1 - Decimal Conversion\n")
        b.insert('insert', "~ Press 2 - Binary Conversion\n")
        b.insert('insert', "~ Press 3 - Octal Conversion\n")
        b.insert('insert', "~ Press 4 - Hexadecimal Conversion\n")
        b.insert('insert', "~ Press 5 - Binary Operation(add, sub, mul)\n")
        b.insert('insert', "~ Press 6 - Binary Operation Divide\n")
        b.insert('insert', "~ Press 7 - 1's & 2's Complement\n")
        b.config(state=DISABLED)
        
        # Variable
        a2=IntVar()

        a22=Label(bc, text="ENTER THE COMMAND ", font="vani 19 bold", bg="gray15", fg="white")
        a22.place(x=860, y=300)
        a22entry=Entry(bc, font="vani 20 bold", bg="white", fg="black", relief=GROOVE, justify=CENTER, textvariable=a2)
        a22entry.place(x=1160, y=300)

        def enter2():
            if a2.get()==1:
# ------------------------------------------------------------------------------------------------------------------------------------------------------
                bx=Toplevel()
                #  Decimal Conversion
                bx.title("Decimal conversion")
                bx.geometry("1620x950")
                bx.config(bg="aqua")
                bx.attributes('-fullscreen', True)

                def minimize_window():
                    bx.iconify()

                def maximize_window():
                    bx.attributes('-fullscreen', not bx.attributes('-fullscreen'))

                def close_window():
                    bx.destroy()
                
                minimize_button = Button(bx, text='-', command=minimize_window)
                minimize_button.place(x=bx.winfo_screenwidth() - 70, y=5)

                maximize_button = Button(bx, text='❐', command=maximize_window)
                maximize_button.place(x=bx.winfo_screenwidth() - 50, y=5)

                close_button = Button(bx, text='X', command=close_window)
                close_button.place(x=bx.winfo_screenwidth() - 30, y=5)

                # variable
                num1=IntVar()
                biiin=StringVar()
                octaaa=StringVar()
                hexaaa=StringVar()
                
                def convert():
                    a=num1.get()
                    b=str(bin(a))
                    o=str(oct(a))
                    h=str(hex(a))
                    biiin.set(b)
                    octaaa.set(o)
                    hexaaa.set(h)
                
                decimalheading=Label(bx, text="DECIMAL CONVERSION ", font="vani 30 bold", bg="grey", fg="black", relief=GROOVE, justify=CENTER)
                decimalheading.place(x=480, y=20)
                number=Label(bx, text="Enter number = ", fg="black", background="aqua", font="times 25 bold")
                number.place(x=380, y=200)
                n=Label(bx, text="Enter number = ", fg="black", background="aqua", font="times 25 bold")
                n.place(x=380, y=200)
                n=Label(bx, text="Binary = ", fg="black", background="aqua", font="times 25 bold")
                n.place(x=380, y=300)
                n=Label(bx, text="Octal = ", fg="black", background="aqua", font="times 25 bold")
                n.place(x=380, y=400)
                n=Label(bx, text="Hexadecimal = ", fg="black", background="aqua", font="times 25 bold")
                n.place(x=380, y=500)
                n=Entry(bx, font="arial 25 bold", fg="black", relief=GROOVE, justify=CENTER, textvariable=num1)
                n.place(x=670, y=200)
                n=Entry(bx, font="arial 25 bold", fg="black", relief=GROOVE, justify=CENTER, state=DISABLED, textvariable=biiin)
                n.place(x=670, y=300)
                n=Entry(bx, font="arial 25 bold", fg="black", relief=GROOVE, justify=CENTER, state=DISABLED, textvariable=octaaa)
                n.place(x=670, y=400)
                n=Entry(bx, font="arial 25 bold", fg="black", relief=GROOVE, justify=CENTER, state=DISABLED, textvariable=hexaaa)
                n.place(x=670, y=500)
                
                def clear3():
                    num1.set(0)
                    biiin.set("")
                    octaaa.set("")
                    hexaaa.set("")
        
                def exit3():
                    if messagebox.askyesno('Exit', "Do you really want to Exit"):
                        bx.destroy()
                        bc.deiconify()
                    else:
                        bx.deiconify()
                
                Button(bx, text="Clear", font="times 20 bold", fg="black", bg="white", command=clear3).place(x=450, y=600)
                Button(bx, text="Convert", font="times 20 bold", fg="black", bg="white", command=convert).place(x=650, y=600)
                Button(bx, text="Exit", font="times 20 bold", fg="black", bg="white", command=exit3).place(x=850, y=600)
                
                bx.mainloop()
            
            # Binary conversion   
            if a2.get()==2:
# ------------------------------------------------------------------------------------------------------------------------------------------------------
                dc=Toplevel()
                #  Decimal Conversion
                dc=Toplevel()
                dc.title("Decimal conversion")
                dc.geometry("1620x950")
                dc.config(bg="aqua")
                dc.attributes('-fullscreen', True)

                def minimize_window():
                    dc.iconify()

                def maximize_window():
                    dc.attributes('-fullscreen', not bx.attributes('-fullscreen'))

                def close_window():
                    dc.destroy()
                
                minimize_button = Button(dc, text='-', command=minimize_window)
                minimize_button.place(x=dc.winfo_screenwidth() - 70, y=5)

                maximize_button = Button(dc, text='❐', command=maximize_window)
                maximize_button.place(x=dc.winfo_screenwidth() - 50, y=5)

                close_button = Button(dc, text='X', command=close_window)
                close_button.place(x=dc.winfo_screenwidth() - 30, y=5)

                # variable
               
                biin=StringVar()
                deci=StringVar()
                octaa=StringVar()
                hexaa=StringVar()
                
                def convert1():
                    a=biin.get()
                    # bin to deci
                    a3=int(a, 2)
                    deci.set(a3)
                    # bin to oct
                    o=oct(int(a, 2))
                    octaa.set(o)
                    # bin to hex
                    h=hex(int(a, 2))
                    hexaa.set(h)
                
                decimalheading=Label(dc, text="BINARY CONVERSION ", font="vani 30 bold", bg="white", fg="black", relief=GROOVE, justify=CENTER)
                decimalheading.place(x=480, y=20)
                x=Label(dc, text="Enter binary number = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=350, y=200)
                x=Label(dc, text="Decimal = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=350, y=300)
                x=Label(dc, text="Octal = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=350, y=400)
                x=Label(dc, text="Hexadecimal = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=350, y=500)
                x=Entry(dc, font="arial 25 bold", fg="black", relief=GROOVE, justify=CENTER, textvariable=biin)
                x.place(x=700, y=200)
                x=Entry(dc, font="arial 25 bold", fg="black", state=DISABLED, relief=GROOVE, justify=CENTER, textvariable=deci)
                x.place(x=700, y=300)
                x=Entry(dc, font="arial 25 bold", fg="black", state=DISABLED, relief=GROOVE, justify=CENTER, textvariable=octaa)
                x.place(x=700, y=400)
                x=Entry(dc, font="arial 25 bold", fg="black", state=DISABLED, relief=GROOVE, justify=CENTER, textvariable=hexaa)
                x.place(x=700, y=500)
                
                def clear4():
                    biin.set(0)
                    deci.set("")
                    octaa.set("")
                    hexaa.set("")
        
                def exit4():
                    if messagebox.askyesno('Exit', "Do you really want to Exit"):
                        dc.destroy()
                        bc.deiconify()
                    else:
                        dc.deiconify()
                
                Button(dc, text="Clear", font="times 20 bold", fg="black", bg="white", command=clear4).place(x=450, y=600)
                Button(dc, text="Convert", font="times 20 bold", fg="black", bg="white", command=convert1).place(x=650, y=600)
                Button(dc, text="Exit", font="times 20 bold", fg="black", bg="white", command=exit4).place(x=850, y=600)
                
                dc.mainloop()
            
            
            if a2.get()==3:
# ------------------------------------------------------------------------------------------------------------------------------------------------------
                oc=Toplevel()
                #  Octal Conversion
                oc=Toplevel()
                oc.title("Octal conversion")
                oc.geometry("1620x950")
                oc.config(bg="aqua")
                oc.attributes('-fullscreen', True)

                def minimize_window():
                    oc.iconify()

                def maximize_window():
                    oc.attributes('-fullscreen', not oc.attributes('-fullscreen'))

                def close_window():
                    oc.destroy()
                
                minimize_button = Button(oc, text='-', command=minimize_window)
                minimize_button.place(x=oc.winfo_screenwidth() - 70, y=5)

                maximize_button = Button(oc, text='❐', command=maximize_window)
                maximize_button.place(x=oc.winfo_screenwidth() - 50, y=5)

                close_button = Button(oc, text='X', command=close_window)
                close_button.place(x=oc.winfo_screenwidth() - 30, y=5)
    
                # variable
               
                octaa=StringVar()
                biin=StringVar()
                deci=StringVar()
                hexaa=StringVar()
                
                def convert2():
                    a=octaa.get()
                    # oct to deci
                    a3=int(a, 8)
                    deci.set(a3)
                    # oct to bin
                    b=bin(int(a, 8))
                    biin.set(b)
                    # oct to hex
                    h=hex(int(a, 8))
                    hexaa.set(h)
                
                decimalheading=Label(oc, text="OCTAL CONVERSION ", font="vani 30 bold", bg="white", fg="black", relief=GROOVE, justify=CENTER)
                decimalheading.place(x=480, y=20)
                x=Label(oc, text="Enter octal number = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=350, y=200)
                x=Label(oc, text="Decimal = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=350, y=300)
                x=Label(oc, text="Binary = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=350, y=400)
                x=Label(oc, text="Hexadecimal = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=350, y=500)
                x=Entry(oc, font="arial 25 bold", fg="black", relief=GROOVE, justify=CENTER, textvariable=octaa)
                x.place(x=700, y=200)
                x=Entry(oc, font="arial 25 bold", fg="black", state=DISABLED, relief=GROOVE, justify=CENTER, textvariable=deci)
                x.place(x=700, y=300)
                x=Entry(oc, font="arial 25 bold", fg="black", state=DISABLED, relief=GROOVE, justify=CENTER, textvariable=biin)
                x.place(x=700, y=400)
                x=Entry(oc, font="arial 25 bold", fg="black", state=DISABLED, relief=GROOVE, justify=CENTER, textvariable=hexaa)
                x.place(x=700, y=500)
                
                def clear5():
                    octaa.set(0)
                    deci.set("")
                    biin.set("")
                    hexaa.set("")
        
                def exit5():
                    if messagebox.askyesno('Exit', "Do you really want to Exit"):
                        oc.destroy()
                        bc.deiconify()
                    else:
                        oc.deiconify()
                
                Button(oc, text="Clear", font="times 20 bold", fg="black", bg="white", command=clear5).place(x=450, y=600)
                Button(oc, text="Convert", font="times 20 bold", fg="black", bg="white", command=convert2).place(x=650, y=600)
                Button(oc, text="Exit", font="times 20 bold", fg="black", bg="white", command=exit5).place(x=850, y=600)
                
                oc.mainloop()
             
            if a2.get()==4:
# ------------------------------------------------------------------------------------------------------------------------------------------------------
                hc=Toplevel()
                #  Hexadecimal Conversion
                hc=Toplevel()
                hc.title("Hexadecimal conversion")
                hc.geometry("1620x950")
                hc.config(bg="aqua")
                hc.attributes('-fullscreen', True)

                def minimize_window():
                    hc.iconify()

                def maximize_window():
                    hc.attributes('-fullscreen', not hc.attributes('-fullscreen'))

                def close_window():
                    hc.destroy()
                
                minimize_button = Button(hc, text='-', command=minimize_window)
                minimize_button.place(x=hc.winfo_screenwidth() - 70, y=5)

                maximize_button = Button(hc, text='❐', command=maximize_window)
                maximize_button.place(x=hc.winfo_screenwidth() - 50, y=5)

                close_button = Button(hc, text='X', command=close_window)
                close_button.place(x=hc.winfo_screenwidth() - 30, y=5)

                # variable
               
                hexaaaa=StringVar()
                decii=StringVar()
                biiiin=StringVar()
                octaaaa=StringVar()
                
                def convert3():
                    a=hexaaaa.get()
                    # hex to deci
                    a3=int(a, 16)
                    decii.set(a3)
                    # hex to bin
                    b=bin(int(a, 16))
                    biiiin.set(b)
                    # hex to oct
                    o=oct(int(a, 16))
                    octaaaa.set(o)
                
                decimalheading=Label(hc, text="HEXADECIMAL CONVERSION ", font="vani 30 bold", bg="white", fg="black", relief=GROOVE, justify=CENTER)
                decimalheading.place(x=480, y=20)
                x=Label(hc, text="Enter hexadecimal number = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=280, y=200)
                x=Label(hc, text="Decimal = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=280, y=300)
                x=Label(hc, text="Binary = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=280, y=400)
                x=Label(hc, text="Octal = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=280, y=500)
                x=Entry(hc, font="arial 25 bold", fg="black", relief=GROOVE, justify=CENTER, textvariable=hexaaaa)
                x.place(x=700, y=200)
                x=Entry(hc, font="arial 25 bold", fg="black", state=DISABLED, relief=GROOVE, justify=CENTER, textvariable=decii)
                x.place(x=700, y=300)
                x=Entry(hc, font="arial 25 bold", fg="black", state=DISABLED, relief=GROOVE, justify=CENTER, textvariable=biiiin)
                x.place(x=700, y=400)
                x=Entry(hc, font="arial 25 bold", fg="black", state=DISABLED, relief=GROOVE, justify=CENTER, textvariable=octaaaa)
                x.place(x=700, y=500)
                
                def clear6():
                    hexaaaa.set(0)
                    decii.set("")
                    biiiin.set("")
                    octaaaa.set("")
        
                def exit6():
                    if messagebox.askyesno('Exit', "Do you really want to Exit"):
                        hc.destroy()
                        bc.deiconify()
                    else:
                        hc.deiconify()
                
                Button(hc, text="Clear", font="times 20 bold", fg="black", bg="white", command=clear6).place(x=420, y=600)
                Button(hc, text="Convert", font="times 20 bold", fg="black", bg="white", command=convert3).place(x=620, y=600)
                Button(hc, text="Exit", font="times 20 bold", fg="black", bg="white", command=exit6).place(x=820, y=600)
                
                hc.mainloop()   
                
            if a2.get()==5:
# ------------------------------------------------------------------------------------------------------------------------------------------------------
                bo=Toplevel()
                bo.title("add, sub, mul operation")
                bo.geometry("1620x950")
                bo.config(bg="aqua")
                bo.attributes('-fullscreen', True)

                def minimize_window():
                    bo.iconify()

                def maximize_window():
                    bo.attributes('-fullscreen', not bo.attributes('-fullscreen'))

                def close_window():
                    bo.destroy()
                
                minimize_button = Button(bo, text='-', command=minimize_window)
                minimize_button.place(x=bo.winfo_screenwidth() - 70, y=5)

                maximize_button = Button(bo, text='❐', command=maximize_window)
                maximize_button.place(x=bo.winfo_screenwidth() - 50, y=5)

                close_button = Button(bo, text='X', command=close_window)
                close_button.place(x=bo.winfo_screenwidth() - 30, y=5)

                num1=IntVar()
                num2=IntVar()
                num3=StringVar()
                num4=StringVar()
                result=StringVar()
                result1=StringVar()
                
                def sum1():
                    a=str(num1.get())
                    b=int(a, 2)
                    num3.set(b)
                    c=str(num2.get())
                    d=int(c, 2)
                    num4.set(d)
                    sum=int(a, 2)+int(c, 2)
                    result1.set(sum)
                    sum1=str(bin(sum))
                    result.set(sum1)
                    
                def sub1():
                    a=str(num1.get())
                    b=int(a, 2)
                    num3.set(b)
                    c=str(num2.get())
                    d=int(c, 2)
                    num4.set(d)
                    sub=int(a, 2)-int(c, 2)
                    result1.set(sub)
                    subb1=str(bin(sub))
                    result.set(subb1)
                    
                def mul1():
                    a=str(num1.get())
                    b=int(a, 2)
                    num3.set(b)
                    c=str(num2.get())
                    d=int(c, 2)
                    num4.set(d)
                    mul=int(a, 2)*int(c, 2)
                    result1.set(mul)
                    mul1=str(bin(mul))
                    result.set(mul1)   
                    
                def clear11():
                    num1.set(0)
                    num2.set(0)
                    num3.set("")
                    num4.set("")
                    result.set("")
                    result1.set("")
                        
                def exit11():
                    if messagebox.askyesno('Exit', "Do you really want to Exit"):
                        bo.destroy()
                        bc.deiconify()
                    else:
                        bo.deiconify() 
                        
                opr=Label(bo, text="Binary Operation ", font="vani 30 bold", bg="white", fg="black", relief=GROOVE, justify=CENTER)
                opr.place(x=570, y=20)
                opr=Label(bo, text="Binary ", font="vani 30 bold", bg="white", fg="black", relief=GROOVE, justify=CENTER)
                opr.place(x=700, y=100)
                opr=Label(bo, text="Decimal ", font="vani 30 bold", bg="white", fg="black", relief=GROOVE, justify=CENTER)
                opr.place(x=1100, y=100)
                x=Label(bo, text="Enter 1st binary number = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=180, y=200)
                x=Label(bo, text="Enter 2nd binary number = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=180, y=300)
                x=Label(bo, text="Result = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=180, y=400)
                x=Entry(bo, font="arial 25 bold", fg="black", relief=GROOVE, justify=CENTER, textvariable=num1)
                x.place(x=600, y=200)
                x=Entry(bo, font="arial 25 bold", fg="black", state=DISABLED, relief=GROOVE, justify=CENTER, textvariable=num3)
                x.place(x=1000, y=200)
                x=Entry(bo, font="arial 25 bold", fg="black", relief=GROOVE, justify=CENTER, textvariable=num2)
                x.place(x=600, y=300)
                x=Entry(bo, font="arial 25 bold", fg="black", state=DISABLED, relief=GROOVE, justify=CENTER, textvariable=num4)
                x.place(x=1000, y=300)
                x=Entry(bo, font="arial 25 bold", fg="black", state=DISABLED, relief=GROOVE, justify=CENTER, textvariable=result)
                x.place(x=600, y=400)
                x=Entry(bo, font="arial 25 bold", fg="black", state=DISABLED, relief=GROOVE, justify=CENTER, textvariable=result1)
                x.place(x=1000, y=400)
                Button(bo, text="Sum", font="times 20 bold", fg="black", bg="white", command=sum1).place(x=300, y=600)
                Button(bo, text="Subtraction", font="times 20 bold", fg="black", bg="white", command=sub1).place(x=600, y=600)
                Button(bo, text="Multiplication", font="times 20 bold", fg="black", bg="white", command=mul1).place(x=1000, y=600)
                Button(bo, text="clear", font="times 20 bold", fg="black", bg="white", command=clear11).place(x=450, y=700)
                Button(bo, text="Exit", font="times 20 bold", fg="black", bg="white", command=exit11).place(x=830, y=700)
                bo.mainloop()
                
            if a2.get()==6:
# ------------------------------------------------------------------------------------------------------------------------------------------------------
                do=Toplevel()
                do.title("devide operation")
                do.geometry("1620x950")
                do.config(bg="aqua")
                do.attributes('-fullscreen', True)

                def minimize_window():
                    do.iconify()

                def maximize_window():
                    do.attributes('-fullscreen', not do.attributes('-fullscreen'))

                def close_window():
                    do.destroy()
                
                minimize_button = Button(do, text='-', command=minimize_window)
                minimize_button.place(x=do.winfo_screenwidth() - 70, y=5)

                maximize_button = Button(do, text='❐', command=maximize_window)
                maximize_button.place(x=do.winfo_screenwidth() - 50, y=5)

                close_button = Button(do, text='X', command=close_window)
                close_button.place(x=do.winfo_screenwidth() - 30, y=5)

                num1=IntVar()
                num2=IntVar()
                num3=StringVar()
                num4=StringVar()
                quo=StringVar()
                quo1=StringVar()
                rema=StringVar()
                rema1=StringVar()
                
                def devide1():
                    a=str(num1.get())
                    b=int(a, 2)
                    num3.set(b)
                    c=str(num2.get())
                    d=int(c, 2)
                    num4.set(d)
                    dev=int(int(a, 2)/int(c, 2))
                    quo1.set(dev)
                    r=str(bin(dev))
                    quo.set(r)
                    mod=int(int(a, 2)%int(c, 2))
                    rema1.set(mod)
                    r1=str(bin(mod))
                    rema.set(r1)
                    
                def clear111():
                    num1.set(0)
                    num2.set(0)
                    num3.set("")
                    num4.set("")
                    quo.set("")
                    quo1.set("")
                    rema.set("")
                    rema1.set("")
                        
                def exit111():
                    if messagebox.askyesno('Exit', "Do you really want to Exit"):
                        do.destroy()
                        bc.deiconify()
                    else:
                        do.deiconify() 
                        
                opr=Label(do, text="Binary Division Operation ", font="vani 30 bold", bg="white", fg="black", relief=GROOVE, justify=CENTER)
                opr.place(x=480, y=20)
                opr=Label(do, text="Binary ", font="vani 30 bold", bg="white", fg="black", relief=GROOVE, justify=CENTER)
                opr.place(x=700, y=100)
                opr=Label(do, text="Decimal ", font="vani 30 bold", bg="white", fg="black", relief=GROOVE, justify=CENTER)
                opr.place(x=1100, y=100)
                x=Label(do, text="Enter 1st binary number = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=180, y=200)
                x=Label(do, text="Enter 2nd binary number = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=180, y=300)
                x=Label(do, text="Quotient = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=180, y=400)
                x=Label(do, text="Remainder = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=180, y=500)
                x=Entry(do, font="arial 25 bold", fg="black", relief=GROOVE, justify=CENTER, textvariable=num1)
                x.place(x=600, y=200)
                x=Entry(do, font="arial 25 bold", fg="black", state=DISABLED, relief=GROOVE, justify=CENTER, textvariable=num3)
                x.place(x=1000, y=200)
                x=Entry(do, font="arial 25 bold", fg="black", relief=GROOVE, justify=CENTER, textvariable=num2)
                x.place(x=600, y=300)
                x=Entry(do, font="arial 25 bold", fg="black", state=DISABLED, relief=GROOVE, justify=CENTER, textvariable=num4)
                x.place(x=1000, y=300)
                x=Entry(do, font="arial 25 bold", fg="black", state=DISABLED, relief=GROOVE, justify=CENTER, textvariable=quo)
                x.place(x=600, y=400)
                x=Entry(do, font="arial 25 bold", fg="black", state=DISABLED, relief=GROOVE, justify=CENTER, textvariable=quo1)
                x.place(x=1000, y=400)
                x=Entry(do, font="arial 25 bold", fg="black", state=DISABLED, relief=GROOVE, justify=CENTER, textvariable=rema)
                x.place(x=600, y=500)
                x=Entry(do, font="arial 25 bold", fg="black", state=DISABLED, relief=GROOVE, justify=CENTER, textvariable=rema1)
                x.place(x=1000, y=500)
                Button(do, text="clear", font="times 20 bold", fg="black", bg="white", command=clear111).place(x=340, y=600)
                Button(do, text="Devide", font="times 20 bold", fg="black", bg="white", command=devide1).place(x=640, y=600)
                Button(do, text="Exit", font="times 20 bold", fg="black", bg="white", command=exit111).place(x=940, y=600)
                do.mainloop()
                
            if a2.get()==7:
# ------------------------------------------------------------------------------------------------------------------------------------------------------
                co=Toplevel()
                co.title("1's & 2's complement")
                co.geometry("1620x950")
                co.config(bg="aqua")
                co.attributes('-fullscreen', True)

                def minimize_window():
                    co.iconify()

                def maximize_window():
                    co.attributes('-fullscreen', not co.attributes('-fullscreen'))

                def close_window():
                    co.destroy()
                
                minimize_button = Button(co, text='-', command=minimize_window)
                minimize_button.place(x=co.winfo_screenwidth() - 70, y=5)

                maximize_button = Button(co, text='❐', command=maximize_window)
                maximize_button.place(x=co.winfo_screenwidth() - 50, y=5)

                close_button = Button(co, text='X', command=close_window)
                close_button.place(x=co.winfo_screenwidth() - 30, y=5)

                num1=StringVar()
                one=StringVar()
                two=StringVar()
                
                def convert11():
                    a=str(num1.get())
                    b=[]
                    for i in a:
                        if (int(i)==0):
                            b.append(1)
                        if (int(i)==1):
                            b.append(0)
                    x=""
                    for j in b:
                        y=str(j)
                        x=x+y        
                    one.set(x)
                    c="1"
                    c1=str(int(x, 2)+int(c, 2))
                    s=bin(int(c1))
                    two.set(s)
                    
                def clear1111():
                    num1.set(0)
                    one.set("")
                    two.set("")
                    
                        
                def exit1111():
                    if messagebox.askyesno('Exit', "Do you really want to Exit"):
                        co.destroy()
                        bc.deiconify()
                    else:
                        co.deiconify() 
                        
                opr=Label(co, text="1's & 2's COMPLEMENT ", font="vani 30 bold", bg="white", fg="black", relief=GROOVE, justify=CENTER)
                opr.place(x=480, y=20)
                x=Label(co, text="Enter binary number = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=300, y=200)
                x=Label(co, text="1's Complement = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=300, y=300)
                x=Label(co, text="2's Complement = ", fg="black", background="aqua", font="times 25 bold")
                x.place(x=300, y=400)
                x=Entry(co, font="arial 25 bold", fg="black", relief=GROOVE, justify=CENTER, textvariable=num1)
                x.place(x=700, y=200)
                x=Entry(co, font="arial 25 bold", fg="black", state=DISABLED, relief=GROOVE, justify=CENTER, textvariable=one)
                x.place(x=700, y=300)
                x=Entry(co, font="arial 25 bold", fg="black", state=DISABLED, relief=GROOVE, justify=CENTER, textvariable=two)
                x.place(x=700, y=400)
                Button(co, text="clear", font="times 20 bold", fg="black", bg="white", command=clear1111).place(x=340, y=500)
                Button(co, text="Convert", font="times 20 bold", fg="black", bg="white", command=convert11).place(x=640, y=500)
                Button(co, text="Exit", font="times 20 bold", fg="black", bg="white", command=exit1111).place(x=940, y=500)
                co.mainloop()    
            else:
                messagebox.showerror('Sorry', "Please enter right command !")
                bc.deiconify()  
# ------------------------------------------------------------------------------------------------------------------------------------------------------
        def clear2():
            a2.set(0)
        
        def exit2():
            if messagebox.askyesno('Exit', "Do you really want to Exit"):
                bc.destroy()
            else:
                bc.deiconify()
                
        clearbutton=Button(bc, text="Clear", font="times 20 bold", fg="white", bg="black", command=clear2)
        clearbutton.place(x=920, y=400)
        enterbutton=Button(bc, text="Enter", font="times 20 bold", fg="white", bg="black", command=enter2)
        enterbutton.place(x=1120, y=400)
        exitbutton=Button(bc, text="Exit", font="times 20 bold", fg="white", bg="black", command=exit2)
        exitbutton.place(x=1320, y=400)
        bc.mainloop()

    if a1.get()==2:
# ------------------------------------------------------------------------------------------------------------------------------------------------------
        bcc=Toplevel()
        bcc.geometry("1620x950")
        bcc.title(" Bmi calculator")
        bcc.config(bg="aqua")
        bcc.attributes('-fullscreen', True)

        def minimize_window():
            bcc.iconify()
            bc.iconify()
            root.iconify()

        def maximize_window():
            bcc.attributes('-fullscreen', not bc.attributes('-fullscreen'))

        def close_window():
            bcc.destroy()
        
        minimize_button = Button(bcc, text='-', command=minimize_window)
        minimize_button.place(x=bcc.winfo_screenwidth() - 70, y=5)

        maximize_button = Button(bcc, text='❐', command=maximize_window)
        maximize_button.place(x=bcc.winfo_screenwidth() - 50, y=5)

        close_button = Button(bcc, text='X', command=close_window)
        close_button.place(x=bcc.winfo_screenwidth() - 30, y=5)

        heading=Label(bcc, text="BMI CALCULATOR", font="VANI 30 bold", fg="gold", bg="gray15")
        heading.place(x=480, y=10)
        weightvalue=Label(bcc, text="Weight (Kg) = ", font="times 25 bold", fg="black", background="aqua")
        weightvalue.place(x=300, y=80)
        heightvalue=Label(bcc, text="Height (Cm) = ", font="times 25 bold", fg="black", background="aqua")
        heightvalue.place(x=300, y=140)
        totalvalue=Label(bcc, text="BMI = ", font="times 25 bold", fg="black", background="aqua")
        totalvalue.place(x=300, y=200)

        a=StringVar()
        b=StringVar()
        T=StringVar()
        def clear1():
            a.set("")
            b.set("")
            T.set("")

        def calculate():
            c=int(a.get())
            d=int(b.get())/100
            e=c/(d*d)
            T.set(e)
            if e>0 and e<18.5:
                messagebox.showinfo('BMI',"You are underweight ! Focus on your health.")
                bcc.deiconify()
            if e>18.4 and e<25:
                messagebox.showinfo('BMI',"You are normal ! Maintain your health.")
                bcc.deiconify()
            if e>24.9 and e<30:
                messagebox.showwarning('BMI',"You are overweight ! Focus on your health.")
                bcc.deiconify()
            if e>29.9:
                messagebox.showwarning('BMI',"You are obese ! Focus on your health.")
                bcc.deiconify()

        def exit1():
            if messagebox.askyesno('Exit ', "Do you really want to exit"):
                bcc.destroy()
            else:
                bcc.deiconify()

        Entry(bcc, justify=CENTER, font="times 20 bold", textvariable=a).place(x=700, y=80)
        Entry(bcc, justify=CENTER, font="times 20 bold", textvariable=b).place(x=700, y=140)
        Entry(bcc, justify=CENTER, font="times 20 bold", state=DISABLED, textvariable=T).place(x=700, y=200)

        Button(bcc, font="times 25 bold", fg="white", bg="black", text="Clear", command=clear1).place(x=340, y=300)
        Button(bcc, font="times 25 bold", fg="white", text="Calculate", bg="black", command=calculate).place(x=640, y=300)
        Button(bcc, font="times 25 bold", fg="white", text="Exit", bg="black", command=exit1).place(x=940, y=300)
        bcc.mainloop()
    else:
        messagebox.showerror('Sorry', "Please enter right command !")
        
# ------------------------------------------------------------------------------------------------------------------------------------------------------

def clear1():
    a1.set(0)

def exit1():
    if messagebox.askyesno('Exit', "Do you really want to Exit"):
        root.destroy()
    else:
        root.deiconify()


a11=Label(root, text="ENTER THE COMMAND ", font="vani 19 bold", bg="gray15", fg="white")
a11.place(x=860, y=500)
a11entry=Entry(root, font="vani 20 bold", bg="white", fg="black", relief=GROOVE, justify=CENTER, textvariable=a1)
a11entry.place(x=1160, y=500)

clearbutton=Button(root, text="Clear", font="times 20 bold", fg="white", bg="black", command=clear1)
clearbutton.place(x=920, y=600)
enterbutton=Button(root, text="Enter", font="times 20 bold", fg="white", bg="black", command=enter1)
enterbutton.place(x=1120, y=600)
exitbutton=Button(root, text="Exit", font="times 20 bold", fg="white", bg="black", command=exit1)
exitbutton.place(x=1320, y=600)
root.mainloop()
# ------------------------------------------------------------------------------------------------------------------------------------------------------