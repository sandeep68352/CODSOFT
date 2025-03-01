def add(n1,n2):
    return n1 + n2
def substract(n1,n2):
    return n1 - n2
def multiply (n1,n2):
    return n1 * n2
def divide (n1,n2):
    return n1 / n2 

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide,
}
def calculator ():
    should_accmulate = True
    num1 = float(input("what's your frist number : "))
    while should_accmulate :
        for symbol in operations :
            print(symbol)
        operator_symbol = input("pick up operator :")    
        num2 = float(input("what's your second number :"))
        solution = operations[operator_symbol](num1,num2)
        print(f"{num1} {operator_symbol} {num2} = {solution}")

        choice = input(f"type 'y' to continue the calculator with {solution} , or type 'n' to start a new cal calculator: ")

        if choice == "y":
            num1 = solution 
        else:
            should_accmulate = False
            print("\n" * 20)
            calculator()
            
calculator()