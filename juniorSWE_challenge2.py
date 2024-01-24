"""

Author: Cole Emerine

Challenge #2 for Junior Software Engineer
TAMID Group Application

"""


#calculate function that takes in the parameters for the numbers and the calculation
def calculate(num1, num2, symbol):
    value = 0
    if symbol == "+":
        value = num1 + num2
    elif symbol == "-":
        value = num1 - num2
    elif symbol == "*":
        value = num1*num2
    elif symbol == "/":
        value = num1/num2
    elif symbol == "%":
        value = num1%num2
    else:
        return "\nPlease enter one of these symbols (+-*/%) for function.\n"

    return "\nYour result was: "+str(value)


#I didn't have to break this calculator into two functions main() and calculate()
#but I feel this gives the file a better overall read
def main():
    print("Welcome to the TAMID Calculator!")

    while(True):

        choice = input("\nWould you like to calculate something (y/n): ")
        if choice == 'n':
            break

        #this try except catch, catches if the user doesn't enter a number or if they divide by 0
        try:
            num1 = int(input("\nPlease enter the first number: "))
            num2 = int(input("Please enter the second number: "))
            symbol = input("Please enter your function: ")

            print(calculate(num1, num2, symbol))


        except ValueError:
            print("\nPlease only enter numbers where asked.")
        except ZeroDivisionError:
            print("\nYou cannot divide by 0!")



    print("\nThanks for coming!")

if __name__ == "__main__":
    main()