import csv
import matplotlib.pyplot as plt

data_dict = {}

with open('taichung_flower.csv', 'r', encoding = 'utf-8') as input_file:
    rows = csv.DictReader(input_file)
    for row in rows:
        category = row['花種']
        if category not in data_dict:
            data_dict[category] = 1
        else:
            data_dict[category] += 1


# print(data_dict)

''' 寫入檔案 - category '''
# 目標：計算台中市花種
with open('taichung_flower_category.csv', 'w') as output_file_cat:
    dict_writer = csv.DictWriter(output_file_cat, data_dict.keys())
    dict_writer.writeheader()
    dict_writer.writerows([data_dict])

with open('taichung_flower_category.csv', 'r') as read_file_Cat:
    read_data_Cat = csv.DictReader(read_file_Cat)
    for cat in read_data_Cat:
        print(cat)

