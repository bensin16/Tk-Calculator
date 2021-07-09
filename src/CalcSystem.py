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

    def __init__(self):
        """
        Constructor
        """
        self.__display_value = 0

    def press_button(self, button):
        """
        Update calculator state based on pressed button
        @param button: value of pressed button
        """
        self.__display_value = button

    def get_display_value(self):
        return self.__display_value