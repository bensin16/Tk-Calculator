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
    OP_EXP = "^"

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
    ST_AFTEQ = "afterequals"        # After equals is pressed

    def __init__(self):
        self.__state = self.ST_EFN  # State of the calculator 
        self.__display_value = 0    # Value shown on the display of the calculator
        self.__current_value = 0    # Current number being constructed 
        self.__previous_value = 0   # Value to be "operated on" by current value and operand
        self.__operand = None       # Operation to perform on current value and previous value

    def press_button(self, button_value):
        """
        Update calculator state based on button press
        """
        # if number is pressed:
        if button_value in range(0, 10):
            if self.__state == self.ST_AFTEQ:   # if number pushed after equals calculated, reset and start from beginning
                self.__clear_calculator()   # clear before doing any operations when entering first number
            self.__update_current_value(button_value)
        elif button_value == self.VL_PLUSMINUS: # if plus minus is hit, switch to opposite sign
            self.__current_value *= -1
        # elif operation is pressed:
        elif button_value in [self.OP_DIVIDE, self.OP_EXP, self.OP_MINUS, self.OP_MULTIPLY, self.OP_PLUS]:
            if self.__state == self.ST_ESN:
                # if entering second number, calculate what was in calculator then continue
                self.__calculate()
            # set operand
            self.__operand = button_value
            # convert current number to previous number
            self.__previous_value = self.__current_value
            # set current_value back to zero
            self.__current_value = 0
            # update state of calculator
            self.__state = self.ST_ESN
        # elif equals button is pressed and we are entering the second number
        elif button_value == self.OP_EQUALS and self.__state == self.ST_ESN:
            # calculate answer 
            self.__calculate()
        # elif clear is pressed
        elif button_value == self.CLR_ALL:
            # only implementing clear all for now
            # Set all values back to default
            self.__clear_calculator()

        # Update display value
        self.__update_display_value()

    def __clear_calculator(self):
        """
        Reset all values to initial values
        """
        self.__state = self.ST_EFN  
        self.__display_value = 0    
        self.__current_value = 0   
        self.__previous_value = 0   
        self.__operand = None 

    def __calculate(self):
        """
        Calculate answer based on previous and current value and operand. Sets answer to the new current value
        """
        calculated_value = None
        if self.__operand == self.OP_DIVIDE:
            calculated_value = self.__previous_value / self.__current_value
        elif self.__operand == self.OP_MINUS:
            calculated_value = self.__previous_value - self.__current_value
        elif self.__operand == self.OP_MULTIPLY:
            calculated_value = self.__previous_value * self.__current_value
        elif self.__operand == self.OP_PLUS:
            calculated_value = self.__previous_value + self.__current_value
        elif self.__operand == self.OP_EXP:
            calculated_value = self.__calculate_power(self.__previous_value, self.__current_value)

        self.__current_value = calculated_value
        self.__state = self.ST_AFTEQ  # Update the state to be entering the first number

    def calculate_power(self, base, exponent):
        """
        2 ^ 2 = 4
        2 ^ 3 = 8
        """
        calculated_value = 1

        # return 1 if exponent is 0
        if exponent == 0:
            return 1

        # return 0 if the base is 0 to bypass unnecessary calculations
        if base == 0:
            return 0

        #if exponent is negative
        for i in range(abs(exponent)):
            calculated_value *= base

        # if exp is negative
        if exponent < 0:
            # answer is going to be 1 / base^exp
            calculated_value = 1 / calculated_value

        return calculated_value


    def __update_current_value(self, value):
        self.__current_value *= 10
        self.__current_value += value

    def __update_display_value(self):
        self.__display_value = self.__current_value

    def get_display_value(self):
        return self.__display_value