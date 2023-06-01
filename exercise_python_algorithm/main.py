### 問答申論題 ###
'''
N = 10 
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
當 N = 10, 值：55

def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

N = 10 
result = fibonacci(N)
print(result)
'''

### 程式實作題 ###


insert_list = input("請輸入一連串數字：")
unsorted_list = insert_list.split(',')

for ind, val in enumerate(unsorted_list):
  unsorted_list[ind] = int(val)
  
print("排列前："+str(unsorted_list))

def bubble_sort(list_obj):
  list_len = len(list_obj)
  for i in range(list_len):
    for j in range(list_len - i -1):
      if list_obj[j] > list_obj[j+1]:
        list_obj[j], list_obj[j+1] = list_obj[j+1], list_obj[j]
    
  return list_obj

sorted_list = bubble_sort(unsorted_list)
print("排列後："+str(sorted_list))