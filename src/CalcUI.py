import tkinter as tk

# Constants
BUTTON_WIDTH = 7
BUTTON_HEIGHT = 3
WINDOW_SIZE = "280x400"

class CalcUI():
    def __init__(self, root):

        # Create GUI elements
        root.geometry(WINDOW_SIZE)  #set window size
        
        # label for calculator display
        self.lbl_display = tk.Label(master=root, text="0", width=35, height=5, borderwidth=2, relief=tk.GROOVE)

        # generate form for button grid
        frm_buttons = tk.Frame(master=root)
        frm_buttons.rowconfigure(5, minsize=50, uniform=True, pad=5)
        frm_buttons.columnconfigure([0, 1, 2, 3], minsize=50, uniform=True, pad=5)

        #Initialize number buttons, +/- button, and . button
        btn_nine = tk.Button(master=frm_buttons, text="9", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command= lambda: self.handle_button_press(9))    
        btn_eight = tk.Button(master=frm_buttons, text="8", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command= lambda: self.handle_button_press(8))
        btn_seven = tk.Button(master=frm_buttons, text="7", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command= lambda: self.handle_button_press(7))
        btn_six = tk.Button(master=frm_buttons, text="6", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command= lambda: self.handle_button_press(6))
        btn_five = tk.Button(master=frm_buttons, text="5", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command= lambda: self.handle_button_press(5))
        btn_four = tk.Button(master=frm_buttons, text="4", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command= lambda: self.handle_button_press(4))
        btn_three = tk.Button(master=frm_buttons, text="3", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command= lambda: self.handle_button_press(3))
        btn_two = tk.Button(master=frm_buttons, text="2", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command= lambda: self.handle_button_press(2))
        btn_one = tk.Button(master=frm_buttons, text="1", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command= lambda: self.handle_button_press(1))
        btn_plus_minus = tk.Button(master=frm_buttons, text="+/-", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command= lambda: self.handle_button_press("+/-"))
        btn_zero = tk.Button(master=frm_buttons, text="0", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command= lambda: self.handle_button_press(0))
        btn_decimal = tk.Button(master=frm_buttons, text=".", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command= lambda: self.handle_button_press("."))

        # place buttons on grid
        btn_nine.grid(row=1, column=2, sticky="nsew")
        btn_eight.grid(row=1, column=1, sticky="nsew")
        btn_seven.grid(row=1, column=0, sticky="nsew")
        btn_six.grid(row=2, column=2, sticky="nsew")
        btn_five.grid(row=2, column=1, sticky="nsew")
        btn_four.grid(row=2, column=0, sticky="nsew")
        btn_three.grid(row=3, column=2, sticky="nsew")
        btn_two.grid(row=3, column=1, sticky="nsew")
        btn_one.grid(row=3, column=0, sticky="nsew")
        btn_plus_minus.grid(row=4, column=0, sticky="nsew")
        btn_zero.grid(row=4, column=1, sticky="nsew")
        btn_decimal.grid(row=4, column=2, sticky="nsew")

        # Pack display label and buttons 
        self.lbl_display.pack()
        frm_buttons.pack(side=tk.BOTTOM)

    def handle_button_press(self, button):
        pass

    def __update_display(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    calc_gui = CalcUI(root)
    root.mainloop()