import pulp
import time
import matplotlib.pyplot as plt

start = time.time()
x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
problem = pulp.LpProblem('0', pulp.LpMaximize)
problem += 30 * x1 + x2, "Функция цели"
problem += 90 * x1 + 5 * x2 <= 10000, "1"
problem += x2 == 3 * x1, "2"
problem.solve()
print("Результат:")
for variable in problem.variables():
    print(variable.name, "=", variable.varValue)
print("Прибыль:")
print(pulp.value(problem.objective))
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
