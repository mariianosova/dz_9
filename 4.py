import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('data.txt', delimiter=',', dtype=str) 

#Какова общая сумма продаж для всех продуктов?
sales = data[:, 1].astype(int)  #преобразование второго столбца в целочисленный тип данных
total_sales = np.sum(sales)

print("Общая сумма продаж для всех продуктов:", total_sales)

#Сколько уникальных регионов продаж существует?
regions = data[:, 2]
unique_regions = np.unique(regions)
num_unique_regions = unique_regions.size

print("Количество уникальных регионов продаж:", num_unique_regions)

#Какова средняя сумма продаж на продукт?
num_products = sales.size
average_sales_per_product = np.mean(sales)

print("Средняя сумма продаж на продукт:", average_sales_per_product)

#Какой продукт имеет наибольшую сумму продаж?
max_sales = np.argmax(sales)
product_id = data[max_sales, 0]

print("Продукт с наибольшей суммой продаж имеет id:", product_id)

#Рассчитайте сумму продаж для каждого региона продаж. (постройте круговую гистограмму)
region_sales = {}
for i in range(len(regions)):
    region = regions[i]
    sale = sales[i]
    if region in region_sales:
        region_sales[region] += sale
    else:
        region_sales[region] = sale

# Круговая диаграмма с суммой продаж для каждого региона
labels = region_sales.keys()
values = region_sales.values()

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Сумма продаж по регионам')
plt.show()

#Топ 5 продуктов по продажам и построить круговую гистограмму, где будет 6 секторов: топ 5 и все остальное
top_indixes = np.argsort(sales)[-5:]  # Индексы топ 5 продуктов

top_products = data[top_indixes]
other_sales = np.sum(sales) - np.sum(sales[top_indixes])  # Сумма продаж остальных продуктов

# Создание массива для круговой гистограммы
labels = np.append(top_products[:, 0], 'Other')
values = np.append(top_products[:, 1].astype(float), other_sales)

# Круговая диаграмма с топ 5 и остальными продуктами
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.axis('equal')
plt.title('Продажи по топ 5 продуктам')
plt.show()