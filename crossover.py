import random

#the function that after setting a crossover point randomly (mpoint), part of the genes of two individuals are exchanged with each other from this point
def crossover(pop, pc):		
	poplen = len(pop)
	for i in range(poplen - 1):
		if(random.random() < pc):
			cpoint = random.randint(0, len(pop[0]))
			temp1 = []
			temp2 = []
			temp1.extend(pop[i][0 : cpoint])				#exchange starts
			temp1.extend(pop[i + 1][cpoint : len(pop[i])])
			temp2.extend(pop[i + 1][0 : cpoint])
			temp2.extend(pop[i][cpoint : len(pop[i])])		#exchange ends
			pop[i] = temp1
			pop[i + 1] = temp2