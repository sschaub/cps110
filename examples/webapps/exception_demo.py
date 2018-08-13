try:
   ageStr = input('Enter your age:')
   age = int(ageStr)
   print('You are', age, 'years old.')
except Exception as esmerelda:
   print('Something went wrong: ', esmerelda)

