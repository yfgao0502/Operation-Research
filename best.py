#find the best one in a population
def best(pop, fit):  		
	bestone = []
	bestfit = fit[0]
	for i in range(1, len(pop)):
		if(fit[i] > bestfit):
			bestfit = fit[i]
			bestone = pop[i]
	return [bestone, bestfit]