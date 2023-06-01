### 問答申論題 ###
# for loop #
'''
number = int(input("Please insert a number:"))
num_list = list(range(1, number+1))

count = 0
for i in num_list:
  count += i

print("1+2+3+...+"+str(number)+" -> "+str(count))
'''
# while loop #
'''
number = int(input("Please insert a number:"))
num_list = list(range(1, number+1))

i = 1 # inital count number 
result = 0
while i <= number:
  result += i
  i += 1

print("1+2+3+...+"+str(number)+" -> "+str(result))
'''

### 程式設計實作題 ###
import number_utils as nu

number = int(input("Please insert a positive number:"))
judge_odd = nu.get_is_odd(number)

judge_prime = nu.get_is_prime_number(number)