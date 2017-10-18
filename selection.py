import random

def sum(fit):
	total = 0
	for i in range(len(fit)):
		total += fit[i]
	return total

def cumsum(fit):
	for i in range(len(fit)):
		t = 0
		j = 0
		while(j <= i):
			t += fit[j]
			j = j+1
		fit[i] = t

#the function that guarantee the individual gene segment which has the best fitness can evolve to the next generation
def selection(pop, fit):
	newfit = []
	totalfit = sum(fit)

	for i in range(len(fit)):
		newfit.append(fit[i] / totalfit)
	cumsum(newfit)
	ms = []
	poplen = len(pop)
	for i in range(poplen):
		ms.append(random.random())
	ms.sort()
	fitin = 0
	newin = 0
	newpop = pop
	while newin < poplen:
		if(ms[newin] < newfit[fitin]):
			newpop[newin] = pop[fitin]
			newin = newin + 1
		else:
			fitin = fitin + 1
	pop = newpop
