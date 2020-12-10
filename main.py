from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.lang import Builder
from kivy.properties import StringProperty
import math as m
from kivy.metrics import Metrics
import numpy as np
from kivymd.app import MDApp
# from system_solver import system_solver1
from solver_if import system_if,system_X
# import csv
from all_popups import firstPopup, secondPopup, thirdPopup, rpmPopup, h2tPopup, diamPopup, error_Popup
# from creating_database import create_database_nd
###########################################################################################
# from kivy.uix.popup import Popup
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.uix.boxlayout import BoxLayout
# from kivymd.uix.button import MDFillRoundFlatButton


class VelocityTriangles(Screen):

	########## Window properties #########
	Config.set('graphics', 'resizable', True)
	Window.size = (400, 700)
	Window.softinput_mode = "below_target"

	######### Variable properties ########
	p  = ObjectProperty(None)
	f  = ObjectProperty(None)
	rn = ObjectProperty(None)
	a1 = ObjectProperty(None)
	a2 = ObjectProperty(None)
	a3 = ObjectProperty(None)
	b1 = ObjectProperty(None)
	b2 = ObjectProperty(None)
	b3 = ObjectProperty(None)

	d1 = ObjectProperty(None)
	d2 = ObjectProperty(None)
	d3 = ObjectProperty(None)
	rh2t1 = ObjectProperty(None)
	rh2t2 = ObjectProperty(None)
	rh2t3 = ObjectProperty(None)

	check = NumericProperty(0)

	n = ObjectProperty(None)
	l = NumericProperty(0)
	k =  NumericProperty(0) #### Debugging tool for less than 3 variables and for not changing window ######
	t = NumericProperty(0) ##### Debugging tool for more than 3 variables ####

	j = NumericProperty(0)
	#### Values of checkboxes state ##########
	ch1_value = ObjectProperty('normal')
	ch2_value = ObjectProperty('normal')
	ch3_value = ObjectProperty('normal')
	ch4_value = ObjectProperty('normal')
	ch5_value = ObjectProperty('normal')

	def systemsolver(self):
		try:
			global a1e
			global a2e
			global b1e
			global b2e
			global pe
			global fe
			global rne
			global i

			pe  = str(self.p.text)
			fe  = str(self.f.text)
			rne = str(self.rn.text)
			a1e = str(self.a1.text)
			a2e = str(self.a2.text)
			a3e = str(self.a3.text)
			b1e = str(self.b1.text)
			b2e = str(self.b2.text)
			b3e = str(self.b3.text)

			global D1e
			global D2e
			global D3e
			global Rh1e
			global Rh2e
			global Rh3e
			global Ne

			D1e = str(self.d1.text)
			D2e = str(self.d2.text)
			D3e = str(self.d3.text)
			Rh1e = str(self.rh2t1.text)
			Rh2e = str(self.rh2t2.text)
			Rh3e = str(self.rh2t3.text)
			Ne = str(self.n.text)

			##################   System_Solver  ################
			pe, fe, rne, a1e, a2e, b1e, b2e, self.k, t, X = system_if(pe, fe, rne, a1e, a2e, b1e, b2e)
			self.manager.get_screen('mid_sc').XText = str(X)
			# with open('data.csv', 'w', newline='') as file:
			# 	writer = csv.writer(file)
			# 	writer.writerow(["ψ", "φ", "Rn", "α1", "α2", "β1", "β2"])
			# 	writer.writerow([str(pe),str(fe),str(rne),str(a1e),str(a2e),str(b1e),str(b2e)])

			############################# Drawing Triangles ######################################
			global U
			global x0
			global y0
			global x1
			global y1

			x0,y0 = Window.size[0]*130/400,Window.size[1]*70/700
			x1,y1 = Window.size[0]*270/400,Window.size[1]*70/700
			U = x1-x0
			xL = x1 - U*float(rne)-U*float(pe)/2
			yL = y0 + U*float(fe)
			xR = x1 - U*float(rne) +U*float(pe)/2
			yR = y0 + U*float(fe)

	######### While functions for triangles fitting #########
			while xL < self.x + Window.size[0]*60/400 or xR > self.width -  Window.size[0]*80/400 or yL >  Window.size[1]*200/700 \
					or xR < self.x +  Window.size[0]*60/400 or xL > self.width -  Window.size[0] * 80 / 400:

				x0 = x0 + 1
				x1 = x1 - 1

				U = x1 - x0
				xL = x1 - U * float(rne) - U * float(pe) / 2
				yL = y0 + U * float(fe)
				xR = x1 - U * float(rne) + U * float(pe) / 2
				yR = y0 + U * float(fe)

			############### Computing base angles  ############################

			a1d = 180 + float(a1e) - 90
			a2d = 180 - float(a2e) - 90
			b1d = 180 - float(b1e) - 90
			b2d = 180 - float(b2e) - 90

			############### Computing rotating arrow points  ############################

			xL1u = x0 + (Window.size[0] / 400) * 25 * m.cos(m.radians(a1d + 11.3))
			yL1u = y0 + (Window.size[1] / 700) * 25 * m.sin(m.radians(a1d + 11.3))
			xL1d = x0 + (Window.size[0] / 400) * 25 * m.cos(m.radians(a1d - 11.3))
			yL1d = y0 + (Window.size[1] / 700) * 25 * m.sin(m.radians(a1d - 11.3))

			xL2u = x0 + (Window.size[0] / 400) * 25 * m.cos(m.radians(a2d + 11.3))
			yL2u = y0 + (Window.size[1] / 700) * 25 * m.sin(m.radians(a2d + 11.3))
			xL2d = x0 + (Window.size[0] / 400) * 25 * m.cos(m.radians(a2d - 11.3))
			yL2d = y0 + (Window.size[1] / 700) * 25 * m.sin(m.radians(a2d - 11.3))

			xR1u = x1 - (Window.size[0] / 400) * 25 * m.cos(m.radians(b1d + 11.3))
			yR1u = y1 + (Window.size[1] / 700) * 25 * m.sin(m.radians(b1d + 11.3))
			xR1d = x1 - (Window.size[0] / 400) * 25 * m.cos(m.radians(b1d - 11.3))
			yR1d = y1 + (Window.size[1] / 700) * 25 * m.sin(m.radians(b1d - 11.3))

			xR2u = x1 + (Window.size[0] / 400) * 25 * m.cos(m.radians(b2d + 11.3))
			yR2u = y1 + (Window.size[1] / 700) * 25 * m.sin(m.radians(b2d + 11.3))
			xR2d = x1 + (Window.size[0] / 400) * 25 * m.cos(m.radians(b2d - 11.3))
			yR2d = y1 + (Window.size[1] / 700) * 25 * m.sin(m.radians(b2d - 11.3))

			######################### Choosing if it is Turbine or Compressor ###################
			if self.ch1_value == 'down':
				tc = 0  # turbine
				tc_namem = 'Turbine Middle'
				tc_nameh = 'Turbine Hub'
				tc_namet = 'Turbine Tip'
				ptnm_x = self.x - self.width / 2 + Window.size[0] * 76 / 400
				ptnh_x = self.x - self.width / 2 + Window.size[0] * 67 / 400
				ptnt_x = self.x - self.width / 2 + Window.size[0] * 65 / 400
			elif self.ch2_value == 'down':
				tc = 1  # compressor
				tc_namem = 'Compressor Middle'
				tc_nameh = 'Compressor Hub'
				tc_namet = 'Compressor Tip'
				ptnm_x = self.x - self.width / 2 + Window.size[0] * 91 / 400
				ptnh_x = self.x - self.width / 2 + Window.size[0] * 82 / 400
				ptnt_x = self.x - self.width / 2 + Window.size[0] * 80 / 400
			else:
				if float(pe) > 0.999:
					if abs(x1-xL)>abs(x1-xR):
						tc = 0  # turbine
						tc_namem = 'Turbine Middle'
						tc_nameh = 'Turbine Hub'
						tc_namet = 'Turbine Tip'
						ptnm_x = self.x - self.width / 2 + Window.size[0] * 76 / 400
						ptnh_x = self.x - self.width / 2 + Window.size[0] * 67 / 400
						ptnt_x = self.x - self.width / 2 + Window.size[0] * 65 / 400
					else:
						tc = 1  # compressor
						tc_namem = 'Compressor Middle'
						tc_nameh = 'Compressor Hub'
						tc_namet = 'Compressor Tip'
						ptnm_x = self.x - self.width / 2 + Window.size[0] * 91 / 400
						ptnh_x = self.x - self.width / 2 + Window.size[0] * 82 / 400
						ptnt_x = self.x - self.width / 2 + Window.size[0] * 80 / 400
				else:
					if abs(x1 - xL) > abs(x1 - xR):
						tc = 1  # compressor
						tc_namem = 'Compressor Middle'
						tc_nameh = 'Compressor Hub'
						tc_namet = 'Compressor Tip'
						ptnm_x = self.x - self.width / 2 + Window.size[0] * 91 / 400
						ptnh_x = self.x - self.width / 2 + Window.size[0] * 82 / 400
						ptnt_x = self.x - self.width / 2 + Window.size[0] * 80 / 400
					else:
						tc = 0  # turbine
						tc_namem = 'Turbine Middle'
						tc_nameh = 'Turbine Hub'
						tc_namet = 'Turbine Tip'
						ptnm_x = self.x - self.width / 2 + Window.size[0] * 76 / 400
						ptnh_x = self.x - self.width / 2 + Window.size[0] * 67 / 400
						ptnt_x = self.x - self.width / 2 + Window.size[0] * 65 / 400

			# create_database_nd(pe, fe, rne, a1e, a2e, b1e, b2e, tc)

