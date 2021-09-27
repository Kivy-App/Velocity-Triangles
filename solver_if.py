from math import radians,degrees,atan,tan
from all_popups import firstPopup

def system_X(pe,fe,rne,a1e,a2e,b1e,b2e):
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
		a1 = radians(a1e)

	if a2e == '':
		X.append(5)
	else:
		a2e = float(a2e)
		a2 = radians(a2e)

	if b1e == '':
		X.append(6)
	else:
		b1e = float(b1e)
		b1 = radians(b1e)

	if b2e == '':
		X.append(7)
	else:
		b2e = float(b2e)
		b2 = radians(b2e)

	k = len(X)
	t = len(X)

	return X

def system_if(pe,fe,rne,a1e,a2e,b1e,b2e):
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
		a1e = -float(a1e)
		a1 = radians(a1e)

	if a2e == '':
		X.append(5)
	else:
		a2e = float(a2e)
		a2 = radians(a2e)

	if b1e == '':
		X.append(6)
	else:
		b1e = -float(b1e)
		b1 = radians(b1e)

	if b2e == '':
		X.append(7)
	else:
		b2e = float(b2e)
		b2 = radians(b2e)

	k=len(X)
	t=len(X)


	############################### ψ,φ,Rn ######################################

	if X == [4, 5, 6, 7]:  # p,f,r
		a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
		a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
		b1e = degrees(atan(((pe / 2) + rne) / fe))
		b2e = degrees(atan(((pe / 2) - rne) / fe))

	############################### μόνο γωνίες ######################################

	if X == [1, 2, 3, 7]:  # a1,a2,b1
		if a1 == b1:
			a1 =+ 1
		pe = (tan(a1) + tan(a2)) / (tan(b1) - tan(a1))
		fe = 1 / (tan(b1) - tan(a1))
		rne = (-tan(a1) - tan(a2) + 2 * tan(b1)) / (2 * (tan(b1) - tan(a1)))
		b2e = degrees(atan(tan(a1) + tan(a2) - tan(b1)))

	if X == [1, 2, 3, 6]:  # a1,a2,b2
		if a2 == b2:
			a2 =+ 1
		pe = (tan(a1) + tan(a2)) / (tan(a2) - tan(b2))
		fe = 1 / (tan(a2) - tan(b2))
		rne = (-tan(a1) - tan(a2) + 2 * tan(b2)) / (2 * (tan(b2) - tan(a2)))
		b1e = degrees(atan(tan(a1) + tan(a2) - tan(b2)))

	if X == [1, 2, 3, 5]:  # a1,b1,b2
		if a1 == b1:
			a1 =+ 1
		pe = (tan(b1) + tan(b2)) / (tan(b1) - tan(a1))
		fe = 1 / (tan(b1) - tan(a1))
		rne = (tan(b1) - tan(b2)) / (2 * (tan(b1) - tan(a1)))
		a2e = -degrees(atan(tan(a1) - tan(b1) - tan(b2)))

	if X == [1, 2, 3, 4]:  # a2,b1,b2
		if a2 == b2:
			a2 =+ 1
		pe = (tan(b1) + tan(b2)) / (tan(a2) - tan(b2))
		fe = 1 / (tan(a2) - tan(b2))
		rne = (tan(b2) - tan(b1)) / (2 * (tan(b2) - tan(a2)))
		a1e = -degrees(atan(tan(a2) - tan(b1) - tan(b2)))

	############################### ψ,φ,γωνίες ######################################

	if X == [3, 5, 6, 7]:  # p,f,a1
		rne = fe * tan(a1) - pe / 2 + 1
		a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
		b1e = degrees(atan(((pe / 2) + rne) / fe))
		b2e = degrees(atan(((pe / 2) - rne) / fe))

	if X == [3, 4, 6, 7]:  # p,f,a2
		rne = -fe * tan(a2) + pe / 2 + 1
		a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
		b1e = degrees(atan(((pe / 2) + rne) / fe))
		b2e = degrees(atan(((pe / 2) - rne) / fe))

	if X == [3, 4, 5, 7]:  # p,f,b1
		rne = fe * tan(b1) - pe / 2
		a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
		a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
		b2e = degrees(atan(((pe / 2) - rne) / fe))

	if X == [3, 4, 5, 6]:  # p,f,b2
		rne = -fe * tan(b2) + pe / 2
		a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
		a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
		b1e = degrees(atan(((pe / 2) + rne) / fe))

	############################### φ,Rn,γωνίες ######################################

	if X == [1, 5, 6, 7]:  # f,r,a1
		pe = 2 * (fe * tan(a1) + 1 - rne)
		a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
		b1e = degrees(atan(((pe / 2) + rne) / fe))
		b2e = degrees(atan(((pe / 2) - rne) / fe))

	if X == [1, 4, 6, 7]:  # f,r,a2
		pe = 2 * (fe * tan(a2) - 1 + rne)
		a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
		b1e = degrees(atan(((pe / 2) + rne) / fe))
		b2e = degrees(atan(((pe / 2) - rne) / fe))

	if X == [1, 4, 5, 7]:  # f,r,b1
		pe = 2 * (fe * tan(b1) - rne)
		a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
		a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
		b2e = degrees(atan(((pe / 2) - rne) / fe))

	if X == [1, 4, 5, 6]:  # f,r,b2
		pe = 2 * (fe * tan(b2) + rne)
		a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
		a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
		b1e = degrees(atan(((pe / 2) + rne) / fe))

	############################### ψ,Rn,γωνίες ######################################

	if X == [2, 5, 6, 7]:  # p,r,a1
		fe = (pe / 2 - 1 + rne) / tan(a1)
		a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
		b1e = degrees(atan(((pe / 2) + rne) / fe))
		b2e = degrees(atan(((pe / 2) - rne) / fe))

	if X == [2, 4, 6, 7]:  # p,r,a2
		fe = (pe / 2 + 1 - rne) / tan(a2)
		a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
		b1e = degrees(atan(((pe / 2) + rne) / fe))
		b2e = degrees(atan(((pe / 2) - rne) / fe))

	if X == [2, 4, 5, 7]:  # p,r,b1
		fe = (pe / 2 + rne) / tan(b1)
		a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
		a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
		b2e = degrees(atan(((pe / 2) - rne) / fe))

	if X == [2, 4, 5, 6]:  # p,r,b2
		fe = (pe / 2 - rne) / tan(b2)
		a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
		a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
		b1e = degrees(atan(((pe / 2) + rne) / fe))

	############################### ψ,2 γωνίες ######################################

		# a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
		# a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
		# b1e = degrees(atan(((pe / 2) + rne) / fe))
		# b2e = degrees(atan(((pe / 2) - rne) / fe))


	if X == [2, 3, 6, 7]:  # p,a1,a2
		rne = (pe * tan(a1) + 2 * tan(a1) - pe * tan(a2) + 2 * tan(a2)) / (2 * (tan(a1) + tan(a2)))
		fe = pe / (tan(a1) + tan(a2))
		b1e = degrees(atan(((pe / 2) + rne) / fe))
		b2e = degrees(atan(((pe / 2) - rne) / fe))

	if X == [2, 3, 5, 7]:  # p,a1,b1
		if a1 == b1:
			a1 =+ 1
		rne = (pe * tan(a1) - pe * tan(b1) + 2 * tan(b1)) / (2 * (tan(b1) - tan(a1)))
		fe = 1 / (tan(b1) - tan(a1))
		a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
		b2e = degrees(atan(((pe / 2) - rne) / fe))

	if X == [2, 3, 5, 6]:  # p,a1,b2
		rne = (pe * tan(a1) - pe * tan(b2) + 2 * tan(b2)) / (2 * (tan(a1) + tan(b2)))
		fe = (pe - 1) / (tan(a1) + tan(b2))
		a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
		b1e = degrees(atan(((pe / 2) + rne) / fe))

	if X == [2, 3, 4, 7]:  # p,a2,b1
		rne = (-pe * tan(a2) + pe * tan(b1) + 2 * tan(b1)) / (2 * (tan(a2) + tan(b1)))
		fe = (pe + 1) / (tan(a2) + tan(b1))
		a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
		b2e = degrees(atan(((pe / 2) - rne) / fe))

	if X == [2, 3, 4, 6]:  # p,a2,b2
		if a2 == b2:
			a2 =+ 1
		fe = 1 / (tan(a2) - tan(b2))
		rne = (-pe * tan(a2) + pe * tan(b2) + 2 * tan(b2)) / (2 * (tan(b2) - tan(a2)))
		a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
		b1e = degrees(atan(((pe / 2) + rne) / fe))

	if X == [2, 3, 4, 5]:  # p,b1,b2
		fe = pe / (tan(b1) + tan(b2))
		rne = (-pe / 2) * ((tan(b2) - tan(b1)) /  (tan(b1) + tan(b2)))
		a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
		a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))

	############################### φ,2 γωνίες ######################################

	if X == [1, 3, 6, 7]:  # f,a1,a2
		pe = fe * (tan(a1) + tan(a2))
		rne = (1 / 2) * (fe * tan(a1) - fe * tan(a2) + 2)
		b1e = degrees(atan(((pe / 2) + rne) / fe))
		b2e = degrees(atan(((pe / 2) - rne) / fe))

	if X == [1, 3, 5, 6]:  # f,a1,b2
		pe = fe * (tan(a1) + tan(b2)) + 1
		rne = (1 / 2) * (fe * tan(a1) - fe * tan(b2) + 1)
		a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
		b1e = degrees(atan(((pe / 2) + rne) / fe))

	if X == [1, 3, 4, 7]:  # f,a2,b1
		pe = fe * (tan(a2) + tan(b1)) - 1
		rne = (1 / 2) * (-fe * tan(a2) + fe * tan(b1) + 1)
		a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
		b2e = degrees(atan(((pe / 2) - rne) / fe))

	if X == [1, 3, 4, 5]:  # f,b1,b2
		pe = fe * (tan(b1) + tan(b2))
		rne = (1 / 2) * fe * (tan(b1) - tan(b2))
		a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
		a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))

	############################### Rn,2 γωνίες ######################################

	if X == [1, 2, 5, 7]:  # r,a1,b1
		if a1 == b1:
			a1 = + 1
		pe = (2 * (rne * tan(a1) - rne * tan(b1) + tan(b1))) / (tan(b1) - tan(a1))
		fe = 1 / (tan(b1) - tan(a1))
		a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
		b2e = degrees(atan(((pe / 2) - rne) / fe))

	if X == [1, 2, 4, 6]:  # r,a2,b2
		if a2 == b2:
			a2 = + 1
		pe = (2 * (-rne * tan(a2) + rne * tan(b2) - tan(b2))) / (tan(b2) - tan(a2))
		fe = 1 / (tan(a2) - tan(b2))
		a1e = -degrees(atan(-2 * rne * tan(a2) + tan(a2) + 2 * rne * tan(b2) - 2 * tan(b2)))
		b1e = degrees(atan(2 * rne * tan(a2) - 2 * rne * tan(b2) + tan(b2)))

	flag = 100
