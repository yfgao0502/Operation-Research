def cal_fit(obj):		#caculate the fit function result
	fit = []
	temp = 0.0
	Cmin = 0
	for i in range(len(obj)):
		if(obj[i] == 'None'):
			temp = 0.0
		elif(float(obj[i]) > 0.0):
			temp = obj[i]
		else:
			temp = 0.0
		fit.append(temp)
	return fit