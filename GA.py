import math
import best
import cal_fit
import cal_obj_2
import crossover
import mutation
import selection

def b2d(b):		#b2d() is a function of binary-to-decimal conversion
	t = 0
	for j in range(len(b)):
		t += b[j] * (math.pow(2,j))
	t = t * 7 / 128
	return t

popsize = 50	#population size is 50
genelen = 7		#the length of gene segment is 7, such as [0, 1, 0, 1, 0, 1, 0]
pc = 0.6		#propability of crossover is 0.6
pm = 0.001		#propability of mutation is 0.01
result = [[]]
bestone = []
bestfit = 0     #initialize the best fit function result
fit = []
tempop = [[]]
pop = [[0, 1, 0, 1, 0, 1, 0] for i in range(popsize)]
generation = 100 #the generation of a popolation is the cycle amount of selection/crossover/mutation
for i in range(generation):
	obj = cal_obj_2.cal_obj(pop)			
	fit = cal_fit.cal_fit(obj)
	[bestone, bestfit] = best.best(pop, fit)
	result.append([bestfit, bestone])
	selection.selection(pop, fit)
	crossover.crossover(pop, pc)
	mutation.mutation(pop, pm)

result.sort()
print(result[-1])
resultlist = []
resultlist.append(result[-1][1])
print(cal_obj_2.linear_function(resultlist))