################################ r,b1,b2 #############################################################################
	if X == [1, 2, 4, 5]:

		if rne == 0 or b1e == b2e:
			pass
		else:
			pe = (-2) * (rne * tan(b1) + rne * tan(b2)) / (tan(b2) - tan(b1))
			fe = -(2 * rne) / (tan(b2) - tan(b1))
			a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
			a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))

	if X == [2, 4, 5]:
		if rne == 0 and b1e == b2e:
			fe = (pe / 2 + rne) / tan(b1)
			a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
			a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
			k = 4
		elif rne ==0 and b1e != b2e:
			b1 = b2
			b1e = b2e
			fe = (pe / 2 + rne) / tan(b1)
			a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
			a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
			k = 4
			flag = 1
		elif b1 == b2 and rne != 0:
			rne = 0
			fe = (pe / 2 + rne) / tan(b1)
			a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
			a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
			k = 4
			flag = 0

	if X == [1, 4, 5]:
		if rne == 0 and b1e == b2e:
			pe = 2*(fe*tan(b1)-rne)
			a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
			a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
			k = 4
		elif rne == 0 and b1e != b2e:
			b1 = b2
			b1e = b2e
			pe = 2 * (fe * tan(b1) - rne)
			a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
			a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
			k = 4
			flag = 1
		elif b1 == b2 and rne != 0:
			rne = 0
			pe = 2 * (fe * tan(b1) - rne)
			a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
			a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
			k = 4
			flag = 0

	if X == [1, 2, 5]:
		if rne == 0 and b1e == b2e:
			pe = (tan(b1) + tan(b2)) / (tan(b1) - tan(a1))
			fe = 1 / (tan(b1) - tan(a1))
			a2e = -degrees(atan(tan(a1) - tan(b1) - tan(b2)))
			k = 4
		elif rne == 0 and b1e != b2e:
			b1 = b2
			b1e = b2e
			pe = (tan(b1) + tan(b2)) / (tan(b1) - tan(a1))
			fe = 1 / (tan(b1) - tan(a1))
			a2e = -degrees(atan(tan(a1) - tan(b1) - tan(b2)))
			k = 4
			flag = 1
		elif b1 == b2 and rne != 0:
			rne = 0
			pe = (tan(b1) + tan(b2)) / (tan(b1) - tan(a1))
			fe = 1 / (tan(b1) - tan(a1))
			a2e = -degrees(atan(tan(a1) - tan(b1) - tan(b2)))
			k = 4
			flag = 0

	if X == [1, 2, 4]:
		if rne == 0 and b1e == b2e:
			pe = (tan(b1) + tan(b2)) / (tan(a2) - tan(b2))
			fe = 1 / (tan(a2) - tan(b2))
			a1e = -degrees(atan(tan(a2) - tan(b1) - tan(b2)))
			k = 4
		elif rne == 0 and b1e != b2e:
			b1 = b2
			b1e = b2e
			pe = (tan(b1) + tan(b2)) / (tan(a2) - tan(b2))
			fe = 1 / (tan(a2) - tan(b2))
			a1e = -degrees(atan(tan(a2) - tan(b1) - tan(b2)))
			k = 4
			flag = 1
		elif b1 == b2 and rne != 0:
			rne = 0
			pe = (tan(b1) + tan(b2)) / (tan(a2) - tan(b2))
			fe = 1 / (tan(a2) - tan(b2))
			a1e = -degrees(atan(tan(a2) - tan(b1) - tan(b2)))
			k = 4
			flag = 0
