class CalcSystem():
    """
    Class for managing calculator state and performing math operations
    """
    # Constants for operations
    OP_DIVIDE = "/"
    OP_EQUALS = "="
    OP_MINUS = "-"
    OP_MULTIPLY = "*"
    OP_PLUS = "+"

    # Constants for values that aren't numbers
    VL_PLUSMINUS = "+/-"
    VL_DECIMAL = "."

    # Constants for clearing
    CLR_ALL = "CLRALL"
    CLR_ENTRY = "CLRENT"
    CLR_BCKSPC = "CLRBACK"

    # Constants for machine state
    ST_CLR = "cleared" # Fresh state, nothing input yet
    ST_EFN = "enteringfirstnumber"  # First number and operand input
    ST_EOP = "enteringoperand"      # Entering operand between first and second number
    ST_ESN = "enteringsecondnumber" # Second number input and equals or another operand were pressed

    def __init__(self):
        self.__state = self.ST_EFN  # State of the calculator 
        self.__display_value = 0    # Value shown on the display of the calculator
        self.__current_value = 0   # Current number being constructed 
        self.__previous_value = 0   # Value to be "operated on" by current value and operand
        self.__operand = None       # Operation to perform on current value and previous value

    def press_button(self, button_value):
        """
        Update calculator state based on button press
        """
        # if number is pressed:
        if button_value in range(0, 10):
            self.__update_current_value(button_value)
            # if state == ST_EFN:
                # build onto current value, there will be a valid previous value
            # if state == ST_ESN:
                # 
        # elif operation is pressed:
        elif button_value in [self.OP_DIVIDE, self.OP_MINUS, self.OP_MULTIPLY, self.OP_PLUS]:
            # set operand
            self.__operand = button_value
            # convert current number to previous number
            self.__previous_value = self.__current_value
            # set current_value back to zero
            self.__current_value = 0
            # update state of calculator
            self.__state = self.ST_ESN
        # elif clear is pressed

        # elif equals button is pressed and we are entering the second number
        elif button_value == self.OP_EQUALS and self.__state == self.ST_ESN:
            # calculate answer and set it equal to current value
            calculated_value = None
            if self.__operand == self.OP_DIVIDE:
                calculated_value = self.__previous_value / self.__current_value
            elif self.__operand == self.OP_MINUS:
                calculated_value = self.__previous_value - self.__current_value
            elif self.__operand == self.OP_MULTIPLY:
                calculated_value = self.__previous_value * self.__current_value
            elif self.__operand == self.OP_PLUS:
                calculated_value = self.__previous_value + self.__current_value

            self.__current_value = calculated_value
        
        elif button_value == self.CLR_ALL:
            # only implementing clear all for now
            self.__state = self.ST_EFN  # Set all values back to default
            self.__display_value = 0    
            self.__current_value = 0   
            self.__previous_value = 0   
            self.__operand = None 

        # Update display value
        self.__update_display_value()

    def __update_current_value(self, value):
        self.__current_value *= 10
        self.__current_value += value

    def __update_display_value(self):
        self.__display_value = self.__current_value

    def get_display_value(self):
        return self.__display_value