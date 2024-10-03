import tkinter as gi
#basic tkinter command
root = gi.Tk()
root.geometry("400x500")
root.title("Dk's Calc")

cal = ""  #the variable where i am saving the user inputs

label = gi.Label(root, text="", font=("Arial", 24), width=15, height=2) #text area for displaying the input and output
label.grid(columnspan=4, padx=10, pady=10)  

#basic fuctions starts here
def add_cal(symbol): #function for adding input together and making it as a ine string for passing into eval function
    global cal
    cal += str(symbol)
    label.config(text=cal) 

def evaluate(): #function that evaluate the string
    global cal
    try:
        cal = str(eval(cal))  
        label.config(text=cal)  
    except Exception:
        label.config(text="Error")  

def clearfield():  #function for clearing whole textarea
    global cal
    cal = ""  
    label.config(text="")  

def clear_last(): #function for backspace
    global cal
    cal = cal[:-1]   
    label.config(text=cal)  

button_config = {   #for changing the button configuration
    'width': 5,
    'height': 2,
    'font': ("Arial", 14)
}

#row 1
b1 = gi.Button(root, text="1", command=lambda: add_cal(1), **button_config)
b1.grid(row=2, column=0, padx=5, pady=5)
b2 = gi.Button(root, text="2", command=lambda: add_cal(2), **button_config)
b2.grid(row=2, column=1, padx=5, pady=5)
b3 = gi.Button(root, text="3", command=lambda: add_cal(3), **button_config)
b3.grid(row=2, column=2, padx=5, pady=5)
bx = gi.Button(root, text="*", command=lambda: add_cal("*"), **button_config)
bx.grid(row=2, column=3, padx=5, pady=5)

#row 2
b4 = gi.Button(root, text="4", command=lambda: add_cal(4), **button_config)
b4.grid(row=3, column=0, padx=5, pady=5)
b5 = gi.Button(root, text="5", command=lambda: add_cal(5), **button_config)
b5.grid(row=3, column=1, padx=5, pady=5)
b6 = gi.Button(root, text="6", command=lambda: add_cal(6), **button_config)
b6.grid(row=3, column=2, padx=5, pady=5)
bd = gi.Button(root, text="/", command=lambda: add_cal("/"), **button_config)
bd.grid(row=3, column=3, padx=5, pady=5)

#row 3
b7 = gi.Button(root, text="7", command=lambda: add_cal(7), **button_config)
b7.grid(row=4, column=0, padx=5, pady=5)
b8 = gi.Button(root, text="8", command=lambda: add_cal(8), **button_config)
b8.grid(row=4, column=1, padx=5, pady=5)
b9 = gi.Button(root, text="9", command=lambda: add_cal(9), **button_config)
b9.grid(row=4, column=2, padx=5, pady=5)
ba = gi.Button(root, text="+", command=lambda: add_cal("+"), **button_config)
ba.grid(row=4, column=3, padx=5, pady=5)

#row 4
bm = gi.Button(root, text="%", command=lambda: add_cal("%"), **button_config)
bm.grid(row=5, column=0, padx=5, pady=5)
b0 = gi.Button(root, text="0", command=lambda: add_cal(0), **button_config)
b0.grid(row=5, column=1, padx=5, pady=5)
bq = gi.Button(root, text=".", command=lambda: add_cal("."), **button_config)
bq.grid(row=5, column=2, padx=5, pady=5)
bs = gi.Button(root, text="-", command=lambda: add_cal("-"), **button_config)
bs.grid(row=5, column=3, padx=5, pady=5)

#row 5
bbackspace = gi.Button(root, text="⌫", command=clear_last, **button_config) #backspace button
bbackspace.grid(row=6, column=3, padx=5, pady=5)
bopen = gi.Button(root, text="(", command=lambda: add_cal("("), **button_config)
bopen.grid(row=6, column=0, padx=5, pady=5)
bclose = gi.Button(root, text=")", command=lambda: add_cal(")"), **button_config)
bclose.grid(row=6, column=1, padx=5, pady=5)
bclear = gi.Button(root, text="clr", command=clearfield, **button_config) # clear button
bclear.grid(row=6, column=2, padx=5, pady=5)

#row 6
bequal = gi.Button(root, text="=", command=evaluate, width=15, height=2, font=("Arial", 16)) # equal button
bequal.grid(row=7, column=0, columnspan=5, padx=5, pady=5)  

root.mainloop() #thing that runs the whole program 