####################################################################################################################

################################ r,a1,a2 #############################################################################
	if X == [1, 2, 6, 7]:
		if rne == 1 or a1e == a2e:
			pass
		else:
			fe = 2 * (rne - 1) / (tan(a1) - tan(a2))
			pe = fe * (tan(a1) + tan(a2))
			b1e = degrees(atan(((pe / 2) + rne) / fe))
			b2e = degrees(atan(((pe / 2) - rne) / fe))

	if X == [2, 6, 7]:
		if rne == 1 and a1e == a2e:
			fe = pe/(2*tan(a1))
			b1e = degrees(atan(((pe / 2) + rne) / fe))
			b2e = degrees(atan(((pe / 2) - rne) / fe))
			k = 4
		elif rne == 1 and a1e != a2e:
			a1 = a2
			a1e = a2e
			fe = pe / (2 * tan(a1))
			b1e = degrees(atan(((pe / 2) + rne) / fe))
			b2e = degrees(atan(((pe / 2) - rne) / fe))
			k = 4
			flag = 2
		elif a1 == a2 and rne != 1:
			rne = 1
			fe = pe / (2 * tan(a1))
			b1e = degrees(atan(((pe / 2) + rne) / fe))
			b2e = degrees(atan(((pe / 2) - rne) / fe))
			k = 4
			flag = 0

	if X == [1, 6, 7]:
		if rne == 1 and a1e == a2e:
			pe = fe * (tan(a1) + tan(a2))
			b1e = degrees(atan(((pe / 2) + rne) / fe))
			b2e = degrees(atan(((pe / 2) - rne) / fe))
			k = 4
		elif rne == 1 and a1e != a2e:
			a1 = a2
			a1e = a2e
			pe = fe * (tan(a1) + tan(a2))
			b1e = degrees(atan(((pe / 2) + rne) / fe))
			b2e = degrees(atan(((pe / 2) - rne) / fe))
			k = 4
			flag = 2
		elif a1 == a2 and rne != 1:
			rne = 1
			pe = fe * (tan(a1) + tan(a2))
			b1e = degrees(atan(((pe / 2) + rne) / fe))
			b2e = degrees(atan(((pe / 2) - rne) / fe))
			k = 4
			flag = 0

	if X == [1, 2, 7]:
		if rne == 1 and a1e == a2e:
			pe = (tan(a1) + tan(a2)) / (tan(b1) - tan(a1))
			fe = 1 / (tan(b1) - tan(a1))
			b2e = degrees(atan(tan(a1) + tan(a2) - tan(b1)))
			k = 4
		elif rne == 1 and a1e != a2e:
			a1 = a2
			a1e = a2e
			pe = (tan(a1) + tan(a2)) / (tan(b1) - tan(a1))
			fe = 1 / (tan(b1) - tan(a1))
			b2e = degrees(atan(tan(a1) + tan(a2) - tan(b1)))
			k = 4
			flag = 2
		elif a1 == a2 and rne != 1:
			rne = 1
			pe = (tan(a1) + tan(a2)) / (tan(b1) - tan(a1))
			fe = 1 / (tan(b1) - tan(a1))
			b2e = degrees(atan(tan(a1) + tan(a2) - tan(b1)))
			k = 4
			flag = 0

	if X == [1, 2, 6]:
		if rne == 1 and a1e == a2e:
			pe = (tan(a1) + tan(a2)) / (tan(a2) - tan(b2))
			fe = 1 / (tan(a2) - tan(b2))
			b1e = degrees(atan(tan(a1) + tan(a2) - tan(b2)))
			k = 4
		elif rne == 1 and a1e != a2e:
			a1 = a2
			a1e = a2e
			pe = (tan(a1) + tan(a2)) / (tan(a2) - tan(b2))
			fe = 1 / (tan(a2) - tan(b2))
			b1e = degrees(atan(tan(a1) + tan(a2) - tan(b2)))
			k = 4
			flag = 2
		elif a1 == a2 and rne != 1:
			rne = 1
			pe = (tan(a1) + tan(a2)) / (tan(a2) - tan(b2))
			fe = 1 / (tan(a2) - tan(b2))
			b1e = degrees(atan(tan(a1) + tan(a2) - tan(b2)))
			k = 4
			flag = 0
