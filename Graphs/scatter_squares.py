import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values, c=y_values,cmap=plt.cm.Blues, edgecolor='none',s=25)
plt.axis([0,1100,0,1100000])
plt.show()

x_values = list(range(1,5001))
y_values = [x**2 * x for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=30)
plt.axis([0,5100,0,135000000000])
plt.show()