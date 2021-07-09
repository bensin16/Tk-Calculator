import tkinter as tk
from CalcSystem import CalcSystem as cs

# Constants
BUTTON_WIDTH = 7
BUTTON_HEIGHT = 3
WINDOW_SIZE = "280x400"

class CalcUI():
    def __init__(self, root):
        # Initalize calculator system object
        self.__cs = cs()

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
        btn_plus_minus = tk.Button(master=frm_buttons, text="+/-", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command= lambda: self.handle_button_press(cs.VL_PLUSMINUS))
        btn_zero = tk.Button(master=frm_buttons, text="0", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command= lambda: self.handle_button_press(0))
        btn_decimal = tk.Button(master=frm_buttons, text=".", width=BUTTON_WIDTH, height=BUTTON_HEIGHT, command= lambda: self.handle_button_press(cs.VL_DECIMAL))

        # Initalize arithmetic buttons
        btn_divide = tk.Button(master=frm_buttons, text="/", command= lambda: self.handle_button_press(cs.OP_DIVIDE))
        btn_minus = tk.Button(master=frm_buttons, text="-", command= lambda: self.handle_button_press(cs.OP_MINUS))
        btn_multiply = tk.Button(master=frm_buttons, text="*", command= lambda: self.handle_button_press(cs.OP_MULTIPLY))
        btn_plus = tk.Button(master=frm_buttons, text="+", command= lambda: self.handle_button_press(cs.OP_PLUS))
        btn_equals = tk.Button(master=frm_buttons, text="=", command= lambda: self.handle_button_press(cs.OP_EQUALS))

        # Initalize Clear buttons
        btn_clear = tk.Button(master=frm_buttons, text="C", command= lambda: self.handle_button_press(cs.CLR_ALL))
        btn_clear_entry = tk.Button(master=frm_buttons, text="CE", command= lambda: self.handle_button_press(cs.CLR_ENTRY))
        btn_delete = tk.Button(master=frm_buttons, text="DEL", command= lambda: self.handle_button_press(cs.CLR_BCKSPC))

        # place buttons on grid
        # grouped by row from left to right for readability
        btn_clear.grid(row=0, column=1, sticky="nsew")
        btn_clear_entry.grid(row=0, column=2, sticky="nsew")
        btn_delete.grid(row=0, column=3, sticky="nsew")

        btn_seven.grid(row=1, column=0, sticky="nsew")
        btn_eight.grid(row=1, column=1, sticky="nsew")
        btn_nine.grid(row=1, column=2, sticky="nsew")
        btn_divide.grid(row=1, column=3, sticky="nsew")

        btn_four.grid(row=2, column=0, sticky="nsew")
        btn_five.grid(row=2, column=1, sticky="nsew")
        btn_six.grid(row=2, column=2, sticky="nsew")
        btn_multiply.grid(row=2, column=3, sticky="nsew")

        btn_one.grid(row=3, column=0, sticky="nsew")
        btn_two.grid(row=3, column=1, sticky="nsew")
        btn_three.grid(row=3, column=2, sticky="nsew")
        btn_minus.grid(row=3, column=3, sticky="nsew")

        btn_plus_minus.grid(row=4, column=0, sticky="nsew")
        btn_zero.grid(row=4, column=1, sticky="nsew")
        btn_decimal.grid(row=4, column=2, sticky="nsew")
        btn_plus.grid(row=4, column=3, sticky="nsew")

        btn_equals.grid(row=5, column=0, columnspan=4, sticky="nsew")

        # Pack display label and buttons 
        self.lbl_display.pack()
        frm_buttons.pack(side=tk.BOTTOM)

    def handle_button_press(self, button):
        """
        Update state of calculator based on button press
        """
        self.__cs.press_button(button)  # send button press to calculator logic
        self.__update_display()         # update display of calculator after state change

    def __update_display(self):
        """
        Update text on label used for display
        """
        self.lbl_display["text"] = self.__cs.get_display_value()

if __name__ == "__main__":
    root = tk.Tk()
    calc_gui = CalcUI(root)
    root.mainloop()