####################################################################################################################

################################ r,a2,b1 #############################################################################
	if X == [1, 2, 4, 7]:
		if rne == 0.5 or a2e == b1e:
			pass
		else:
			fe = (1-2*rne)/(tan(a2)-tan(b1))
			pe = fe * (tan(a2) + tan(b1)) - 1
			a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
			b2e = degrees(atan(((pe / 2) - rne) / fe))

	if X == [2, 4, 7]:
		if rne == 0.5 and a2e == b1e:
			fe = (0.5 + (pe/2))/tan(a2)
			a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
			b2e = degrees(atan(((pe / 2) - rne) / fe))
			k = 4
		elif rne == 0.5 and a2e != b1e:
			a2 = b1
			a2e = b1e
			fe = (0.5 + (pe / 2)) / tan(a2)
			a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
			b2e = degrees(atan(((pe / 2) - rne) / fe))
			k = 4
			flag = 3
		elif a2 == b1 and rne != 0.5:
			rne = 0.5
			fe = (0.5 + (pe / 2)) / tan(a2)
			a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
			b2e = degrees(atan(((pe / 2) - rne) / fe))
			k = 4
			flag = 0

	if X == [1, 4, 7]:
		if rne == 0.5 and a2e == b1e:
			pe = fe * (tan(a2) + tan(b1)) - 1
			a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
			b2e = degrees(atan(((pe / 2) - rne) / fe))
			k = 4
		elif rne == 0.5 and a2e != b1e:
			a2 = b1
			a2e = b1e
			pe = fe * (tan(a2) + tan(b1)) - 1
			a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
			b2e = degrees(atan(((pe / 2) - rne) / fe))
			k = 4
			flag = 3
		elif a2 == b1 and rne != 0.5:
			rne = 0.5
			pe = fe * (tan(a2) + tan(b1)) - 1
			a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
			b2e = degrees(atan(((pe / 2) - rne) / fe))
			k = 4
			flag = 0

	if X == [1, 2, 7]:
		if rne == 0.5 and a2e == b1e:
			pe = (tan(a1) + tan(a2)) / (tan(b1) - tan(a1))
			fe = 1 / (tan(b1) - tan(a1))
			b2e = degrees(atan(tan(a1) + tan(a2) - tan(b1)))
			k = 4
		elif rne == 0.5 and a2e != b1e:
			a2 = b1
			a2e = b1e
			pe = (tan(a1) + tan(a2)) / (tan(b1) - tan(a1))
			fe = 1 / (tan(b1) - tan(a1))
			b2e = degrees(atan(tan(a1) + tan(a2) - tan(b1)))
			k = 4
			flag = 3
		elif a2 == b1 and rne != 0.5:
			rne = 0.5
			pe = (tan(a1) + tan(a2)) / (tan(b1) - tan(a1))
			fe = 1 / (tan(b1) - tan(a1))
			b2e = degrees(atan(tan(a1) + tan(a2) - tan(b1)))
			k = 4
			flag = 0

	if X == [1, 2, 4]:
		if rne == 0.5 and a2e == b1e:
			pe = (tan(b1) + tan(b2)) / (tan(a2) - tan(b2))
			fe = 1 / (tan(a2) - tan(b2))
			a1e = -degrees(atan(tan(a2) - tan(b1) - tan(b2)))
			k = 4
		elif rne == 0.5 and a2e != b1e:
			a2 = b1
			a2e = b1e
			pe = (tan(b1) + tan(b2)) / (tan(a2) - tan(b2))
			fe = 1 / (tan(a2) - tan(b2))
			a1e = -degrees(atan(tan(a2) - tan(b1) - tan(b2)))
			k = 4
			flag = 3
		elif a2 == b1 and rne != 0.5:
			rne = 0.5
			pe = (tan(b1) + tan(b2)) / (tan(a2) - tan(b2))
			fe = 1 / (tan(a2) - tan(b2))
			a1e = -degrees(atan(tan(a2) - tan(b1) - tan(b2)))
			k = 4
			flag = 0
