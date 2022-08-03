from art import logo 

def add(n1, n2):
    return n1 + n2 

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
} 

def calculator():
    print(logo)

    num1 = float(input("What is the first number? "))

    for symbol in operations_dict:
        print(symbol)

    should_continue = True

    while should_continue:
        operational_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is your next number? "))
        calculation_fuction = operations_dict[operational_symbol]
        answer = calculation_fuction(num1, num2)
        rounded_answer = round(answer, 2)

        print(f'{num1} {operational_symbol} {num2} = {rounded_answer}')

        keep_going = input(f'Type "y" to continue calculating with {rounded_answer}, type "k" to start a new calculation, or "n" to exit: '.lower())
        if keep_going == 'y':
            num1 = rounded_answer 
        elif keep_going == 'k':
            calculator()
        elif keep_going == 'n':
            should_continue == False
            break
        
calculator()