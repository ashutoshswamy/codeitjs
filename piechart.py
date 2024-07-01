import matplotlib.pyplot as plt

data = [30, 40, 20, 10]
labels = ['Pizza', 'Pasta', 'Salad', 'Drinks'] 
colors = ['lightcoral', 'gold', 'lightgreen', 'lightskyblue']

plt.pie(data, labels=labels, colors=colors, autopct="%1.1f%%", shadow=True) 
plt.title('Pie Chart') 

plt.axis('equal') 

plt.show()
