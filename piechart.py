import matplotlib.pyplot as plt

data = [30, 40, 20, 10]
labels = ['Pizza', 'Pasta', 'Salad', 'Drinks']  # Change these labels to match your data
colors = ['lightcoral', 'gold', 'lightgreen', 'lightskyblue']  # You can customize colors

plt.pie(data, labels=labels, colors=colors, autopct="%1.1f%%", shadow=True) 
plt.title('Pie Chart')  # Add a title (optional)

plt.axis('equal') 

plt.show()