#####################  Checking if the second compartment is completed ####################
			if D1e == '' and D2e == '' and D3e == '' and Rh1e == '' and Rh2e == '' and Rh3e == '' and Ne == '':
				self.check = 1
			else:
				self.check = 0
############################################################################################

################ Case of  Both Compartments filled #########################################
			if self.check == 0:	
				############### Passing the Results on the Second Screen  ####################
				self.manager.get_screen('mid_sc').pText = pe
				self.manager.get_screen('mid_sc').fText = fe
				self.manager.get_screen('mid_sc').rnText = rne
				self.manager.get_screen('mid_sc').a1Text = a1e
				self.manager.get_screen('mid_sc').a2Text = a2e
				self.manager.get_screen('mid_sc').a3Text = a3e
				self.manager.get_screen('mid_sc').b1Text = b1e
				self.manager.get_screen('mid_sc').b2Text = b2e
				self.manager.get_screen('mid_sc').b3Text = b3e
	
				############### Passing the Triangles Points on the Second Screen  ##################
				self.manager.get_screen('mid_sc').x0Text = str(x0)
				self.manager.get_screen('mid_sc').y0Text = str(y0)
				self.manager.get_screen('hub_sc').y0Text = str(y0)
				self.manager.get_screen('tip_sc').y0Text = str(y0)
				self.manager.get_screen('mid_sc').x1Text = str(x1)
				self.manager.get_screen('mid_sc').y1Text = str(y1)
				self.manager.get_screen('hub_sc').y1Text = str(y1)
				self.manager.get_screen('tip_sc').y1Text = str(y1)
				self.manager.get_screen('mid_sc').UText = str(U)
				self.manager.get_screen('mid_sc').xLText = str(xL)
				self.manager.get_screen('mid_sc').yLText = str(yL)
				self.manager.get_screen('mid_sc').xRText = str(xR)
				self.manager.get_screen('mid_sc').yRText = str(yR)
	
				############### Passing the Arrow Points on the Second Screen  ##################
				self.manager.get_screen('mid_sc').xL1uText = str(xL1u)
				self.manager.get_screen('mid_sc').yL1uText = str(yL1u)
				self.manager.get_screen('mid_sc').xL1dText = str(xL1d)
				self.manager.get_screen('mid_sc').yL1dText = str(yL1d)
	
				self.manager.get_screen('mid_sc').xL2uText = str(xL2u)
				self.manager.get_screen('mid_sc').yL2uText = str(yL2u)
				self.manager.get_screen('mid_sc').xL2dText = str(xL2d)
				self.manager.get_screen('mid_sc').yL2dText = str(yL2d)
	
				self.manager.get_screen('mid_sc').xR1uText = str(xR1u)
				self.manager.get_screen('mid_sc').yR1uText = str(yR1u)
				self.manager.get_screen('mid_sc').xR1dText = str(xR1d)
				self.manager.get_screen('mid_sc').yR1dText = str(yR1d)
	
				self.manager.get_screen('mid_sc').xR2uText = str(xR2u)
				self.manager.get_screen('mid_sc').yR2uText = str(yR2u)
				self.manager.get_screen('mid_sc').xR2dText = str(xR2d)
				self.manager.get_screen('mid_sc').yR2dText = str(yR2d)
	
				############### Passing the compressor or turbine text and possition on the Second Screen  ##################
				self.manager.get_screen('mid_sc').tc_namemText = tc_namem
				self.manager.get_screen('mid_sc').tc_namehText = tc_nameh
				self.manager.get_screen('mid_sc').tc_nametText = tc_namet
				self.manager.get_screen('mid_sc').ptnm_xText = str(ptnm_x)
				self.manager.get_screen('mid_sc').ptnh_xText = str(ptnh_x)
				self.manager.get_screen('mid_sc').ptnt_xText = str(ptnt_x)

				self.manager.get_screen('hub_sc').tc_namehText = tc_nameh
				self.manager.get_screen('hub_sc').tc_namemText = tc_namem
				self.manager.get_screen('tip_sc').tc_nametText = tc_namet
				self.manager.get_screen('tip_sc').tc_namemText = tc_namem
				self.manager.get_screen('hub_sc').ptnh_xText = str(ptnh_x)
				self.manager.get_screen('tip_sc').ptnt_xText = str(ptnt_x)


				############### Passing the Triangles Points on the Second Screen  ##################
				self.manager.get_screen('comp_sc').x0Text = str(x0)
				self.manager.get_screen('comp_sc').y0Text = str(y0)
				self.manager.get_screen('comp_sc').x1Text = str(x1)
				self.manager.get_screen('comp_sc').y1Text = str(y1)
				self.manager.get_screen('comp_sc').UText = str(U)
				self.manager.get_screen('comp_sc').xLText = str(xL)
				self.manager.get_screen('comp_sc').yLText = str(yL)
				self.manager.get_screen('comp_sc').xRText = str(xR)
				self.manager.get_screen('comp_sc').yRText = str(yR)

				############### Passing the Arrow Points on the Second Screen  ##################
				self.manager.get_screen('comp_sc').xL1uText = str(xL1u)
				self.manager.get_screen('comp_sc').yL1uText = str(yL1u)
				self.manager.get_screen('comp_sc').xL1dText = str(xL1d)
				self.manager.get_screen('comp_sc').yL1dText = str(yL1d)

				self.manager.get_screen('comp_sc').xL2uText = str(xL2u)
				self.manager.get_screen('comp_sc').yL2uText = str(yL2u)
				self.manager.get_screen('comp_sc').xL2dText = str(xL2d)
				self.manager.get_screen('comp_sc').yL2dText = str(yL2d)

				self.manager.get_screen('comp_sc').xR1uText = str(xR1u)
				self.manager.get_screen('comp_sc').yR1uText = str(yR1u)
				self.manager.get_screen('comp_sc').xR1dText = str(xR1d)
				self.manager.get_screen('comp_sc').yR1dText = str(yR1d)

				self.manager.get_screen('comp_sc').xR2uText = str(xR2u)
				self.manager.get_screen('comp_sc').yR2uText = str(yR2u)
				self.manager.get_screen('comp_sc').xR2dText = str(xR2d)
				self.manager.get_screen('comp_sc').yR2dText = str(yR2d)

				self.manager.get_screen('comp_sc').tc_namemText = tc_namem

			################ Case of  the First Compartment filled #########################################
			else:
				############### Passing the Results on the Second Screen  ############################
				self.manager.get_screen('simple').pText = pe
				self.manager.get_screen('simple').fText = fe
				self.manager.get_screen('simple').rnText = rne
				self.manager.get_screen('simple').a1Text = a1e
				self.manager.get_screen('simple').a2Text = a2e
				self.manager.get_screen('simple').a3Text = a3e
				self.manager.get_screen('simple').b1Text = b1e
				self.manager.get_screen('simple').b2Text = b2e
				self.manager.get_screen('simple').b3Text = b3e

				############### Passing the Triangles Points on the Second Screen  ##################
				self.manager.get_screen('simple').x0Text = str(x0)
				self.manager.get_screen('simple').y0Text = str(y0)
				self.manager.get_screen('simple').x1Text = str(x1)
				self.manager.get_screen('simple').y1Text = str(y1)
				self.manager.get_screen('simple').UText = str(U)
				self.manager.get_screen('simple').xLText = str(xL)
				self.manager.get_screen('simple').yLText = str(yL)
				self.manager.get_screen('simple').xRText = str(xR)
				self.manager.get_screen('simple').yRText = str(yR)

				############### Passing the Arrow Points on the Second Screen  ##################
				self.manager.get_screen('simple').xL1uText = str(xL1u)
				self.manager.get_screen('simple').yL1uText = str(yL1u)
				self.manager.get_screen('simple').xL1dText = str(xL1d)
				self.manager.get_screen('simple').yL1dText = str(yL1d)

				self.manager.get_screen('simple').xL2uText = str(xL2u)
				self.manager.get_screen('simple').yL2uText = str(yL2u)
				self.manager.get_screen('simple').xL2dText = str(xL2d)
				self.manager.get_screen('simple').yL2dText = str(yL2d)

				self.manager.get_screen('simple').xR1uText = str(xR1u)
				self.manager.get_screen('simple').yR1uText = str(yR1u)
				self.manager.get_screen('simple').xR1dText = str(xR1d)
				self.manager.get_screen('simple').yR1dText = str(yR1d)

				self.manager.get_screen('simple').xR2uText = str(xR2u)
				self.manager.get_screen('simple').yR2uText = str(yR2u)
				self.manager.get_screen('simple').xR2dText = str(xR2d)
				self.manager.get_screen('simple').yR2dText = str(yR2d)

				############### Passing the compressor or turbine text and possition on the Second Screen  ##################
				self.manager.get_screen('simple').tc_namemText = tc_namem
				self.manager.get_screen('simple').ptnm_xText = str(ptnm_x)

