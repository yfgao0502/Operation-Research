import random

#the function that after setting a crossover point randomly (mpoint), the gene on this point will be changed
def mutation(pop, pm):
	px = len(pop)
	py = len(pop[0])

	for i in range(px):
		if(random.random() < pm):
			mpoint = random.randint(0, py-1)
			if(pop[i][mpoint] == 1):
				pop[i][mpoint] = 0
			else:
				pop[i][mpoint] = 1