#from replit import clear
#from artr import cal


def add(n1, n2):
  return n1 + n2


def subtract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 * n2


def divide(n1, n2):
  return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

cal="""
  ____      _            _       _             
 / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| |__| (_| | | (__| |_| | | (_| | || (_) | |   
 \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   


"""

def calucator():
  print(cal)
  num1 = float(input("What is the first number? \n"))
  for symbols in operations:
    print(symbols)
  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation :")
    num2 = float(input("What is the second number?\n"))

    func = operations[operation_symbol]
    result = func(num1, num2)
    print(f"{num1} {operation_symbol} {num2}={result}")

    if input("Do you want to continue? press 'y' for yes and 'n' for no :") == 'y':
      num1 = result
    else:
      should_continue = False

      calucator()


calucator()