################ Debugging Section #################
			if self.k == 4:
				if float(b1e) - float(a1e) < 2 or float(a2e) - float(b2e) < 2:
					self.popup = secondPopup()
					self.k = 0

		except:
		########## It goes in to except if only variables are less than 3. So if is unnecesery #########
			X = system_X(pe,fe,rne,a1e,a2e,b1e,b2e)
			if X == [1,2,4,5] or X == [1,2,6,7] or X == [1, 2, 4, 7] or X == [1, 2, 5, 6] or X == [1, 3, 5, 7] or X == [1, 3, 4, 6]:
				error_Popup()
				self.k = 0
			else:
				firstPopup()
				self.k = 0  # mia allh timh oxi 4 gia na mhn allazei window

################          Dimendional Analisys           ################################
	def dml(self):
		try:
			global rh
			global rt
			global rm
			global Um
			global Uh
			global Ut
			global Vx
			global Vth1
			global Vth2

			if self.k != 0:
				if float(D1e) <= 0:
					self.popup = diamPopup()
					self.k = 0

				elif float(Rh1e) <= 0 or float(Rh1e) >= 1:
					self.popup = h2tPopup()
					self.k = 0


				elif float(Ne) <= 0:
					self.popup = rpmPopup()
					self.k = 0

			rt = float(D1e)/2
			rh = float(Rh1e)*rt
			rm = (rt+rh)/2

			Um = (1/60) * float(Ne) * rm

			Uh = (1/60) * float(Ne) * rh

			Ut = (1/60)* float(Ne) * rt

			Vx = float(fe)*Um

			dvth = float(pe)*Um

			V1 = Vx/m.cos(m.radians(float(a1e)))

			V2 = Vx/m.cos(m.radians(float(a2e)))

			W1 = Vx / m.cos(m.radians(float(b1e)))

			W2 = Vx / m.cos(m.radians(float(b2e)))

			Vth1 = -V1 * m.sin(m.radians(float(a1e)))
			Vth2 = V2 * m.sin(m.radians(float(a2e)))
			Wth1 = -W1 * m.sin(m.radians(float(b1e)))
			Wth2 = W2 * m.sin(m.radians(float(b2e)))


			############### Passing the Results on the Second Screen  ##################
			self.manager.get_screen('mid_sc').UmText = str(round(Um, 3))
			self.manager.get_screen('mid_sc').VxText = str(round(Vx, 3))
			self.manager.get_screen('mid_sc').V1Text = str(round(V1, 3))
			self.manager.get_screen('mid_sc').V2Text = str(round(V2, 3))
			self.manager.get_screen('mid_sc').W1Text = str(round(W1, 3))
			self.manager.get_screen('mid_sc').W2Text = str(round(W2, 3))
			self.manager.get_screen('mid_sc').DVthText = str(round(dvth, 3))
			self.manager.get_screen('mid_sc').Vth1Text = str(round(Vth1, 3))
			self.manager.get_screen('mid_sc').Vth2Text = str(round(Vth2, 3))
			self.manager.get_screen('mid_sc').Wth1Text = str(round(Wth1, 3))
			self.manager.get_screen('mid_sc').Wth2Text = str(round(Wth2, 3))


		except:
			if D1e == '' and D2e == '' and D3e == '' and Rh1e == '' and Rh2e == '' and Rh3e == '' and Ne == '':
				self.check = 1
			else:
				if self.k == 0:
					self.check = 1
				else:
					self.popup = thirdPopup()
					self.k = 0
					self.check = 1