####################################################################################################################

################################ r,b2,a1 #############################################################################
	if X == [1, 2, 5, 6]:
		if rne == 0.5 or a1e == b2e:
			pass
		else:
			fe = (2 * rne - 1) / (tan(a1) - tan(b2))
			pe = fe * (tan(a1) + tan(b1)) + 1
			a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
			b1e = degrees(atan(((pe / 2) + rne) / fe))

	if X == [2, 5, 6]:
		if rne == 0.5 and a1e == b2e:
			fe = (0.5+pe/2)/tan(b2)
			a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
			b1e = degrees(atan(((pe / 2) + rne) / fe))
			k = 4
		elif rne == 0.5 and a1e != b2e:
			a1 = b2
			a1e = b2e
			fe = (2 * rne - 1) / (tan(a1) - tan(b2))
			a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
			b1e = degrees(atan(((pe / 2) + rne) / fe))
			k = 4
			flag = 2
		elif a1 == b2 and rne != 0.5:
			rne = 0.5
			fe = (2 * rne - 1) / (tan(a1) - tan(b2))
			a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
			b1e = degrees(atan(((pe / 2) + rne) / fe))
			k = 4
			flag = 0

	if X == [1, 5, 6]:
		if rne == 0.5 and a1e == b2e:
			pe = fe * (tan(a1) + tan(b2)) + 1
			a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
			b1e = degrees(atan(((pe / 2) + rne) / fe))
			k = 4
		elif rne == 0.5 and a1e != b2e:
			a1 = b2
			a1e = b2e
			pe = fe * (tan(a1) + tan(b2)) + 1
			a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
			b1e = degrees(atan(((pe / 2) + rne) / fe))
			k = 4
			flag = 2
		elif a1 == b2 and rne != 0.5:
			rne = 0.5
			pe = fe * (tan(a1) + tan(b2)) + 1
			a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
			b1e = degrees(atan(((pe / 2) + rne) / fe))
			k = 4
			flag = 0

	if X == [1, 2, 6]:
		if rne == 0.5 and a1e == b2e:
			pe = (tan(a1) + tan(a2)) / (tan(a2) - tan(b2))
			fe = 1 / (tan(a2) - tan(b2))
			b1e = degrees(atan(tan(a1) + tan(a2) - tan(b2)))
			k = 4
		elif rne == 0.5 and a1e != b2e:
			a1 = b2
			a1e = b2e
			pe = (tan(a1) + tan(a2)) / (tan(a2) - tan(b2))
			fe = 1 / (tan(a2) - tan(b2))
			b1e = degrees(atan(tan(a1) + tan(a2) - tan(b2)))
			k = 4
			flag = 2
		elif a1 == b2 and rne != 0.5:
			rne = 0.5
			pe = (tan(a1) + tan(a2)) / (tan(a2) - tan(b2))
			fe = 1 / (tan(a2) - tan(b2))
			b1e = degrees(atan(tan(a1) + tan(a2) - tan(b2)))
			k = 4
			flag = 0

	if X == [1, 2, 5]:
		if rne == 0.5 and a1e == b2e:
			pe = (tan(b1) + tan(b2)) / (tan(b1) - tan(a1))
			fe = 1 / (tan(b1) - tan(a1))
			a2e = -degrees(atan(tan(a1) - tan(b1) - tan(b2)))
			k = 4
		elif rne == 0.5 and a1e != b2e:
			a1 = b2
			a1e = b2e
			pe = (tan(b1) + tan(b2)) / (tan(b1) - tan(a1))
			fe = 1 / (tan(b1) - tan(a1))
			a2e = -degrees(atan(tan(a1) - tan(b1) - tan(b2)))
			k = 4
			flag = 2
		elif a1 == b2 and rne != 0.5:
			rne = 0.5
			pe = (tan(b1) + tan(b2)) / (tan(b1) - tan(a1))
			fe = 1 / (tan(b1) - tan(a1))
			a2e = -degrees(atan(tan(a1) - tan(b1) - tan(b2)))
			k = 4
			flag = 0
