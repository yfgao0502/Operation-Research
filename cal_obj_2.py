import math
from pulp import *

def linear_function(pop):		#linear programming part, which also calculate the object function
	temp = []
	for i in range(len(pop)):
		t = 0
		earn = 100
		#costs are the transportation costs of each route
		costs = \
		[25.6, 23, 30, 18.6, 27.3, 28.5, 30.1,20.9, 31.2, 39.7, 23.6, 34.9, 39.1, 34, 20.2, 26.5, 18.1, 22, 18.4, 29.6, 11, 35.8, 17.1, 36.7, 36.6, 19.4, 15, 29, 20.2, 31.9, 11, 48.4, 35.8, 29.7, 36.5, 35.7, 30.4, 30, 39.1,\
		0, 10, 15.9, 10, 10, 16.6, 11, 23.5, 12.4, 15.1, 10, 13, 18.4, 21.5, 20.3, 10, 22.4, 20.7, 24.6, 10, 28.5, 38.3, 36.1, 38.8, 28.7, 31.5, 35.2, 10, 25.5, 14.4, 27.8, 40.7, 25.6, 24.7, 25.6, 12.4, 12.5, 10, 19.4,\
		18.8, 12.1, 24.3, 12.6, 22.9, 26.2, 18.1, 30.6, 20.9, 22.3, 10, 18.3, 25.5, 29.3, 23.2, 14.4, 25.8, 24.5, 27, 16.4, 20.2, 39.1, 27.3, 39.6, 35.2, 28.3, 26.5, 14.7, 27.8, 28.4, 13, 31.9, 15.1, 10, 12.7, 20.5, 11.3, 13.7, 21.9,\
		17.4, 18.6, 10, 17.5, 15, 10, 12.1, 10, 10.7, 10.8, 20.7, 14.9, 10, 10, 15.7, 16.1, 14.4, 16.9, 11.4, 13.3, 18.6, 17.3, 21.8, 18.1, 10, 15.8, 21.6, 17.7, 12.1, 25.3, 20.6, 49, 38.7, 34.6, 37, 10.7, 23.1, 16.6, 16.7,\
		12.2, 13.1, 10, 12, 10, 10, 10, 10.5, 10, 10, 14.1, 10, 10, 10, 13.4, 10.8, 12.8, 13.9, 11.7, 10, 17.5, 20.9, 22.9, 21.9, 12.2, 18.2, 22.7, 11.4, 12.5, 19.5, 21.4, 44.9, 32.5, 28.4, 32.4, 10, 17.9, 11.6, 13.1,\
		32.8, 33.5, 26.9, 32.8, 30.2, 25, 27.3, 20.8, 25.6, 29.9, 38.9, 29.7, 24.8, 21.8, 25.6, 31.3, 25.1, 27.3, 22.6, 31.2, 24.6, 10, 24.1, 10, 14.5, 23.6, 24.5, 33.9, 22.1, 34.3, 26.3, 63.5, 47, 42.8, 45, 25.6, 38.5, 31.4, 32.6,\
		10, 31.5, 31.8, 27.8]
		#staffamount is the amount of drivers in each route
		staffamount = ['y11', 'y12', 'y13', 'y14', 'y15', 'y16', 'y17', 'y18', 'y19', 'y110', 'y111', 'y112', 'y113',\
		'y114', 'y115', 'y116', 'y117', 'y118', 'y119', 'y120', 'y121', 'y122', 'y123', 'y124', 'y125', 'y126',\
		'y127', 'y128', 'y129', 'y130', 'y131', 'y132', 'y133', 'y134', 'y135', 'y136', 'y137', 'y138', 'y139',\
		'y21', 'y22', 'y23', 'y24', 'y25', 'y26', 'y27', 'y28', 'y29', 'y210', 'y211', 'y212', 'y213',\
		'y214', 'y215', 'y216', 'y217', 'y218', 'y219', 'y220', 'y221', 'y222', 'y223', 'y224', 'y225', 'y226',\
		'y227', 'y228', 'y229', 'y230', 'y231', 'y232', 'y233', 'y234', 'y235', 'y236', 'y237', 'y238', 'y239',\
		'y31', 'y32', 'y33', 'y34', 'y35', 'y36', 'y37', 'y38', 'y39', 'y310', 'y311', 'y312', 'y313',\
		'y314', 'y315', 'y316', 'y317', 'y318', 'y319', 'y320', 'y321', 'y322', 'y323', 'y324', 'y325', 'y326',\
		'y327', 'y328', 'y329', 'y330', 'y331', 'y332', 'y333', 'y334', 'y335', 'y336', 'y337', 'y338', 'y339',\
		'y41', 'y42', 'y43', 'y44', 'y45', 'y46', 'y47', 'y48', 'y49', 'y410', 'y411', 'y412', 'y413',\
		'y414', 'y415', 'y416', 'y417', 'y418', 'y419', 'y420', 'y421', 'y422', 'y423', 'y424', 'y425', 'y426',\
		'y427', 'y428', 'y429', 'y430', 'y431', 'y432', 'y433', 'y434', 'y435', 'y436', 'y437', 'y438', 'y439',\
		'y51', 'y52', 'y53', 'y54', 'y55', 'y56', 'y57', 'y58', 'y59', 'y510', 'y511', 'y512', 'y513',\
		'y514', 'y515', 'y516', 'y517', 'y518', 'y519', 'y520', 'y521', 'y522', 'y523', 'y524', 'y525', 'y526',\
		'y527', 'y528', 'y529', 'y530', 'y531', 'y532', 'y533', 'y534', 'y535', 'y536', 'y537', 'y538', 'y539',\
		'y61', 'y62', 'y63', 'y64', 'y65', 'y66', 'y67', 'y68', 'y69', 'y610', 'y611', 'y612', 'y613',\
		'y614', 'y615', 'y616', 'y617', 'y618', 'y619', 'y620', 'y621', 'y622', 'y623', 'y624', 'y625', 'y626',\
		'y627', 'y628', 'y629', 'y630', 'y631', 'y632', 'y633', 'y634', 'y635', 'y636', 'y637', 'y638', 'y639',\
		'y71', 'y72', 'y73', 'y74', 'y75', 'y76', 'y77', 'y78', 'y79', 'y710', 'y711', 'y712', 'y713',\
		'y714', 'y715', 'y716', 'y717', 'y718', 'y719', 'y720', 'y721', 'y722', 'y723', 'y724', 'y725', 'y726',\
		'y727', 'y728', 'y729', 'y730', 'y731', 'y732', 'y733', 'y734', 'y735', 'y736', 'y737', 'y738', 'y739']
		if(len(pop[i]) == 0):
			z1 = z2 = z3 = z4 = z5 = z6 = z7 = 0
		else:
			z1 = pop[i][0]
			z2 = pop[i][1]
			z3 = pop[i][2]
			z4 = pop[i][3]
			z5 = pop[i][4]
			z6 = pop[i][5]
			z7 = pop[i][6]
		temppop = [z1, z2, z3, z4, z5, z6, z7]
		Z = [z1]*39 + [z2]*39 + [z3]*39 + [z4]*39 + [z5]*39 +[z6]*39 +[z7]*4

		#the calculation of object function if Designated driver problem starts from here
		prob = LpProblem("Designated driver problem", LpMaximize)			

		staffamount_vars = []
		for k in range(len(staffamount)):
			staffamount_vars.append(LpVariable(staffamount[k], 0, cat = 'Integer'))

		#the object is to maximize the profit, that is the reward minus costs
		prob += lpSum([Z[j]*(100-costs[j])*staffamount_vars[j] for j in range(len(Z))])
		#equality constraints
		for a in range(39):		
			prob += lpSum([temppop[j]*staffamount_vars[39*j+a] for j in range(7)]) == 5
		#inequality constraints
		prob += lpSum([Z[j]*staffamount_vars[j] for j in range(0,39)]) <=40
		prob += lpSum([Z[j]*staffamount_vars[j] for j in range(39,39*2)]) <=40
		prob += lpSum([Z[j]*staffamount_vars[j] for j in range(39*2,39*3)]) <=40
		prob += lpSum([Z[j]*staffamount_vars[j] for j in range(39*3,39*4)]) <=40
		prob += lpSum([Z[j]*staffamount_vars[j] for j in range(39*4,39*5)]) <=40
		prob += lpSum([Z[j]*staffamount_vars[j] for j in range(39*5,39*6)]) <=40
		prob += lpSum([Z[j]*staffamount_vars[j] for j in range(39*6,len(Z))]) <=40

		prob.solve()
		temp.append(value(prob.objective))

	if(len(temp) == 1): #this is to get the variable value of a result with one gene segment
		for v in prob.variables():
			print(v.name, '=', v.varValue)

	return temp

def cal_obj(pop):
	return linear_function(pop)
	