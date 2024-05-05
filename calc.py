import sys
def add(one, two):
  return one + two

def subtract(left_number, right_number):
  return left_number - right_number

def multiply(left_number, right_number):
  return left_number * right_number

def divide(left_number, right_number):
  if(right_number == 0):
    raise ZeroDivisionError("Ти що, дебіл? Ділити на нуль не можна!!") 
  return round(left_number / right_number)

def main():
  left_number = int(sys.argv[1])
  right_number = int(sys.argv[3])
  operation = sys.argv[2]
  result = None
  print('left_number: ', left_number)
  print('right_number: ', right_number)
  print('operation: ', operation)

  match operation:
    case '+':
      result = add(left_number, right_number)
    case '-':
      result = subtract(left_number, right_number)
    case '*':
      result = multiply(left_number, right_number)
    case '/':
       result = divide(left_number, right_number)
    case 'divide':
      result = divide(left_number, right_number)

    case _ :
      raise ValueError('Unknown operation')

  print('result is: ', result)
  
main()