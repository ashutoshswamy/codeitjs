import matplotlib.pyplot as plt

categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [23, 17, 35, 29]

plt.figure(figsize = (10, 6))
plt.bar(categories, values, color='skyblue', width=0.4)

plt.title('Sample Bar Graph')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.grid()

plt.show()
