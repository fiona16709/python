### 問答申論題 ###
'''
import tkinter as tk

window = tk.Tk()

window.title('偶數判斷')

window.geometry('800x600')

window.configure(background = 'white')

input_entry = tk.Entry(window)
input_entry.pack()

result_label = tk.Label(text = '')
result_label.pack()

def send():
  input_value = int(input_entry.get()) # input_entry.get() output -> type: string
  # print(type(input_value))
  if input_value % 2 == 0:
    result_text = '喔喔，是偶數！'
  else:
    result_text = '喔喔，不是偶數！'
    
  result_label.configure(text = result_text)
  
button = tk.Button(window, text = 'Send', command = send)
button.pack()

window.mainloop()
'''

### 程式設計實作題 ###
import tkinter as tk

window = tk.Tk()

window.title('Price calculator')

window.geometry('200x200')

window.configure(background='white')

top_frame = tk.Frame(window)
top_frame.pack()

# left_frame = tk.Frame(window) # for price input
# left_frame.pack(side = tk.LEFT)

price_label = tk.Label(top_frame, text='Price: ')
price_label.pack()

input_price = tk.Entry(top_frame)
input_price.pack()

# right_frame = tk.Frame(window) # for discount input
# right_frame.pack(side = tk.RIGHT)

discount_label = tk.Label(top_frame, text='Discount: (Please insert number.)')
discount_label.pack()

input_discount = tk.Entry(top_frame)
input_discount.pack()

bottom_frame = tk.Frame(window) # for result output
bottom_frame.pack(side = tk.BOTTOM)

result_text = tk.Label(bottom_frame, text = '')
result_text.pack(side = tk.BOTTOM)

result_label = tk.Label(bottom_frame, text = 'Result: ')
result_label.pack(side = tk.BOTTOM)


def submit():
  input_priceValue = float(input_price.get())
  input_discountValue = float(input_discount.get())
  output_price = round(input_priceValue * (0.1 * input_discountValue))
  result_text.configure(text = output_price)

button = tk.Button(window, text = 'Submit', command = submit)
button.pack()

window.mainloop()
