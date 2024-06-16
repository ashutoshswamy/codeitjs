import matplotlib.pyplot as plt

months = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
temperatures = [23, 14, 34, 35, 56, 34, 27, 12, 21, 32, 17, 11]

plt.figure(figsize = (10, 6))
plt.plot(months, temperatures, marker = "o", linestyle = "-", label = "Monthly Temperature")

plt.title("Average Monthly Temperatures")
plt.xlabel("Month")
plt.ylabel("Temperature")
plt.legend()
plt.grid()

plt.show()