#######################     Radial Balance  Computation   #######################
	def h2t_triangles(self):
		a = Um * (1 - float(rne))
		b = Vth2 - a

		if self.ch3_value == 'normal' and self.ch3_value == 'normal' and self.ch3_value == 'normal':
			n = 0
		if self.ch3_value == 'down' :
			n = 0
		if self.ch4_value == 'down' :
			n = -1
		if self.ch5_value == 'down' :
			n = 2


		#########    HUB    ##########
		Vth1h = a * ((rh / rm))** n - b * (rm / rh)
		Vth2h = a * (rh / rm) ** n + b * (rm / rh)
		Vx1h = m.sqrt(abs(Vx ** 2 - 2 * a * (np.log(rh / rm) - b * ((rm / rh) - 1))))
		Vx2h = m.sqrt(abs(Vx ** 2 - 2 * a * (np.log(rh / rm) + b * ((rm / rh) - 1))))
		# Vx1h = m.sqrt(Vx**2 - 2*(a**2)*(rh**2 - rm**2)-4*a*b*np.log(rh/rm))
		# Vx2h = m.sqrt(Vx ** 2 - 2 * (a ** 2) * (rh ** 2 - rm ** 2) + 4 * a * b * np.log(rh / rm))
		dVthh = Vth2h - Vth1h
		# rneh = 1 + (((a / Um) * (2 * ((rh / rm) ** (n - 1)) - n - 1)) / (n - 1))
		rneh = 1 - (a/Um)*(rh/rm)**(n-1)
		feh1 = Vx1h / Uh
		feh2 = Vx2h / Uh
		peh = dVthh/Uh

		Wth1h = Vth1h - Uh
		Wth2h = Vth2h - Uh

		a1eh = -np.degrees(np.arctan(Vth1h/Vx1h))
		a2eh = np.degrees(np.arctan(Vth2h / Vx2h))
		b1eh = -np.degrees(np.arctan(Wth1h/Vx1h))
		b2eh = np.degrees(np.arctan(Wth2h / Vx2h))

		V1h = Vx1h / m.cos(m.radians(float(a1eh)))
		V2h = Vx2h / m.cos(m.radians(float(a2eh)))
		W1h = Vx1h / m.cos(m.radians(float(b1eh)))
		W2h = Vx2h / m.cos(m.radians(float(b2eh)))

		#############     Drawing Hub Triangles       ############

		Uhp = (Uh/Um)*U
		difH = U - Uhp
		x0h = x0 + difH/2
		x1h = x1 - difH / 2

		# xLh = x1h - Uhp * float(rneh) - Uhp * float(peh) / 2
		xLh = x0h + (Vth1h/Uh)*Uhp
		yLh = y0 + Uhp * float(feh1)
		# xRh = x1h - Uhp * float(rneh) + Uhp * float(peh) / 2
		xRh = x0h + (Vth2h/Uh)*Uhp
		yRh = y0 + Uhp * float(feh2)

		while xRh > self.width - Window.size[0] * 80 / 400 or xLh < self.x + Window.size[0] * 80 / 400 \
				or yLh > Window.size[1] * 200 / 700 or yRh > Window.size[1] * 200 / 700 \
				or xLh > self.width - Window.size[0] * 80 / 400 or xRh < self.x + Window.size[0] * 80 / 400:
			x0h = x0h + 1
			x1h = x1h - 1
			Uhp = x1h - x0h

			xLh = x1h - Uhp * float(rneh) - Uhp * float(peh) / 2
			yLh = y0 + Uhp * float(feh1)
			xRh = x1h - Uhp * float(rneh) + Uhp * float(peh) / 2
			yRh = y0 + Uhp * float(feh2)

		a1dh = 180 + float(a1eh) - 90
		a2dh = 180 - float(a2eh) - 90
		b1dh = 180 - float(b1eh) - 90
		b2dh = 180 - float(b2eh) - 90

		############### Computing rotating arrow points  ############################

		xL1uh = x0h + (Window.size[0] / 400) * 25 * m.cos(m.radians(a1dh + 11.3))
		yL1uh = y0 + (Window.size[1] / 700) * 25 * m.sin(m.radians(a1dh + 11.3))
		xL1dh = x0h + (Window.size[0] / 400) * 25 * m.cos(m.radians(a1dh - 11.3))
		yL1dh = y0 + (Window.size[1] / 700) * 25 * m.sin(m.radians(a1dh - 11.3))

		xL2uh = x0h + (Window.size[0] / 400) * 25 * m.cos(m.radians(a2dh + 11.3))
		yL2uh = y0 + (Window.size[1] / 700) * 25 * m.sin(m.radians(a2dh + 11.3))
		xL2dh = x0h + (Window.size[0] / 400) * 25 * m.cos(m.radians(a2dh - 11.3))
		yL2dh = y0 + (Window.size[1] / 700) * 25 * m.sin(m.radians(a2dh - 11.3))

		xR1uh = x1h - (Window.size[0] / 400) * 25 * m.cos(m.radians(b1dh + 11.3))
		yR1uh = y1 + (Window.size[1] / 700) * 25 * m.sin(m.radians(b1dh + 11.3))
		xR1dh = x1h - (Window.size[0] / 400) * 25 * m.cos(m.radians(b1dh - 11.3))
		yR1dh = y1 + (Window.size[1] / 700) * 25 * m.sin(m.radians(b1dh - 11.3))

		xR2uh = x1h + (Window.size[0] / 400) * 25 * m.cos(m.radians(b2dh + 11.3))
		yR2uh = y1 + (Window.size[1] / 700) * 25 * m.sin(m.radians(b2dh + 11.3))
		xR2dh = x1h + (Window.size[0] / 400) * 25 * m.cos(m.radians(b2dh - 11.3))
		yR2dh = y1 + (Window.size[1] / 700) * 25 * m.sin(m.radians(b2dh - 11.3))


		#########    TIP    ##########
		Vth1t = a * (rt / rm) ** n - b * (rm / rt)
		Vth2t = a * (rt / rm) ** n + b * (rm / rt)
		Vx1t = m.sqrt(abs(Vx ** 2 - 2 * a * (np.log(rt / rm) - b * ((rm / rt) - 1))))
		Vx2t = m.sqrt(abs(Vx ** 2 - 2 * a * (np.log(rt / rm) + b * ((rm / rt) - 1))))
		# Vx1t = m.sqrt(Vx ** 2 - 2 * a * (a * np.log(rt / rm) - b * ((1 / rt) - (1 / rm))))
		# Vx2t = m.sqrt(Vx ** 2 - 2 * a * (a * np.log(rt / rm) + b * ((1 / rt) - (1 / rm))))
		dVtht = Vth2t - Vth1t
		# rnet = 1 + (a / Um) * (2 * (rt / rm) ** (n - 1) - n - 1) / (n - 1)
		rnet = 1- (a/Um)*(rt/rm)**(n-1)
		fet1 = Vx1t / Ut
		fet2 = Vx2t / Ut
		pet = dVtht / Ut

		Wth1t = Vth1t - Ut
		Wth2t = Vth2t - Ut

		a1et = -np.degrees(np.arctan(Vth1t / Vx1t))
		a2et = np.degrees(np.arctan(Vth2t / Vx2t))
		b1et = -np.degrees(np.arctan(Wth1t / Vx1t))
		b2et = np.degrees(np.arctan(Wth2t / Vx2t))

		# a1et = - np.degrees(np.arctan(-((pet / 2) - 1 + rnet) / fet1))
		# a2et = np.degrees(np.arctan(((pet / 2) + 1 - rnet) / fet2))
		# b1et = np.degrees(np.arctan(((pet / 2) + rnet) / fet1))
		# b2et = - np.degrees(np.arctan(-((pet / 2) - rnet) / fet2))

		V1t = Vx1t / m.cos(m.radians(float(a1et)))
		V2t = Vx2t / m.cos(m.radians(float(a2et)))
		W1t = Vx1t / m.cos(m.radians(float(b1et)))
		W2t = Vx2t / m.cos(m.radians(float(b2et)))

		# Wth1t = -W1t * m.sin(m.radians(float(b1et)))
		# Wth2t = W2t * m.sin(m.radians(float(b2et)))

		#############     Tip Triangles Drwaing       ############

		Utp = (Ut / Um) * U
		difT = U - Utp
		x0t = x0 + difT / 2
		x1t = x1 - difT / 2

		xLt = x1t - Utp * float(rnet) - Utp * float(pet) / 2
		yLt = y0 + Utp * float(fet1)
		xRt = x1t - Utp * float(rnet) + Utp * float(pet) / 2
		yRt = y0 + Utp * float(fet2)

		while xRt > self.width - Window.size[0] * 80 / 400 or xLt < self.x + Window.size[0] * 80 / 400\
			or yLt > Window.size[1]*200/700 or yRt > Window.size[1]*200/700\
			or xLt > self.width - Window.size[0] * 80 / 400 or xRt < self.x + Window.size[0] * 80 / 400:
			x0t = x0t + 1
			x1t = x1t - 1
			Utp = x1t - x0t

			xLt = x1t - Utp * float(rnet) - Utp * float(pet) / 2
			yLt = y0 + Utp * float(fet1)
			xRt = x1t - Utp * float(rnet) + Utp * float(pet) / 2
			yRt = y0 + Utp * float(fet2)

		a1dt = 180 + float(a1et) - 90
		a2dt = 180 - float(a2et) - 90
		b1dt = 180 - float(b1et) - 90
		b2dt = 180 - float(b2et) - 90

		# y0_2  = y0 + Window.size[1] * 150 / 700
		# yLh_2 = y0_2 - Uhp * float(feh1)
		# yRh_2 = y0_2 - Uhp * float(feh2)
		# self.manager.get_screen('comp_sc').y0_2Text = str(round(y0_2, 3))
		# self.manager.get_screen('comp_sc').yLh_2Text = str(round(yLh_2, 3))
		# self.manager.get_screen('comp_sc').yRh_2Text = str(round(yRh_2, 3))


		############### Computing rotating arrow points  ############################

		xL1ut = x0t + (Window.size[0] / 400) * 25 * m.cos(m.radians(a1dt + 11.3))
		yL1ut = y0 + (Window.size[1] / 700) * 25 * m.sin(m.radians(a1dt + 11.3))
		xL1dt = x0t + (Window.size[0] / 400) * 25 * m.cos(m.radians(a1dt - 11.3))
		yL1dt = y0 + (Window.size[1] / 700) * 25 * m.sin(m.radians(a1dt - 11.3))

		xL2ut = x0t + (Window.size[0] / 400) * 25 * m.cos(m.radians(a2dt + 11.3))
		yL2ut = y0 + (Window.size[1] / 700) * 25 * m.sin(m.radians(a2dt + 11.3))
		xL2dt = x0t + (Window.size[0] / 400) * 25 * m.cos(m.radians(a2dt - 11.3))
		yL2dt = y0 + (Window.size[1] / 700) * 25 * m.sin(m.radians(a2dt - 11.3))

		xR1ut = x1t - (Window.size[0] / 400) * 25 * m.cos(m.radians(b1dt + 11.3))
		yR1ut = y1 + (Window.size[1] / 700) * 25 * m.sin(m.radians(b1dt + 11.3))
		xR1dt = x1t - (Window.size[0] / 400) * 25 * m.cos(m.radians(b1dt - 11.3))
		yR1dt = y1 + (Window.size[1] / 700) * 25 * m.sin(m.radians(b1dt - 11.3))

		xR2ut = x1t + (Window.size[0] / 400) * 25 * m.cos(m.radians(b2dt + 11.3))
		yR2ut = y1 + (Window.size[1] / 700) * 25 * m.sin(m.radians(b2dt + 11.3))
		xR2dt = x1t + (Window.size[0] / 400) * 25 * m.cos(m.radians(b2dt - 11.3))
		yR2dt = y1 + (Window.size[1] / 700) * 25 * m.sin(m.radians(b2dt - 11.3))

		############### Passing Hub Results #################
		self.manager.get_screen('hub_sc').phText = str(round(peh, 3))
		self.manager.get_screen('hub_sc').fh1Text = str(round(feh1, 3))
		self.manager.get_screen('hub_sc').fh2Text = str(round(feh2, 3))
		self.manager.get_screen('hub_sc').rnhText = str(round(rneh, 3))
		self.manager.get_screen('hub_sc').a1hText = str(round(a1eh, 3))
		self.manager.get_screen('hub_sc').a2hText = str(round(a2eh, 3))
		self.manager.get_screen('hub_sc').b1hText = str(round(b1eh, 3))
		self.manager.get_screen('hub_sc').b2hText = str(round(b2eh, 3))

		self.manager.get_screen('hub_sc').UhText = str(round(Uh, 3))
		self.manager.get_screen('hub_sc').Vx1hText = str(round(Vx1h, 3))
		self.manager.get_screen('hub_sc').Vx2hText = str(round(Vx2h, 3))
		self.manager.get_screen('hub_sc').V1hText = str(round(V1h, 3))
		self.manager.get_screen('hub_sc').V2hText = str(round(V2h, 3))
		self.manager.get_screen('hub_sc').W1hText = str(round(W1h, 3))
		self.manager.get_screen('hub_sc').W2hText = str(round(W2h, 3))
		self.manager.get_screen('hub_sc').DVthhText = str(round(dVthh, 3))
		self.manager.get_screen('hub_sc').Vth1hText = str(round(Vth1h, 3))
		self.manager.get_screen('hub_sc').Vth2hText = str(round(Vth2h, 3))
		self.manager.get_screen('hub_sc').Wth1hText = str(round(Wth1h, 3))
		self.manager.get_screen('hub_sc').Wth2hText = str(round(Wth2h, 3))

		####### Hub drawing variables #####
		self.manager.get_screen('hub_sc').x0hText = str(x0h)
		self.manager.get_screen('hub_sc').x1hText = str(x1h)
		self.manager.get_screen('hub_sc').UhpText = str(Uhp)
		self.manager.get_screen('hub_sc').xLhText = str(xLh)
		self.manager.get_screen('hub_sc').yLhText = str(yLh)
		self.manager.get_screen('hub_sc').xRhText = str(xRh)
		self.manager.get_screen('hub_sc').yRhText = str(yRh)

		#################    Hub  Arrows      ###############
		self.manager.get_screen('hub_sc').xL1uhText = str(xL1uh)
		self.manager.get_screen('hub_sc').yL1uhText = str(yL1uh)
		self.manager.get_screen('hub_sc').xL1dhText = str(xL1dh)
		self.manager.get_screen('hub_sc').yL1dhText = str(yL1dh)

		self.manager.get_screen('hub_sc').xL2uhText = str(xL2uh)
		self.manager.get_screen('hub_sc').yL2uhText = str(yL2uh)
		self.manager.get_screen('hub_sc').xL2dhText = str(xL2dh)
		self.manager.get_screen('hub_sc').yL2dhText = str(yL2dh)

		self.manager.get_screen('hub_sc').xR1uhText = str(xR1uh)
		self.manager.get_screen('hub_sc').yR1uhText = str(yR1uh)
		self.manager.get_screen('hub_sc').xR1dhText = str(xR1dh)
		self.manager.get_screen('hub_sc').yR1dhText = str(yR1dh)

		self.manager.get_screen('hub_sc').xR2uhText = str(xR2uh)
		self.manager.get_screen('hub_sc').yR2uhText = str(yR2uh)
		self.manager.get_screen('hub_sc').xR2dhText = str(xR2dh)
		self.manager.get_screen('hub_sc').yR2dhText = str(yR2dh)


		####### Hub drawing variables #####
		self.manager.get_screen('comp_sc').x0hText = str(x0h)
		self.manager.get_screen('comp_sc').x1hText = str(x1h)
		self.manager.get_screen('comp_sc').UhpText = str(Uhp)
		self.manager.get_screen('comp_sc').xLhText = str(xLh)
		self.manager.get_screen('comp_sc').yLhText = str(yLh)
		self.manager.get_screen('comp_sc').xRhText = str(xRh)
		self.manager.get_screen('comp_sc').yRhText = str(yRh)

		#################    Hub  Arrows      ###############
		self.manager.get_screen('comp_sc').xL1uhText = str(xL1uh)
		self.manager.get_screen('comp_sc').yL1uhText = str(yL1uh)
		self.manager.get_screen('comp_sc').xL1dhText = str(xL1dh)
		self.manager.get_screen('comp_sc').yL1dhText = str(yL1dh)

		self.manager.get_screen('comp_sc').xL2uhText = str(xL2uh)
		self.manager.get_screen('comp_sc').yL2uhText = str(yL2uh)
		self.manager.get_screen('comp_sc').xL2dhText = str(xL2dh)
		self.manager.get_screen('comp_sc').yL2dhText = str(yL2dh)

		self.manager.get_screen('comp_sc').xR1uhText = str(xR1uh)
		self.manager.get_screen('comp_sc').yR1uhText = str(yR1uh)
		self.manager.get_screen('comp_sc').xR1dhText = str(xR1dh)
		self.manager.get_screen('comp_sc').yR1dhText = str(yR1dh)

		self.manager.get_screen('comp_sc').xR2uhText = str(xR2uh)
		self.manager.get_screen('comp_sc').yR2uhText = str(yR2uh)
		self.manager.get_screen('comp_sc').xR2dhText = str(xR2dh)
		self.manager.get_screen('comp_sc').yR2dhText = str(yR2dh)
		

		############### Passing Tip Results #################
		self.manager.get_screen('tip_sc').ptText = str(round(pet, 3))
		self.manager.get_screen('tip_sc').ft1Text = str(round(fet1, 3))
		self.manager.get_screen('tip_sc').ft2Text = str(round(fet2, 3))
		self.manager.get_screen('tip_sc').rntText = str(round(rnet, 3))
		self.manager.get_screen('tip_sc').a1tText = str(round(a1et, 3))
		self.manager.get_screen('tip_sc').a2tText = str(round(a2et, 3))
		self.manager.get_screen('tip_sc').b1tText = str(round(b1et, 3))
		self.manager.get_screen('tip_sc').b2tText = str(round(b2et, 3))

		self.manager.get_screen('tip_sc').UtText = str(round(Ut, 3))
		self.manager.get_screen('tip_sc').Vx1tText = str(round(Vx1t, 3))
		self.manager.get_screen('tip_sc').Vx2tText = str(round(Vx2t, 3))
		self.manager.get_screen('tip_sc').V1tText = str(round(V1t, 3))
		self.manager.get_screen('tip_sc').V2tText = str(round(V2t, 3))
		self.manager.get_screen('tip_sc').W1tText = str(round(W1t, 3))
		self.manager.get_screen('tip_sc').W2tText = str(round(W2t, 3))
		self.manager.get_screen('tip_sc').DVthtText = str(round(dVtht, 3))
		self.manager.get_screen('tip_sc').Vth1tText = str(round(Vth1t, 3))
		self.manager.get_screen('tip_sc').Vth2tText = str(round(Vth2t, 3))
		self.manager.get_screen('tip_sc').Wth1tText = str(round(Wth1t, 3))
		self.manager.get_screen('tip_sc').Wth2tText = str(round(Wth2t, 3))
		
		##########   Drawing variables   ##########
		self.manager.get_screen('tip_sc').x0tText = str(x0t)
		self.manager.get_screen('tip_sc').x1tText = str(x1t)
		self.manager.get_screen('tip_sc').UtpText = str(Utp)
		self.manager.get_screen('tip_sc').xLtText = str(xLt)
		self.manager.get_screen('tip_sc').yLtText = str(yLt)
		self.manager.get_screen('tip_sc').xRtText = str(xRt)
		self.manager.get_screen('tip_sc').yRtText = str(yRt)

		#################    Tip Arrows      ###############
		self.manager.get_screen('tip_sc').xL1utText = str(xL1ut)
		self.manager.get_screen('tip_sc').yL1utText = str(yL1ut)
		self.manager.get_screen('tip_sc').xL1dtText = str(xL1dt)
		self.manager.get_screen('tip_sc').yL1dtText = str(yL1dt)

		self.manager.get_screen('tip_sc').xL2utText = str(xL2ut)
		self.manager.get_screen('tip_sc').yL2utText = str(yL2ut)
		self.manager.get_screen('tip_sc').xL2dtText = str(xL2dt)
		self.manager.get_screen('tip_sc').yL2dtText = str(yL2dt)

		self.manager.get_screen('tip_sc').xR1utText = str(xR1ut)
		self.manager.get_screen('tip_sc').yR1utText = str(yR1ut)
		self.manager.get_screen('tip_sc').xR1dtText = str(xR1dt)
		self.manager.get_screen('tip_sc').yR1dtText = str(yR1dt)

		self.manager.get_screen('tip_sc').xR2utText = str(xR2ut)
		self.manager.get_screen('tip_sc').yR2utText = str(yR2ut)
		self.manager.get_screen('tip_sc').xR2dtText = str(xR2dt)
		self.manager.get_screen('tip_sc').yR2dtText = str(yR2dt)

		##########   Drawing variables   ##########
		self.manager.get_screen('comp_sc').x0tText = str(x0t)
		self.manager.get_screen('comp_sc').x1tText = str(x1t)
		self.manager.get_screen('comp_sc').UtpText = str(Utp)
		self.manager.get_screen('comp_sc').xLtText = str(xLt)
		self.manager.get_screen('comp_sc').yLtText = str(yLt)
		self.manager.get_screen('comp_sc').xRtText = str(xRt)
		self.manager.get_screen('comp_sc').yRtText = str(yRt)

		#################    Tip Arrows      ###############
		self.manager.get_screen('comp_sc').xL1utText = str(xL1ut)
		self.manager.get_screen('comp_sc').yL1utText = str(yL1ut)
		self.manager.get_screen('comp_sc').xL1dtText = str(xL1dt)
		self.manager.get_screen('comp_sc').yL1dtText = str(yL1dt)

		self.manager.get_screen('comp_sc').xL2utText = str(xL2ut)
		self.manager.get_screen('comp_sc').yL2utText = str(yL2ut)
		self.manager.get_screen('comp_sc').xL2dtText = str(xL2dt)
		self.manager.get_screen('comp_sc').yL2dtText = str(yL2dt)

		self.manager.get_screen('comp_sc').xR1utText = str(xR1ut)
		self.manager.get_screen('comp_sc').yR1utText = str(yR1ut)
		self.manager.get_screen('comp_sc').xR1dtText = str(xR1dt)
		self.manager.get_screen('comp_sc').yR1dtText = str(yR1dt)

		self.manager.get_screen('comp_sc').xR2utText = str(xR2ut)
		self.manager.get_screen('comp_sc').yR2utText = str(yR2ut)
		self.manager.get_screen('comp_sc').xR2dtText = str(xR2dt)
		self.manager.get_screen('comp_sc').yR2dtText = str(yR2dt)
		
		

