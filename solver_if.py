import numpy as np


def system_if(pe, fe, rne, a1e, a2e, b1e, b2e):

	X = []

	if pe == '':
		X.append(1)
	else:
		pe = float(pe)

	if fe == '':
		X.append(2)
	else:
		fe = float(fe)

	if rne == '':
		X.append(3)
	else:
		rne = float(rne)

	if a1e == '':
		X.append(4)
	else:
		a1e = float(a1e)
		a1 = np.radians(a1e)

	if a2e == '':
		X.append(5)
	else:
		a2e = float(a2e)
		a2 = np.radians(a2e)

	if b1e == '':
		X.append(6)
	else:
		b1e = float(b1e)
		b1 = np.radians(b1e)

	if b2e == '':
		X.append(7)
	else:
		b2e = float(b2e)
		b2 = np.radians(b2e)

	k = len(X)
	t = len(X)

	# ############################## ψ,φ,Rn ######################################

	if X == [4, 5, 6, 7]:  # p,f,r
		a1e = np.degrees(np.arctan(((pe / 2) - 1 + rne) / fe))
		a2e = np.degrees(np.arctan(((pe / 2) + 1 - rne) / fe))
		b1e = np.degrees(np.arctan(((pe / 2) + rne) / fe))
		b2e = np.degrees(np.arctan(((pe / 2) - rne) / fe))

	# ############################## μόνο γωνίες ######################################

	if X == [1, 2, 3, 7]:  # a1,a2,b1
		pe = (np.tan(a1) + np.tan(a2)) / (np.tan(b1) - np.tan(a1))
		fe = 1 / (np.tan(b1) - np.tan(a1))
		rne = (-np.tan(a1) - np.tan(a2) + 2 * np.tan(b1)) / (2 * (np.tan(b1) - np.tan(a1)))
		b2e = np.degrees(np.arctan(np.tan(a1) + np.tan(a2) - np.tan(b1)))

	if X == [1, 2, 3, 6]:  # a1,a2,b2
		pe = (np.tan(a1) + np.tan(a2)) / (np.tan(a2) - np.tan(b2))
		fe = 1 / (np.tan(a2) - np.tan(b2))
		rne = (-np.tan(a1) - np.tan(a2) + 2 * np.tan(b2)) / (2 * (np.tan(b2) - np.tan(a2)))
		b1e = np.degrees(np.arctan(np.tan(a1) + np.tan(a2) - np.tan(b2)))

	if X == [1, 2, 3, 5]:  # a1,b1,b2
		pe = (np.tan(b1) + np.tan(b2)) / (np.tan(b1) - np.tan(a1))
		fe = 1 / (np.tan(b1) - np.tan(a1))
		rne = (np.tan(b1) - np.tan(b2)) / (2 * (np.tan(b1) - np.tan(a1)))
		a2e = -np.degrees(np.arctan(np.tan(a1) - np.tan(b1) - np.tan(b2)))

	if X == [1, 2, 3, 4]:  # a2,b1,b2
		pe = (np.tan(b1) + np.tan(b2)) / (np.tan(a2) - np.tan(b2))
		fe = 1 / (np.tan(a2) - np.tan(b2))
		rne = (np.tan(b2) - np.tan(b1)) / (2 * (np.tan(b2) - np.tan(a2)))
		a1e = -np.degrees(np.arctan(np.tan(a2) - np.tan(b1) - np.tan(b2)))

	# ############################## ψ,φ,γωνίες ######################################

	if X == [3, 5, 6, 7]:  # p,f,a1
		rne = fe * np.tan(a1) - pe / 2 + 1
		a2e = np.degrees(np.arctan(((pe / 2) + 1 - rne) / fe))
		b1e = np.degrees(np.arctan(((pe / 2) + rne) / fe))
		b2e = np.degrees(np.arctan(((pe / 2) - rne) / fe))

	if X == [3, 4, 6, 7]:  # p,f,a2
		rne = -fe * np.tan(a2) + pe / 2 + 1
		a1e = np.degrees(np.arctan(((pe / 2) - 1 + rne) / fe))
		b1e = np.degrees(np.arctan(((pe / 2) + rne) / fe))
		b2e = np.degrees(np.arctan(((pe / 2) - rne) / fe))

	if X == [3, 4, 5, 7]:  # p,f,b1
		rne = fe * np.tan(b1) - pe / 2
		a1e = np.degrees(np.arctan(((pe / 2) - 1 + rne) / fe))
		a2e = np.degrees(np.arctan(((pe / 2) + 1 - rne) / fe))
		b2e = np.degrees(np.arctan(((pe / 2) - rne) / fe))

	if X == [3, 4, 5, 6]:  # p,f,b2
		rne = -fe * np.tan(b2) + pe / 2
		a1e = np.degrees(np.arctan(((pe / 2) - 1 + rne) / fe))
		a2e = np.degrees(np.arctan(((pe / 2) + 1 - rne) / fe))
		b1e = np.degrees(np.arctan(((pe / 2) + rne) / fe))

	# ############################## φ,Rn,γωνίες ######################################

	if X == [1, 5, 6, 7]:  # f,r,a1
		pe = 2 * (fe * np.tan(a1) + 1 - rne)
		a2e = np.degrees(np.arctan(((pe / 2) + 1 - rne) / fe))
		b1e = np.degrees(np.arctan(((pe / 2) + rne) / fe))
		b2e = np.degrees(np.arctan(((pe / 2) - rne) / fe))

	if X == [1, 4, 6, 7]:  # f,r,a2
		pe = 2 * (fe * np.tan(a2) - 1 + rne)
		a1e = np.degrees(np.arctan(((pe / 2) - 1 + rne) / fe))
		b1e = np.degrees(np.arctan(((pe / 2) + rne) / fe))
		b2e = np.degrees(np.arctan(((pe / 2) - rne) / fe))

	if X == [1, 4, 5, 7]:  # f,r,b1
		pe = 2 * (fe * np.tan(b1) - rne)
		a1e = np.degrees(np.arctan(((pe / 2) - 1 + rne) / fe))
		a2e = np.degrees(np.arctan(((pe / 2) + 1 - rne) / fe))
		b2e = np.degrees(np.arctan(((pe / 2) - rne) / fe))

	if X == [1, 4, 5, 6]:  # f,r,b2
		pe = 2 * (fe * np.tan(b2) + rne)
		a1e = np.degrees(np.arctan(((pe / 2) - 1 + rne) / fe))
		a2e = np.degrees(np.arctan(((pe / 2) + 1 - rne) / fe))
		b1e = np.degrees(np.arctan(((pe / 2) + rne) / fe))

	# ############################## ψ,Rn,γωνίες ######################################

	if X == [2, 5, 6, 7]:  # p,r,a1
		fe = (pe / 2 - 1 + rne) / np.tan(a1)
		a2e = np.degrees(np.arctan(((pe / 2) + 1 - rne) / fe))
		b1e = np.degrees(np.arctan(((pe / 2) + rne) / fe))
		b2e = np.degrees(np.arctan(((pe / 2) - rne) / fe))

	if X == [2, 4, 6, 7]:  # p,r,a2
		fe = (pe / 2 + 1 - rne) / np.tan(a2)
		a1e = np.degrees(np.arctan(((pe / 2) - 1 + rne) / fe))
		b1e = np.degrees(np.arctan(((pe / 2) + rne) / fe))
		b2e = np.degrees(np.arctan(((pe / 2) - rne) / fe))

	if X == [2, 4, 5, 7]:  # p,r,b1
		fe = (pe / 2 + rne) / np.tan(b1)
		a1e = np.degrees(np.arctan(((pe / 2) - 1 + rne) / fe))
		a2e = np.degrees(np.arctan(((pe / 2) + 1 - rne) / fe))
		b2e = np.degrees(np.arctan(((pe / 2) - rne) / fe))

	if X == [2, 4, 5, 6]:  # p,r,b2
		fe = (pe / 2 - rne) / np.tan(b2)
		a1e = np.degrees(np.arctan(((pe / 2) - 1 + rne) / fe))
		a2e = np.degrees(np.arctan(((pe / 2) + 1 - rne) / fe))
		b1e = np.degrees(np.arctan(((pe / 2) + rne) / fe))

	# ############################## ψ,2 γωνίες ######################################

		# a1e = np.degrees(np.arctan(((pe / 2) - 1 + rne) / fe))
		# a2e = np.degrees(np.arctan(((pe / 2) + 1 - rne) / fe))
		# b1e = np.degrees(np.arctan(((pe / 2) + rne) / fe))
		# b2e = np.degrees(np.arctan(((pe / 2) - rne) / fe))

	if X == [2, 3, 6, 7]:  # p,a1,a2
		rne = (pe * np.tan(a1) + 2 * np.tan(a1) - pe * np.tan(a2) + 2 * np.tan(a2)) / (2 * (np.tan(a1) + np.tan(a2)))
		fe = pe / (np.tan(a1) + np.tan(a2))
		b1e = np.degrees(np.arctan(((pe / 2) + rne) / fe))
		b2e = np.degrees(np.arctan(((pe / 2) - rne) / fe))

	if X == [2, 3, 5, 7]:  # p,a1,b1
		rne = (pe * np.tan(a1) - pe * np.tan(b1) + 2 * np.tan(b1)) / (2 * (np.tan(b1) - np.tan(a1)))
		fe = 1 / (np.tan(b1) - np.tan(a1))
		a2e = np.degrees(np.arctan(((pe / 2) + 1 - rne) / fe))
		b2e = np.degrees(np.arctan(((pe / 2) - rne) / fe))

	if X == [2, 3, 5, 6]:  # p,a1,b2
		rne = (pe * np.tan(a1) - pe * np.tan(b2) + 2 * np.tan(b2)) / (2 * (np.tan(a1) + np.tan(b2)))
		fe = (pe - 1) / (np.tan(a1) + np.tan(b2))
		a2e = np.degrees(np.arctan(((pe / 2) + 1 - rne) / fe))
		b1e = np.degrees(np.arctan(((pe / 2) + rne) / fe))

	if X == [2, 3, 4, 7]:  # p,a2,b1
		rne = (-pe * np.tan(a2) + pe * np.tan(b1) + 2 * np.tan(b1)) / (2 * (np.tan(a2) + np.tan(b1)))
		fe = (pe + 1) / (np.tan(a2) + np.tan(b1))
		a1e = np.degrees(np.arctan(((pe / 2) - 1 + rne) / fe))
		b2e = np.degrees(np.arctan(((pe / 2) - rne) / fe))

	if X == [2, 3, 4, 6]:  # p,a2,b2
		fe = 1 / (np.tan(a2) - np.tan(b2))
		rne = (-pe * np.tan(a2) + pe * np.tan(b2) + 2 * np.tan(b2)) / (2 * (np.tan(b2) - np.tan(a2)))
		a1e = np.degrees(np.arctan(((pe / 2) - 1 + rne) / fe))
		b1e = np.degrees(np.arctan(((pe / 2) + rne) / fe))

	if X == [2, 3, 4, 5]:  # p,b1,b2
		fe = pe / (np.tan(b1) + np.tan(b2))
		rne = (-pe / 2) * ((np.tan(b2) - np.tan(b1)) / (np.tan(b1) + np.tan(b2)))
		a1e = np.degrees(np.arctan(((pe / 2) - 1 + rne) / fe))
		a2e = np.degrees(np.arctan(((pe / 2) + 1 - rne) / fe))

	# ############################## φ,2 γωνίες ######################################

	if X == [1, 3, 6, 7]:  # f,a1,a2
		pe = fe * (np.tan(a1) + np.tan(a2))
		rne = (1 / 2) * (fe * np.tan(a1) - fe * np.tan(a2) + 2)
		b1e = np.degrees(np.arctan(((pe / 2) + rne) / fe))
		b2e = np.degrees(np.arctan(((pe / 2) - rne) / fe))

	if X == [1, 3, 5, 7]:  # f,a1,b1
		pe = 1
		rne = (1 / 2) * (2 * fe * np.tan(a1) - pe - 1)
		a2e = np.degrees(np.arctan(((pe / 2) + 1 - rne) / fe))
		b2e = np.degrees(np.arctan(((pe / 2) - rne) / fe))

	if X == [1, 3, 5, 6]:  # f,a1,b2
		pe = fe * (np.tan(a1) + np.tan(b2)) + 1
		rne = (1 / 2) * (fe * np.tan(a1) - fe * np.tan(b2) + 1)
		a2e = np.degrees(np.arctan(((pe / 2) + 1 - rne) / fe))
		b1e = np.degrees(np.arctan(((pe / 2) + rne) / fe))

	if X == [1, 3, 4, 7]:  # f,a2,b1
		pe = fe * (np.tan(a2) + np.tan(b1)) - 1
		rne = (1 / 2) * (-fe * np.tan(a2) + fe * np.tan(b1) + 1)
		a1e = np.degrees(np.arctan(((pe / 2) - 1 + rne) / fe))
		b2e = np.degrees(np.arctan(((pe / 2) - rne) / fe))

	if X == [1, 3, 4, 6]:  # f,a2,b2
		pe = 1
		rne = (1 / 2) * (-2 * fe * np.tan(a2) + pe + 2)
		a1e = np.degrees(np.arctan(((pe / 2) - 1 + rne) / fe))
		b1e = np.degrees(np.arctan(((pe / 2) + rne) / fe))

	if X == [1, 3, 4, 5]:  # f,b1,b2
		pe = fe * (np.tan(b1) + np.tan(b2))
		rne = (1 / 2) * fe * (np.tan(b1) - np.tan(b2))
		a1e = np.degrees(np.arctan(((pe / 2) - 1 + rne) / fe))
		a2e = np.degrees(np.arctan(((pe / 2) + 1 - rne) / fe))

	# ############################## Rn,2 γωνίες ######################################

	# if  X == [1,2,6,7]:               #r,a1,a2

	if X == [1, 2, 5, 7]:  # r,a1,b1
		pe = (2 * (rne * np.tan(a1) - rne * np.tan(b1) + np.tan(b1))) / (np.tan(b1) - np.tan(a1))
		fe = 1 / (np.tan(b1) - np.tan(a1))
		a2e = np.degrees(np.arctan(((pe / 2) + 1 - rne) / fe))
		b2e = np.degrees(np.arctan(((pe / 2) - rne) / fe))

	# if  X == [1,2,5,6]:               #r,a1,b2

	# if  X == [1,2,4,7]:               #r,a2,b1

	if X == [1, 2, 4, 6]:  # r,a2,b2
		pe = (2 * (-rne * np.tan(a2) + rne * np.tan(b2) - np.tan(b2))) / (np.tan(b2) - np.tan(a2))
		fe = 1 / (np.tan(a2) - np.tan(b2))
		a1e = -np.degrees(np.arctan(-2 * rne * np.tan(a2) + np.tan(a2) + 2 * rne * np.tan(b2) - 2 * np.tan(b2)))
		b1e = np.degrees(np.arctan(2 * rne * np.tan(a2) - 2 * rne * np.tan(b2) + np.tan(b2)))

	if X == [1, 2, 4, 5]:  # r,b1,b2
		if rne == 0 and b1e == b2e:
			pe = 1
			fe = (pe / 2 + rne) / np.tan(b1)
			a1e = np.degrees(np.arctan(((pe / 2) - 1 + rne) / fe))
			a2e = np.degrees(np.arctan(((pe / 2) + 1 - rne) / fe))
		else:
			pe = (-2) * (rne * np.tan(b1) + rne * np.tan(b2)) / (np.tan(b2) - np.tan(b1))
			fe = -(2 * rne) / (np.tan(b2) - np.tan(b1))
			a1e = np.degrees(np.arctan(((pe / 2) - 1 + rne) / fe))
			a2e = np.degrees(np.arctan(((pe / 2) + 1 - rne) / fe))

	pe = str(round(float(pe), 3))
	fe = str(round(float(fe), 3))
	rne = str(round(float(rne), 3))
	a1e = str(round(float(a1e), 3))
	a2e = str(round(float(a2e), 3))
	# a3e = str(round(float(a3e), 3))
	b1e = str(round(float(b1e), 3))
	b2e = str(round(float(b2e), 3))
	# b3e = str(round(float(b3e), 3))

	return pe, fe, rne, a1e, a2e, b1e, b2e, k, t
