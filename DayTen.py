## Functions with output- Calculator Assignment

# function return single value
def format_name(fname, lname):
    formatted_f_name = fname.title()
    formatted_l_name = lname.title()
    return f"{formatted_f_name} {formatted_l_name}"


print(format_name("YogEsh","aAYush"))

#Calculator functons


def add(n1,n2):
    return n1+n2


def subtract(n1,n2):
    return n1-n2


def multiply(n1,n2):
    return n1*n2


def devide(n1,n2):
    return n1/n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":devide
}

def calculator():
    num1 = int(input("Please enter first number"))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Please pick the operation from lines above")
        num2 = int(input("Please enter second number"))
        calculate_function = operations[operation_symbol]
        result = calculate_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")
        if input(f"type 'y' to continue with {result} or type 'n' to start new  calculations :") == 'y':
            num1 = result
        else:
            should_continue = False
            calculator()


calculator()