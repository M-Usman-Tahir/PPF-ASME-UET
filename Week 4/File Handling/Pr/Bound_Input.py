import sys

def check (A_str, Valid_Inputs): 
    while True:
        Input=input(A_str)
        if (Input not in Valid_Inputs) or Input in "(/)":
            if Input=="exit":
                print("System Exited!!!")
                sys.exit()
            print("Input Error: InValid input")
            print("Valid Inputs",Valid_Inputs,"OR Enter \"exit\" to Exit")
        else:
            return Input