####################################################################################################################

################################ f,a1,b1 #############################################################################
	if X == [1, 3, 5, 7]:
		pass
	if X == [3, 5, 7]:
		if a1 == b1:
			a1 =+ 1
		fe = 1/(tan(b1)-tan(a1))
		rne =  fe * tan(a1) - pe/2 + 1
		a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
		b2e = degrees(atan(((pe / 2) - rne) / fe))
		k = 4
	if X == [1, 5, 7]:
		if a1 == b1:
			a1 =+ 1
		fe = 1 / (tan(b1) - tan(a1))
		pe = 2*(-rne + fe*tan(b1))
		a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
		b2e = degrees(atan(((pe / 2) - rne) / fe))
		k = 4
	if X == [1, 3, 7]:
		if a1 == b1:
			a1 =+ 1
		fe = 1 / (tan(b1) - tan(a1))
		pe = fe*(tan(a2)+tan(a1))
		rne = fe*tan(b1)-pe/2
		b2e = degrees(atan(((pe / 2) - rne) / fe))
		k = 4
	if X == [1, 3, 5]:
		if a1 == b1:
			a1 =+ 1
		fe = 1 / (tan(b1) - tan(a1))
		pe = fe*(tan(b2)+tan(a1)) + 1
		rne = fe*tan(b1)-pe/2
		a2e = degrees(atan(((pe / 2) + 1 - rne) / fe))
		k = 4
