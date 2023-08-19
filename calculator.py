def calculator():
    operation = input(''' 
Please type the operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = float(input("Please enter the first number: "))
    number_2 = float(input("Please enter the second number: "))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)
    elif operation == "-":
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)
    elif operation == "*":
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)
    elif operation == "/":
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)
    else:
        print('You have entered a wrong math operator!')

    again()


def again():
    calculation_again = input('''    
Do you want to calculate again?
Please type Y for yes or N for no
''')

    if calculation_again.upper() == 'Y':
        calculator()
    elif calculation_again.upper() == 'N':
        print("Bye bye! Thank you for using the calculator.")
    else:
        again()


calculator()