class NewWindow(Screen):

	DPI = Metrics.dpi/96
	check = NumericProperty(0)

class SimWindow(Screen):
	DPI = Metrics.dpi / 96
	
	check = NumericProperty(0)

	tc_namemText = StringProperty('0')
	ptnm_xText = StringProperty('0')

	pText = StringProperty('0')
	fText = StringProperty('0')
	rnText = StringProperty('0')
	a1Text = StringProperty('0')
	a2Text = StringProperty('0')
	a3Text = StringProperty('0')
	b1Text = StringProperty('0')
	b2Text = StringProperty('0')
	b3Text = StringProperty('0')

	x0Text = StringProperty('0')
	y0Text = StringProperty('0')
	x1Text = StringProperty('0')
	y1Text = StringProperty('0')
	UText = StringProperty('0')
	xLText = StringProperty('0')
	yLText = StringProperty('0')
	xRText = StringProperty('0')
	yRText = StringProperty('0')

	UmText = StringProperty('1')
	VxText = StringProperty('0')
	V1Text = StringProperty('0')
	V2Text = StringProperty('0')
	W1Text = StringProperty('0')
	W2Text = StringProperty('0')
	DVthText = StringProperty('0')
	Vth1Text = StringProperty('0')
	Vth2Text = StringProperty('0')
	Wth1Text = StringProperty('0')
	Wth2Text = StringProperty('0')

	xL1uText = StringProperty('0')
	yL1uText = StringProperty('0')
	xL1dText = StringProperty('0')
	yL1dText = StringProperty('0')

	xL2uText = StringProperty('0')
	yL2uText = StringProperty('0')
	xL2dText = StringProperty('0')
	yL2dText = StringProperty('0')

	xR1uText = StringProperty('0')
	yR1uText = StringProperty('0')
	xR1dText = StringProperty('0')
	yR1dText = StringProperty('0')

	xR2uText = StringProperty('0')
	yR2uText = StringProperty('0')
	xR2dText = StringProperty('0')
	yR2dText = StringProperty('0')

