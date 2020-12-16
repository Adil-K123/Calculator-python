from tkinter import *


def button_click(num):
    global expression
    if entry.get() != "Division by Zero is undefined":
        expression = expression + str(num)
        input_text.set(expression)


def clear_click():
    global expression
    global code
    global first_operator_click
    code = ''
    first_operator_click = TRUE
    expression = ''
    input_text.set(expression)


def operator_click(op):
    global first_operator_click
    global code
    global expression
    global old_value
    if first_operator_click:
        if op == '+':
            code = 1
        elif op == '-':
            code = 2
        elif op == 'x':
            code = 3
        elif op == '/':
            code = 4
        first_operator_click = FALSE
        old_value = float(entry.get())
    else:
        inter_value = float(entry.get())
        if code == 1:
            old_value = old_value + inter_value
        elif code == 2:
            old_value = old_value - inter_value
        elif code == 3:
            old_value = old_value * inter_value
        elif code == 4:
            if inter_value != 0:
                old_value = old_value / inter_value
            else:
                expression = "Division by Zero is undefined"
        if op == '+':
            code = 1
        elif op == '-':
            code = 2
        elif op == 'x':
            code = 3
        elif op == '/':
            code = 4
    if expression == "Division by Zero is undefined":
        input_text.set(expression)
    else:
        expression = ""
        input_text.set(expression)


def equal_click():
    new_value = float(entry.get())
    global old_value
    result = ''
    global code
    global first_operator_click
    if code == 1:
        result = old_value + new_value
    elif code == 2:
        result = old_value - new_value
    elif code == 3:
        result = old_value * new_value
    elif code == 4:
        if new_value != 0:
            result = old_value / new_value
        else:
            result = "Division by Zero is undefined"
    input_text.set(str(result))
    code = ""
    first_operator_click = TRUE


window = Tk()
window.geometry("600x600")
window.title("Calculator")

old_value = ""
expression = ""
input_text = StringVar()
code = ""
first_operator_click = TRUE

entry = Entry(window, bg="grey", fg="white", width=65,textvariable=input_text,justify=RIGHT)
entry.place(x=40, y=10, height=65)

button_clear = Button(window, text='C', width=7, height=3, command=clear_click)
button_clear.grid(row=0, column=3, padx=36, pady=(125, 15))

button7 = Button(window, text=7, width=7, height=3, command=lambda: button_click(7))
button7.grid(row=1, column=0, padx=30, pady=15)
button8 = Button(window, text=8, width=7, height=3, command=lambda: button_click(8))
button8.grid(row=1, column=1, padx=30, pady=15)
button9 = Button(window, text=9, width=7, height=3, command=lambda: button_click(9))
button9.grid(row=1, column=2, padx=30, pady=15)
button_equal = Button(window, text='=', width=7, height=3, command=equal_click)
button_equal.grid(row=1, column=3, padx=30, pady=15)

button4 = Button(window, text=4, width=7, height=3, command=lambda: button_click(4))
button4.grid(row=2, column=0, padx=30, pady=15)
button5 = Button(window, text=5, width=7, height=3, command=lambda: button_click(5))
button5.grid(row=2, column=1, padx=30, pady=15)
button6 = Button(window, text=6, width=7, height=3, command=lambda: button_click(6))
button6.grid(row=2, column=2, padx=30, pady=15)
button_divide = Button(window, text='/', width=7, height=3, command=lambda: operator_click('/'))
button_divide.grid(row=2, column=3, padx=30, pady=15)

button1 = Button(window, text=1, width=7, height=3, command=lambda: button_click(1))
button1.grid(row=3, column=0, padx=30, pady=15)
button2 = Button(window, text=2, width=7, height=3, command=lambda: button_click(2))
button2.grid(row=3, column=1, padx=30, pady=15)
button3 = Button(window, text=3, width=7, height=3, command=lambda: button_click(3))
button3.grid(row=3, column=2, padx=30, pady=15)
button_multiply = Button(window, text='x', width=7, height=3, command=lambda: operator_click('x'))
button_multiply.grid(row=3, column=3, padx=30, pady=15)

button0 = Button(window, text=0, width=7, height=3, command=lambda: button_click(0))
button0.grid(row=4, column=0, padx=30, pady=15)
button_decimal = Button(window, text='.', width=7, height=3, command=lambda: button_click('.'))
button_decimal.grid(row=4, column=1, padx=30, pady=15)
button_add = Button(window, text='+', width=7, height=3, command=lambda: operator_click('+'))
button_add.grid(row=4, column=2, padx=30, pady=15)
button_subtract = Button(window, text='-', width=7, height=3, command=lambda: operator_click('-'))
button_subtract.grid(row=4, column=3, padx=30, pady=15)

window.mainloop()
