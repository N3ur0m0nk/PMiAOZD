import matplotlib.pyplot as plt

plt.xlim(0,10)
plt.ylim(0,10)
plt.axline((0, 7), slope=-1)
plt.axvline(2)
plt.axline((0, 3), slope=-1)
plt.axline((4, 0), slope=1/2)
plt.fill((0, 0, 2, 2),(3, 7, 5, 1), color='yellow')
plt.axline((0, 3), slope=2, color='red')
plt.grid()
plt.show()