class MidScreen(Screen):
	check = NumericProperty(0)

	tc_namemText = StringProperty('0')
	ptnm_xText = StringProperty('0')
	XText = StringProperty('0')
	pText = StringProperty('0')
	fText = StringProperty('0')
	rnText = StringProperty('0')
	a1Text = StringProperty('0')
	a2Text = StringProperty('0')
	a3Text = StringProperty('0')
	b1Text = StringProperty('0')
	b2Text = StringProperty('0')
	b3Text = StringProperty('0')

	x0Text = StringProperty('0')
	y0Text = StringProperty('0')
	x1Text = StringProperty('0')
	y1Text = StringProperty('0')
	UText = StringProperty('0')
	xLText = StringProperty('0')
	yLText = StringProperty('0')
	xRText = StringProperty('0')
	yRText = StringProperty('0')

	UmText = StringProperty('0')
	UtText = StringProperty('0')
	UhText = StringProperty('0')
	VxText = StringProperty('0')
	V1Text = StringProperty('0')
	V2Text = StringProperty('0')
	W1Text = StringProperty('0')
	W2Text = StringProperty('0')
	DVthText = StringProperty('0')
	Vth1Text = StringProperty('0')
	Vth2Text = StringProperty('0')
	Wth1Text = StringProperty('0')
	Wth2Text = StringProperty('0')

	xL1uText = StringProperty('0')
	yL1uText = StringProperty('0')
	xL1dText = StringProperty('0')
	yL1dText = StringProperty('0')

	xL2uText = StringProperty('0')
	yL2uText = StringProperty('0')
	xL2dText = StringProperty('0')
	yL2dText = StringProperty('0')

	xR1uText = StringProperty('0')
	yR1uText = StringProperty('0')
	xR1dText = StringProperty('0')
	yR1dText = StringProperty('0')

	xR2uText = StringProperty('0')
	yR2uText = StringProperty('0')
	xR2dText = StringProperty('0')
	yR2dText = StringProperty('0')

	tc_namemText = StringProperty('0')
	ptnm_xText = StringProperty('0')


