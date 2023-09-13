from scipy.optimize import linprog
import time
import matplotlib.pyplot as plt

start = time.time()
c = [-30, -1]
A_ub = [[90, 5]]
b_ub = [10000]
A_eq = [[3, -1]]
b_eq = [0]
print(linprog(c, A_ub, b_ub, A_eq, b_eq))
stop = time.time()
print("Время :")
print(stop - start)

plt.title('ПЗ 2')
plt.xlabel('Значение X1')
plt.ylabel('Значение X2')
plt.xlim(0, 150)
plt.ylim(0, 300)
plt.axline((0, 2000), slope=-18)
plt.axline((0, 0), slope=3)
plt.fill_between((0, 2000/21, 111.111), (0, 2000/7, 0))
plt.text(4, 25, 'x2=3*x1', rotation=50)
plt.text(97, 180, 'x2<=2000-18*x1', rotation=-80)
plt.grid()
plt.show()