### 問答申論題 ###
'''
number = int(input('Please insert a positive interger.'))

def get_is_odd(number):
  if number % 2 != 0:
    return True
  else:
    return False

print(get_is_odd(number))
'''

### 程式設計實作題 ###
# from num_module import get_is_odd, get_is_even
from num_module import get_is_odd
from num_module import get_is_even

insert_num = int(input("Please input a positive integer."))

print('Is it odd? Ans: '+ str(get_is_odd(insert_num)))
print('Is it even? Ans: '+ str(get_is_even(insert_num)))