class HubScreen(Screen):
	check = NumericProperty(0)

	tc_namemText = StringProperty('0')
	ptnm_xText = StringProperty('0')

	phText = StringProperty('0')
	fh1Text = StringProperty('0')
	fh2Text = StringProperty('0')
	rnhText = StringProperty('0')
	a1hText = StringProperty('0')
	a2hText = StringProperty('0')
	b1hText = StringProperty('0')
	b2hText = StringProperty('0')

	UhText = StringProperty('0')
	UmText = StringProperty('1')
	Vx1hText = StringProperty('0')
	Vx2hText = StringProperty('0')
	V1hText = StringProperty('0')
	V2hText = StringProperty('0')
	W1hText = StringProperty('0')
	W2hText = StringProperty('0')
	DVthhText = StringProperty('0')
	Vth1hText = StringProperty('0')
	Vth2hText = StringProperty('0')
	Wth1hText = StringProperty('0')
	Wth2hText = StringProperty('0')

	y0Text = StringProperty('0')
	y1Text = StringProperty('0')
	x0hText = StringProperty('0')
	x1hText = StringProperty('0')
	UhpText = StringProperty('0')
	UText = StringProperty('0')
	xLhText = StringProperty('0')
	yLhText = StringProperty('0')
	xRhText = StringProperty('0')
	yRhText = StringProperty('0')

	xL1uhText = StringProperty('0')
	yL1uhText = StringProperty('0')
	xL1dhText = StringProperty('0')
	yL1dhText = StringProperty('0')

	xL2uhText = StringProperty('0')
	yL2uhText = StringProperty('0')
	xL2dhText = StringProperty('0')
	yL2dhText = StringProperty('0')

	xR1uhText = StringProperty('0')
	yR1uhText = StringProperty('0')
	xR1dhText = StringProperty('0')
	yR1dhText = StringProperty('0')

	xR2uhText = StringProperty('0')
	yR2uhText = StringProperty('0')
	xR2dhText = StringProperty('0')
	yR2dhText = StringProperty('0')

	tc_namehText = StringProperty('0')
	ptnh_xText = StringProperty('0')