######################################################################################################################

################################ f,a2,b2 #############################################################################
	if X == [1, 3, 4, 6]:
		pass
	if X == [3, 4, 6]:
		if a2 == b2:
			a2  = +  1
		fe = 1 / (tan(a2) - tan(b2))
		rne = - fe * tan(a2) + pe / 2 + 1
		a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
		b1e = degrees(atan(((pe / 2) + rne) / fe))
		k = 4
	if X == [1, 4, 6]:
		if a2 == b2:
			a2  = +  1
		fe = 1 / (tan(a2) - tan(b2))
		pe = 2 * (rne + fe * tan(b2))
		a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
		b1e = degrees(atan(((pe / 2) + rne) / fe))
		k = 4
	if X == [1, 3, 6]:
		if a2 == b2:
			a2  = +  1
		fe = 1 / (tan(a2) - tan(b2))
		pe = fe * (tan(a2) + tan(a1))
		rne = pe / 2 - fe * tan(b2)
		b1e = degrees(atan(((pe / 2) + rne) / fe))
		k = 4
	if X == [1, 3, 4]:
		if a2 == b2:
			a2  = +  1
		fe = 1 / (tan(a2) - tan(b2))
		pe = fe * (tan(a2) + tan(b1)) - 1
		rne = pe / 2 - fe * tan(b2)
		a1e = degrees(atan(((pe / 2) - 1 + rne) / fe))
		k = 4
######################################################################################################################
	if X == []:
		firstPopup()

	pe = str(round(float(pe),3))
	fe = str(round(float(fe),3))
	rne = str(round(float(rne),3))
	a1e = str(round(float(a1e),3))
	a2e = str(round(float(a2e),3))
	#a3e = str(round(float(a3e),3))
	b1e = str(round(float(b1e),3))
	b2e = str(round(float(b2e),3))
	#b3e = str(round(float(b3e),3))

	return pe,fe,rne,a1e,a2e,b1e,b2e,k,t,X,flag
