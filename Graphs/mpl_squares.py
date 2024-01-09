import matplotlib.pyplot as plt
input_values = [1,2,3,4,5,6,7]
squares = [1,4,9,16,25,36,49]
plt.plot(input_values,squares, linewidth = 4)
plt.title("Square Numbers",fontsize=25)
plt.xlabel("Input",fontsize=15)
plt.ylabel("Square of input",fontsize=15)
# setting the size of tick labels.
plt.tick_params(axis='both',labelsize=13)
plt.show()