class TipScreen(Screen):
	check = NumericProperty(0)

	tc_namemText = StringProperty('0')
	ptnm_xText = StringProperty('0')

	ptText = StringProperty('0')
	ft1Text = StringProperty('0')
	ft2Text = StringProperty('0')
	rntText = StringProperty('0')
	a1tText = StringProperty('0')
	a2tText = StringProperty('0')
	b1tText = StringProperty('0')
	b2tText = StringProperty('0')

	UtText = StringProperty('0')
	UmText = StringProperty('1')
	Vx1tText = StringProperty('0')
	Vx2tText = StringProperty('0')
	V1tText = StringProperty('0')
	V2tText = StringProperty('0')
	W1tText = StringProperty('0')
	W2tText = StringProperty('0')
	DVthtText = StringProperty('0')
	Vth1tText = StringProperty('0')
	Vth2tText = StringProperty('0')
	Wth1tText = StringProperty('0')
	Wth2tText = StringProperty('0')

	y0Text = StringProperty('0')
	y1Text = StringProperty('0')
	x0tText = StringProperty('0')
	x1tText = StringProperty('0')
	UtpText = StringProperty('0')
	UText = StringProperty('0')
	xLtText = StringProperty('0')
	yLtText = StringProperty('0')
	xRtText = StringProperty('0')
	yRtText = StringProperty('0')

	xL1utText = StringProperty('0')
	yL1utText = StringProperty('0')
	xL1dtText = StringProperty('0')
	yL1dtText = StringProperty('0')

	xL2utText = StringProperty('0')
	yL2utText = StringProperty('0')
	xL2dtText = StringProperty('0')
	yL2dtText = StringProperty('0')

	xR1utText = StringProperty('0')
	yR1utText = StringProperty('0')
	xR1dtText = StringProperty('0')
	yR1dtText = StringProperty('0')

	xR2utText = StringProperty('0')
	yR2utText = StringProperty('0')
	xR2dtText = StringProperty('0')
	yR2dtText = StringProperty('0')

	tc_nametText = StringProperty('0')
	ptnt_xText = StringProperty('0')

class CompScreen(Screen):

	# y0_2Text = StringProperty('0')
	# yLh_2Text = StringProperty('0')
	# yRh_2Text = StringProperty('0')

	####### MID #########

	x0Text = StringProperty('0')
	y0Text = StringProperty('0')
	x1Text = StringProperty('0')
	y1Text = StringProperty('0')
	UText = StringProperty('0')
	xLText = StringProperty('0')
	yLText = StringProperty('0')
	xRText = StringProperty('0')
	yRText = StringProperty('0')

	xL1uText = StringProperty('0')
	yL1uText = StringProperty('0')
	xL1dText = StringProperty('0')
	yL1dText = StringProperty('0')

	xL2uText = StringProperty('0')
	yL2uText = StringProperty('0')
	xL2dText = StringProperty('0')
	yL2dText = StringProperty('0')

	xR1uText = StringProperty('0')
	yR1uText = StringProperty('0')
	xR1dText = StringProperty('0')
	yR1dText = StringProperty('0')

	xR2uText = StringProperty('0')
	yR2uText = StringProperty('0')
	xR2dText = StringProperty('0')
	yR2dText = StringProperty('0')

	###### HUB  #####
	x0hText = StringProperty('0')
	x1hText = StringProperty('0')
	UhpText = StringProperty('0')
	xLhText = StringProperty('0')
	yLhText = StringProperty('0')
	xRhText = StringProperty('0')
	yRhText = StringProperty('0')

	xL1uhText = StringProperty('0')
	yL1uhText = StringProperty('0')
	xL1dhText = StringProperty('0')
	yL1dhText = StringProperty('0')

	xL2uhText = StringProperty('0')
	yL2uhText = StringProperty('0')
	xL2dhText = StringProperty('0')
	yL2dhText = StringProperty('0')

	xR1uhText = StringProperty('0')
	yR1uhText = StringProperty('0')
	xR1dhText = StringProperty('0')
	yR1dhText = StringProperty('0')

	xR2uhText = StringProperty('0')
	yR2uhText = StringProperty('0')
	xR2dhText = StringProperty('0')
	yR2dhText = StringProperty('0')

	######## TIP #######
	x0tText = StringProperty('0')
	x1tText = StringProperty('0')
	UtpText = StringProperty('0')
	xLtText = StringProperty('0')
	yLtText = StringProperty('0')
	xRtText = StringProperty('0')
	yRtText = StringProperty('0')

	xL1utText = StringProperty('0')
	yL1utText = StringProperty('0')
	xL1dtText = StringProperty('0')
	yL1dtText = StringProperty('0')

	xL2utText = StringProperty('0')
	yL2utText = StringProperty('0')
	xL2dtText = StringProperty('0')
	yL2dtText = StringProperty('0')

	xR1utText = StringProperty('0')
	yR1utText = StringProperty('0')
	xR1dtText = StringProperty('0')
	yR1dtText = StringProperty('0')

	xR2utText = StringProperty('0')
	yR2utText = StringProperty('0')
	xR2dtText = StringProperty('0')
	yR2dtText = StringProperty('0')

	tc_namemText = StringProperty('0')
	ptnm_xText = StringProperty('0')

	pass

class InfoScreen(Screen):
	pass

class WindowManager(ScreenManager):
	pass

class MainApp(MDApp):
	def __init__(self, **kwargs):
		self.title = "VTA"
		self.theme_cls.theme_style = "Light"
		self.theme_cls.primary_palette = "DeepOrange"
		self.theme_cls.secondary_palette = "Black"
		super().__init__(**kwargs)

MainApp().run()



