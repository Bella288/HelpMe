def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


num1 = float(text_prompt('>Enter your first number - n1 : '))
print('>Type the shortcut for your mathematical operation: Multiply is X, Subtract n1')
print('from n2 (2-1) is S1, Subtract n2 from n1 (1-2) is S2, Exponent is E, and Divide')
print('input1/input2) is D.')
op = text_prompt('>Type operation shortcut - see above: ')
num2 = float(text_prompt('>Enter your second number - n2: '))
def operate1():
  if op.upper() == 'X': 
    return (num1 * num2)
  elif op.upper() == 'S1':
   return (num2 - num1)
  elif op.upper() == 'S2':
    return (num1 - num2)
  elif op.upper() == 'E':
    return (num1 ** num2)
  elif op.upper() == 'D':
    return (num1 / num2)
  elif op.upper() == 'A':
    return (num1 + num2)

ans = operate1()
print('>Your answer is: ', ans)
yn = text_prompt('Do you want to use your answer in a calculation? (y/n) ')
if yn.upper() == 'Y':
  print('>Type the shortcut for your mathematical operation: Multiply is X, Subtract')
  print(' answer from new input (3-a) is S1, Subtract new input from answer (a-3) is')
  print('(S2, Expopnent (answer ^ new input) is E, and divide (answer/newInput) is D.')

def operate2():
  ans = operate1()
  op2 = text_prompt('>Type operation shortcut - see above: ')
  num3 = float(text_prompt('>Enter your new input number - n3 AKA 3: '))
  if op2.upper() == 'X': 
    return (ans * num3)
  elif op2.upper() == 'S1':
    return (ans - num3)
  elif op2.upper() == 'S2':
    return (num3 - ans)
  elif op2.upper() == 'E':
    return (ans ** num3)
  elif op2.upper() == 'D':
    return (ans / num3)
  elif op2.upper() == 'A':
    return (ans + num3)


print('Your answer is: ', operate2())
