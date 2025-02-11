# Writting by mohammad hossein yaghubi
# mail: m.h.yaghubi.info@gmail.com
#------------------------------------------
import tkinter as tk
from tkinter import messagebox

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        w=330
        h=440
        ws=self.winfo_screenwidth()
        hs=self.winfo_screenheight()
        x=(ws/2)-(w/2)
        y=(hs/2)-(h/2)
        self.geometry("%dx%d+%d+%d"%(w,h,x,y))
        # self.geometry("320x500")
        self.configure(background="#999696") 

        self.expression = ""
        self.input_text = tk.StringVar()

        # Build input frame
        input_frame = tk.Frame(self, width=300, height=50, bd=0)
        input_frame.pack(side=tk.TOP)
        
        # Number validator
        vcmd = (self.register(self.validate), "%P")

        input_field = tk.Entry(input_frame, font=('arial', 26, 'bold'), textvariable=self.input_text, width=50, bg="#eee", relief='groove', bd=10, justify=tk.RIGHT, validate="key", validatecommand=vcmd)
        input_field.grid(row=0, column=3)
        input_field.pack(ipady=50)

        # Build button
        btns_frame = tk.Frame(self, width=500, height=400, bg="#999696")
        btns_frame.pack(pady=5)

        # Row 1
        clear = tk.Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=self.clear).grid(row=0, column=0, columnspan=3)
        divide = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", activebackground="blue", activeforeground="white", command=lambda: self.click("/")).grid(row=0, column=3, padx=1 ,pady=1)

        # Row 2
        seven = tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click(7)).grid(row=1, column=0)
        eight = tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click(8)).grid(row=1, column=1)
        nine = tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click(9)).grid(row=1, column=2)
        multiply = tk.Button(btns_frame, text="x", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", activebackground="blue", activeforeground="white", command=lambda: self.click("*")).grid(row=1, column=3,pady=1)

        # Row 3
        four = tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click(4)).grid(row=2, column=0)
        five = tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click(5)).grid(row=2, column=1, padx=2)
        six = tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click(6)).grid(row=2, column=2)
        minus = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", activebackground="blue", activeforeground="white", command=lambda: self.click("-")).grid(row=2, column=3, pady=1,padx=2)

        # Row 4
        one = tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click(1)).grid(row=3, column=0)
        two = tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click(2)).grid(row=3, column=1)
        three = tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click(3)).grid(row=3, column=2)
        plus = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", activebackground="blue", activeforeground="white", command=lambda: self.click("+")).grid(row=3, column=3, pady=1)

        # Row 5
        zero = tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.click(0)).grid(row=4, column=0, columnspan=2,)
        point = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.click(".")).grid(row=4, column=2)
        equals = tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", activebackground="blue", activeforeground="white", command=self.evaluate).grid(row=4, column=3, pady=1)

    #----------- Functions ---------------------
    def validate(self,P):
        if P == "" or (P.isdigit() and len(P) <= 16):
            return True
        else:
            return False

    def click(self, item):
        if len(self.expression) < 16:
            self.expression = self.expression + str(item)
            self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = ""
        except:
            messagebox.showerror("Error", "Invalid input")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()