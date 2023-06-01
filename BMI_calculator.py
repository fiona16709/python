import tkinter as tk
import math

# 設定視窗標題、大小和背景顏色
window = tk.Tk()
window.title('BMI APP')
window.geometry('800x600')
window.configure(background = 'white')

''' function --- calculate_bmi_number '''
def calculate_bmi_number():
    height = float(height_input.get())*0.01
    weight = float(weight_input.get())
    bmi_value = round(weight / math.pow(height, 2),2)
    result = '你的 BMI 指數為：{} {}'.format(bmi_value, get_bmi_status_description(bmi_value))
    result_label.configure(text = result)
     # 清除輸入框內容（從 index 0 到結束）
    height_input.delete(0, 'end')
    weight_input.delete(0, 'end')

''' function --- get_bmi_status_description '''
def get_bmi_status_description(bmi_value):
    if bmi_value < 18.5:
        return '體重過輕囉，多吃點！'
    elif 18.5 <= bmi_value and bmi_value < 24:
        return '體重剛剛好，繼續保持！'
    elif bmi_value >= 24:
        return '體重有點過重囉，少吃多運動！'
    else:
        return '請再試一次！'

header_label = tk.Label(window, text = 'BMI 計算器')
header_label.pack()

''' 以下為 height_frame 群組 '''
height_frame = tk.Frame(window)
# 向上對齊父元件
height_frame.pack(side = tk.TOP)

height_label = tk.Label(height_frame, text = '身高 (cm)')
height_label.pack(side = tk.LEFT)

height_input = tk.Entry(height_frame)
height_input.pack(side = tk.LEFT)

''' 以下為 weight_frame 群組 '''
weight_frame = tk.Frame(window)
weight_frame.pack(side = tk.TOP)
weight_label = tk.Label(weight_frame, text = '體重 (kg)')
weight_label.pack(side = tk.LEFT)
weight_input = tk.Entry(weight_frame)
weight_input.pack(side = tk.LEFT)


''' result label '''
result_label = tk.Label(window)
result_label.pack()


''' button '''
calculate_btn  = tk.Button(window, text = '開始計算', command = calculate_bmi_number)
calculate_btn.pack()


# 運行主程式
window.mainloop()