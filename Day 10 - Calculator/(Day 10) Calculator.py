import os

# Clear terminal
def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

# Add
def add(n1,n2):
  """Returns n1 + n2"""
  return n1 + n2

# Subtract
def subtract(n1,n2):
  """Returns n1 - n2"""
  return n1 - n2

# Multiply
def multiply(n1,n2):
  """Returns n1 * n2"""
  return n1 * n2

# Divide
def divide(n1,n2):
  """Returns n1 / n2"""
  return n1 / n2

# functions_dict
functions_dict = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}
def calculator_app():
    # Welcome
    print("Welcome to Calculator App!")

    # User inputs
    ## num1
    while True:
        num1 = input("What's the first number?\n")
        try:
            float(num1)
        except:
            print("Invalid. Please key in number.\n")
        else:
            num1 = float(num1)
            break

    #Loop as long as user wants
    while True:
        # Print list of functions
        print("\n")
        print(list(functions_dict.keys()))

        # Get user choice of operation
        while True:
            func_choice = input("Choose the operator to run.\n")
            if func_choice not in list(functions_dict.keys()):
                print("Invalid. Please choose valid operator to run.")
            else:
                break


        ## num2
        while True:
            num2 = input("\nWhat's the next number?\n")
            try:
                float(num2)
            except:
                print("Invalid. Please key in number.\n")
            else:
                num2 = float(num2)
                break

        # Calculate
        function_to_run = functions_dict[func_choice]
        calculated_answer = function_to_run(num1, num2)

        # Display results
        print("\n{} {} {} = {:.2f}\n".format(num1, func_choice, num2, calculated_answer))

        # Ask to continue
        while True:
            cont_calc = input("Do you want to continue with this calculation? (Y/N)\n").lower()
            if cont_calc in ["y","n"]:
                break
        
        if cont_calc == "y":
            num1 = round(calculated_answer,2)
            clearConsole()
            print(f"Your current subtotal is {num1}\n")
        
        else:
            while True:
                new_calc = input("Do you want to start a new calculation? (Y/N)\n").lower()
                if new_calc in ["y","n"]:
                    break
            
        if new_calc == "y":
                clearConsole()
                calculator_app()
            
        else:
            print("Thank you for using Calculator. Goodbye!")
            break
        break

calculator_app()