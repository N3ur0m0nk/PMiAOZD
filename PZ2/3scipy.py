from scipy.optimize import linprog
import time

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
