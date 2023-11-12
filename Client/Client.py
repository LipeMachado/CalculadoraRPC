import zerorpc

client = zerorpc.Client()
client.connect("tcp://127.0.0.1:4242")

def menu():
    print("Choose a operation:")
    print("1 - Sum")
    print("2 - Subtract")
    print("3 - Multiplication")
    print("4 - Divide")
    choice = int(input("Digit a number for operation: "))
    return choice

choice = menu()

first_number = int(input("Digit the first number: "))
second_number = int(input("Digit the second number: "))

if choice == 1:
    result = client.sum(first_number, second_number)
    operation_name = "Sum"
    operation_symbol = "+"
elif choice == 2:
    result = client.subtract(first_number, second_number)
    operation_name = "Subtract"
    operation_symbol = "-"
elif choice == 3:
    result = client.multiplication(first_number, second_number)
    operation_name = "Multiply"
    operation_symbol = "*"
elif choice == 4:
    result = client.divide(first_number, second_number)
    operation_name = "Divide"
    operation_symbol = "/"
else:
    print("Invalid Choose")
    result = None
    operation_name = None

if result is not None:
    print(f"Result {operation_name}: {first_number} {operation_symbol} {second_number} = {result}")