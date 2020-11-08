from scipy.optimize import fsolve
import numpy as np

def system_solver1(pe,fe,rne,a1e,a2e,b1e,b2e):

	X = []

	if pe == '':
		X.append(1)
	if fe == '':
		X.append(2)
	if rne == '':
		X.append(3)
	if a1e == '':
		X.append(4)
	if a2e == '':
		X.append(5)
	if b1e == '':
		X.append(6)
	if b2e == '':
		X.append(7)

	k = len(X)
	t = len(X)

	def sys(z):

		i = 0

		if 1 in X:
			pev = z[i]
			i = i + 1
		else:
			pev = float(pe)

		if 2 in X:
			fev = z[i]
			i = i + 1
		else:
			fev = float(fe)

		if 3 in X:
			rnev = z[i]
			i = i + 1
		else:
			rnev = float(rne)

		if 4 in X:
			a1ev = z[i]
			i = i + 1
		else:
			a1ev = float(a1e)

		if 5 in X:
			a2ev = z[i]
			i = i + 1
		else:
			a2ev = float(a2e)

		if 6 in X:
			b1ev = z[i]
			i = i + 1
		else:
			b1ev = float(b1e)

		if 7 in X:
			b2ev = z[i]
			i = i + 1
		else:
			b2ev = float(b2e)

		F = np.zeros((4))


		F[0] = -a1ev - np.degrees(np.arctan(-((pev / 2) - 1 + rnev) / fev))
		F[1] = -a2ev + np.degrees(np.arctan(((pev / 2) + 1 - rnev) / (fev)))
		F[2] = -b1ev + np.degrees(np.arctan(((pev / 2) + rnev) / fev))
		F[3] = -b2ev - np.degrees(np.arctan(-((pev / 2) - rnev) / fev))

		return F

	r = fsolve(sys, [1, 1, 1, 1])

	j = 0

	if pe == '':
		pe = str(round(r[j], 3))
		j = j + 1
	if fe == '':
		fe = str(round(r[j], 3))
		j = j + 1
	if rne == '':
		rne = str(round(r[j], 3))
		j = j + 1
	if a1e == '':
		a1e = str(round(r[j], 3))
		j = j + 1
	if a2e == '':
		a2e = str(round(r[j], 3))
		j = j + 1
	if b1e == '':
		b1e = str(round(r[j], 3))
		j = j + 1
	if b2e == '':
		b2e = str(round(r[j], 3))
		j = j + 1

	pe = str(round(float(pe),3))
	fe = str(round(float(fe),3))
	rne = str(round(float(rne),3))
	a1e = str(round(float(a1e),3))
	a2e = str(round(float(a2e),3))
	#a3e = str(round(float(a3e),3))
	b1e = str(round(float(b1e),3))
	b2e = str(round(float(b2e),3))
	#b3e = str(round(float(b3e),3))

	return pe,fe,rne,a1e,a2e,b1e,b2e,k,t
	
