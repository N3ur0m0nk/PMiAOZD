import time
import cvxopt.modeling

start = time.time()
x = cvxopt.modeling.variable(2, 'x')
z = -(30 * x[0] + 1 * x[1])
mass1 = (90 * x[0] + 5 * x[1] <= 10000)
mass2 = (3 * x[0] - x[1] == 0)
x_non_negative = (x >= 0)
problem = cvxopt.modeling.op(z, [mass1, mass2, x_non_negative])
problem.solve(solver='glpk')
print("Прибыль:")
print(abs(problem.objective.value()[0]))
print("Результат:")
print(x.value)
stop = time.time()
print("Время :")
print(stop - start)
