from tkinter import *

window=Tk()
window.geometry("600x600")

label=Label(window,bg="grey",fg="white",width=65,height=4)
label.place(x=40,y=10)

button_clear=Button(window,text='C',width=7,height=3)
button_clear.grid(row=0,column=3,padx=36,pady=(125,15))

button7=Button(window,text=7,width=7,height=3)
button7.grid(row=1,column=0,padx=30,pady=15)
button8=Button(window,text=8,width=7,height=3)
button8.grid(row=1,column=1,padx=30,pady=15)
button9=Button(window,text=9,width=7,height=3)
button9.grid(row=1,column=2,padx=30,pady=15)
button_equal=Button(window,text='=',width=7,height=3)
button_equal.grid(row=1,column=3,padx=30,pady=15)

button4=Button(window,text=4,width=7,height=3)
button4.grid(row=2,column=0,padx=30,pady=15)
button5=Button(window,text=5,width=7,height=3)
button5.grid(row=2,column=1,padx=30,pady=15)
button6=Button(window,text=6,width=7,height=3)
button6.grid(row=2,column=2,padx=30,pady=15)
button_divide=Button(window,text='/',width=7,height=3)
button_divide.grid(row=2,column=3,padx=30,pady=15)

button1=Button(window,text=1,width=7,height=3)
button1.grid(row=3,column=0,padx=30,pady=15)
button2=Button(window,text=2,width=7,height=3)
button2.grid(row=3,column=1,padx=30,pady=15)
button3=Button(window,text=3,width=7,height=3)
button3.grid(row=3,column=2,padx=30,pady=15)
button_multiply=Button(window,text='x',width=7,height=3)
button_multiply.grid(row=3,column=3,padx=30,pady=15)

button0=Button(window,text=0,width=7,height=3)
button0.grid(row=4,column=0,padx=30,pady=15)
button_decimal=Button(window,text='.',width=7,height=3)
button_decimal.grid(row=4,column=1,padx=30,pady=15)
button_add=Button(window,text='+',width=7,height=3)
button_add.grid(row=4,column=2,padx=30,pady=15)
button_subtract=Button(window,text='-',width=7,height=3)
button_subtract.grid(row=4,column=3,padx=30,pady=15)

window.mainloop()
