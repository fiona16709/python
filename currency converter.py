import tkinter as tk

window = tk.Tk()

window.title('Currency Converter (TWD <-> USD)')
# window.geometry('800x600')
window.configure(background = 'white')

''' convert function '''
usd_exchangeRate = 0.33 # 1 twd = 0.33 usd
twd_exchangeRte = 30.41 # 1 usd = 30.41 twd
def convert_to_TWD():
    usd = float(usd_input.get())
    result_value_tw = usd * twd_exchangeRte # USD -> TWD
    result_text_tw.configure(text = 'TWD: ' + str(result_value_tw))

def convert_to_USD():
    twd = float(twd_input.get())
    result_value_us = twd * usd_exchangeRate # TWD -> USD
    result_text_us.configure(text = 'USD: ' + str(result_value_us))

''' header '''
header_label = tk.Label(window, text = 'Currency Converter (TWD <-> USD)')
header_label.pack()

''' TWD area '''
twd_frame = tk.Frame(window)
twd_frame.pack()

twd_label = tk.Label(twd_frame, text = 'TWD:')
twd_label.pack(side = tk.LEFT)

twd_input = tk.Entry(twd_frame)
twd_input.pack(side = tk.LEFT)

''' USD area '''
usd_frame = tk.Frame(window)
usd_frame.pack()

usd_label = tk.Label(usd_frame, text = 'USD:')
usd_label.pack(side = tk.LEFT)

usd_input = tk.Entry(usd_frame)
usd_input.pack(side = tk.LEFT)

''' convert button '''
# USD -> TWD
convert_twd_btn = tk.Button(usd_frame, text = 'Convert to TWD', command = convert_to_TWD)
convert_twd_btn.pack(side = tk.LEFT)

# TWD -> USD
convert_usd_btn = tk.Button(twd_frame, text = 'Convert to USD', command = convert_to_USD)
convert_usd_btn.pack(side = tk.LEFT)

''' result area (USD -> TWD) '''
result_label_tw= tk.Label(window, text = 'Result (USD -> TWD):')
result_label_tw.pack()

result_text_tw = tk.Label(window)
result_text_tw.pack()

''' result area (TWD -> USD) '''
result_label_us= tk.Label(window, text = 'Result (TWD -> USD):')
result_label_us.pack()

result_text_us = tk.Label(window)
result_text_us.pack()



window.mainloop()