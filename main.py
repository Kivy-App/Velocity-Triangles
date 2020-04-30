from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import StringProperty
import math as m
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.metrics import Metrics
import numpy as np
from scipy.optimize import fsolve
from kivy.uix.bubble import Bubble



class P(BoxLayout):
	pass

def firstPopup():
	show = P()
	# create content for the Popup
	bl = BoxLayout(orientation='vertical',padding = 30)
	label = Label(text = ' You should not put less than 3 \n variables at the first segment',halign = 'center',valign = 'middle', color =[1, 0, 0, 1],font_size = '18dp')

	bl.add_widget(label)
	popupWindow = Popup(title=" Error ", content=bl, size_hint=(None, None), size=('350dp' ,'350dp'))
	bl.add_widget(Button(text='OK got it !!!', size_hint=(0.7,0.3), pos_hint={'x': 0.01,'y':1.2}, on_release = popupWindow.dismiss))
	popupWindow.open()

class P2(BoxLayout):
	pass

def secondPopup():
	show = P2()
	# create content for the Popup
	bl = BoxLayout(orientation='vertical',padding = 30)
	label = Label(text = ' This combination of variables \n'
						 ' is not valid. It seems that with\n'
						 ' this combination of variables \n'
						 ' Loading coefficient \u03C8 or \n'
						 ' Flow Coefficient \u03C6 tends to infinity.\n'
						 ' Please try again with new varieables.',halign = 'center',valign = 'middle', color =[1, 0, 0, 1],font_size = '18dp')

	bl.add_widget(label)
	popupWindow = Popup(title=" Error ", content=bl, size_hint=(None, None), size=('350dp' ,'350dp'))
	bl.add_widget(Button(text='OK got it !!!', size_hint=(0.7,0.3), pos_hint={'x': 0.01,'y':1.2}, on_release = popupWindow.dismiss))
	popupWindow.open()

class P3(BoxLayout):
	pass

def thirdPopup():
	show = P3()
	# create content for the Popup
	bl = BoxLayout(orientation='vertical',padding = 30)
	label = Label(text = ' Dimensional measurements missing.\n Please fill all the \n required measurements ',halign = 'center',valign = 'middle', color =[1, 0, 0, 1],font_size = '18dp')

	bl.add_widget(label)
	popupWindow = Popup(title=" Error ", content=bl, size_hint=(None, None), size=('350dp' ,'350dp'))
	bl.add_widget(Button(text='OK got it !!!', size_hint=(0.7,0.3), pos_hint={'x': 0.01,'y':1.2}, on_release = popupWindow.dismiss))
	popupWindow.open()

class P4(BoxLayout):
	pass

def fourthPopup():
	show = P3()
	# create content for the Popup
	bl = BoxLayout(orientation='vertical',padding = 30)
	label = Label(text = ' You should not put more than 3 \n variables at the first segment',halign = 'center',valign = 'middle', color =[1, 0, 0, 1],font_size = '18dp')

	bl.add_widget(label)
	popupWindow = Popup(title=" Error ", content=bl, size_hint=(None, None), size=('350dp' ,'350dp'))
	bl.add_widget(Button(text='OK got it !!!', size_hint=(0.7,0.3), pos_hint={'x': 0.01,'y':1.2}, on_release = popupWindow.dismiss))
	popupWindow.open()

class VelocityTriangles(Screen):
	########## Window properties #########
	Config.set('graphics', 'resizable', True)
	Window.size = (400, 700)
	# Window.Keyboard_anim_args = {'d':.2 , "t": in_out_expo}
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

	n = ObjectProperty(None)
	l = NumericProperty(0)
	k =  NumericProperty(0) #### Debugging tool for less than 3 variables and for not changing window ######
	t = NumericProperty(0) ##### Debugging tool for more than 3 variables ####
	bbl = NumericProperty(0) ##### Bubble Variable #####


############ Debuging for smaller screens #################
	if Window.size[0] > 800 and Window.size[0] < 1000:
		l = 10 / 11
	else:
		l = 1

	DPI = Metrics.dpi/96

############ Function of creating info bubble ############
	def showbubble(self):
		self.bbl += 1
		global bubb
		bubb = Bubble(orientation='vertical', size_hint=(0.98, 0.27), arrow_pos='top_right',
						  pos_hint={'x': 0.01, 'y': 0.65}, background_color = (1, 0, 0, 1))
		l = Label(text=' This application was created to extract an easy and fast velocity \n'
					   ' analysis for one stage of a turbomachine. It can analize the \n'
					   ' velocities of both compressor and turbine and it is divided into 2 \n'
					   ' compartments. The first compartment extracts the non dimensional\n'
					   ' velocity charts through input of coefficients and angles. To achieve\n'
					   ' the non dimensional analysis you should complete 3 off the first \n'
					   ' segments inputs. The second compartment extracts the dimensional\n'
					   ' analysis. At the second compartment you should fill all the enabled\n'
					   ' input slots. Note that the first compartments can work without\n'
					   ' filling the second but it doesnt work the other way around.\n'
					   ' [color=ff3333][b] To dismiss info panel press the info button once more. [/b][/color]'
				  , markup = True
				  ,halign='left', valign='top'
				  ,color=[1,1,1,1], font_size='12dp')
		bubb.add_widget(l)
		self.add_widget(bubb)

############ Function of destroying info bubble ############
	def destroybubble(self):
		self.remove_widget(bubb)
		self.bbl += 1

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

			X = []

			self.k = 0

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

			self.k = len(X)
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

			if self.p.text == '':
				pe = str(round(r[j], 3))
				j = j + 1
			if self.f.text == '':
				fe = str(round(r[j], 3))
				j = j + 1
			if self.rn.text == '':
				rne = str(round(r[j], 3))
				j = j + 1
			if self.a1.text == '':
				a1e = str(round(r[j], 3))
				j = j + 1
			if self.a2.text == '':
				a2e = str(round(r[j], 3))
				j = j + 1
			if self.b1.text == '':
				b1e = str(round(r[j], 3))
				j = j + 1
			if self.b2.text == '':
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

			############################# Drawing Triangles ######################################
			x0,y0 = Window.size[0]*130/400,Window.size[1]*80/700
			x1,y1 = Window.size[0]*270/400,Window.size[1]*80/700
			# x0, y0 = self.width/2 - 100, Window.size[1] * 150 / 700
			# x1, y1 = self.width/2 + 100, Window.size[1] * 150 / 700
			U = x1-x0
			xL = x1 - U*float(rne)-U*float(pe)/2
			yL = y0 + U*float(fe)
			xR = x1 - U*float(rne) +U*float(pe)/2
			yR = y0 + U*float(fe)

	######### While functions for triangles fitting #########
			while xL < self.x + 60:
				x0 = x0 + 1
				x1 = x1 - 1

				U = x1 - x0
				xL = x1 - U * float(rne) - U * float(pe) / 2
				yL = y0 + U * float(fe)
				xR = x1 - U * float(rne) + U * float(pe) / 2
				yR = y0 + U * float(fe)

			while xR < self.x + 60:
				x0 = x0 + 1
				x1 = x1 - 1

				U = x1 - x0
				xL = x1 - U * float(rne) - U * float(pe) / 2
				yL = y0 + U * float(fe)
				xR = x1 - U * float(rne) + U * float(pe) / 2
				yR = y0 + U * float(fe)

			while xR > self.width - 80:
				x0 = x0 + 1
				x1 = x1 - 1

				U = x1 - x0
				xL = x1 - U * float(rne) - U * float(pe) / 2
				yL = y0 + U * float(fe)
				xR = x1 - U * float(rne) + U * float(pe) / 2
				yR = y0 + U * float(fe)

			while xL > self.width - 80:
				x0 = x0 + 1
				x1 = x1 - 1

				U = x1 - x0
				xL = x1 - U * float(rne) - U * float(pe) / 2
				yL = y0 + U * float(fe)
				xR = x1 - U * float(rne) + U * float(pe) / 2
				yR = y0 + U * float(fe)

			while yL > self.height*0.4:
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

			############### Passing the Results on the Second Screen  ############################
			self.manager.get_screen('new').pText = pe
			self.manager.get_screen('new').fText = fe
			self.manager.get_screen('new').rnText = rne
			self.manager.get_screen('new').a1Text = a1e
			self.manager.get_screen('new').a2Text = a2e
			self.manager.get_screen('new').a3Text = a3e
			self.manager.get_screen('new').b1Text = b1e
			self.manager.get_screen('new').b2Text = b2e
			self.manager.get_screen('new').b3Text = b3e

			############### Passing the Triangles Points on the Second Screen  ##################

			self.manager.get_screen('new').x0Text = str(x0)
			self.manager.get_screen('new').y0Text = str(y0)
			self.manager.get_screen('new').x1Text = str(x1)
			self.manager.get_screen('new').y1Text = str(y1)
			self.manager.get_screen('new').UText = str(U)
			self.manager.get_screen('new').xLText = str(xL)
			self.manager.get_screen('new').yLText = str(yL)
			self.manager.get_screen('new').xRText = str(xR)
			self.manager.get_screen('new').yRText = str(yR)

			############### Passing the Arrow Points on the Second Screen  ##################
			self.manager.get_screen('new').xL1uText = str(xL1u)
			self.manager.get_screen('new').yL1uText = str(yL1u)
			self.manager.get_screen('new').xL1dText = str(xL1d)
			self.manager.get_screen('new').yL1dText = str(yL1d)

			self.manager.get_screen('new').xL2uText = str(xL2u)
			self.manager.get_screen('new').yL2uText = str(yL2u)
			self.manager.get_screen('new').xL2dText = str(xL2d)
			self.manager.get_screen('new').yL2dText = str(yL2d)

			self.manager.get_screen('new').xR1uText = str(xR1u)
			self.manager.get_screen('new').yR1uText = str(yR1u)
			self.manager.get_screen('new').xR1dText = str(xR1d)
			self.manager.get_screen('new').yR1dText = str(yR1d)

			self.manager.get_screen('new').xR2uText = str(xR2u)
			self.manager.get_screen('new').yR2uText = str(yR2u)
			self.manager.get_screen('new').xR2dText = str(xR2d)
			self.manager.get_screen('new').yR2dText = str(yR2d)

			############### Passing the compressor or turbine text and possition on the Second Screen  ##################
			self.manager.get_screen('new').tc_namemText = tc_namem
			self.manager.get_screen('new').tc_namehText = tc_nameh
			self.manager.get_screen('new').tc_nametText = tc_namet
			self.manager.get_screen('new').ptnm_xText = str(ptnm_x)
			self.manager.get_screen('new').ptnh_xText = str(ptnh_x)
			self.manager.get_screen('new').ptnt_xText = str(ptnt_x)


################ Debugging Section #################
			if self.k == 4:
				if float(b1e) - float(a1e) < 2 or float(a2e) - float(b2e) < 2:
					self.popup = secondPopup()
					self.k = 0
			if t < 4:
				self.popup = fourthPopup()
				self.k = 0

		except:
			# if self.k > 4:
		########## It goes in to except if only variables are less than 3. So if is unnecesery #########
			self.popup = firstPopup()
			self.k = 0  # mia allh timh oxi 4 gia na mhn allazei window
			# else:
			# 	self.popup = secondPopup()
			# 	self.k = 0


	def dml(self):
		try:
			D1e = str(self.d1.text)
			D2e = str(self.d2.text)
			D3e = str(self.d3.text)
			Rh1e = str(self.rh2t1.text)
			Rh2e = str(self.rh2t2.text)
			Rh3e = str(self.rh2t3.text)
			Ne = str(self.n.text)

			global rh
			global rt
			global rm
			global Um
			global Uh
			global Ut
			global Vx
			global Vth1
			global Vth2

			rt = float(D1e)/2
			rh = float(Rh1e)*float(D1e)/2
			rm = (rt+rh)/2

			Um = 0.01666666 * float(Ne) * rm

			Uh = 0.01666666 * float(Ne) * rh

			Ut = 0.01666666 * float(Ne) * rt

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
			self.manager.get_screen('new').UmText = str(round(Um, 3))
			self.manager.get_screen('new').UhText = str(round(Uh, 3))
			self.manager.get_screen('new').UtText = str(round(Ut, 3))
			self.manager.get_screen('new').VxText = str(round(Vx, 3))
			self.manager.get_screen('new').V1Text = str(round(V1, 3))
			self.manager.get_screen('new').V2Text = str(round(V2, 3))
			self.manager.get_screen('new').W1Text = str(round(W1, 3))
			self.manager.get_screen('new').W2Text = str(round(W2, 3))
			self.manager.get_screen('new').DVthText = str(round(dvth, 3))
			self.manager.get_screen('new').Vth1Text = str(round(Vth1, 3))
			self.manager.get_screen('new').Vth2Text = str(round(Vth2, 3))
			self.manager.get_screen('new').Wth1Text = str(round(Wth1, 3))
			self.manager.get_screen('new').Wth2Text = str(round(Wth2, 3))

			self.manager.get_screen('new').check = 0
		except:
			if D1e == '' and D2e == '' and D3e == '' and Rh1e == '' and Rh2e == '' and Rh3e == '' and Ne == '':
				############### Passing empty slots  on the Second Screen  ##################
				self.manager.get_screen('new').UmText = ''
				self.manager.get_screen('new').UhText = ''
				self.manager.get_screen('new').UtText = ''
				self.manager.get_screen('new').VxText = ''
				self.manager.get_screen('new').V1Text = ''
				self.manager.get_screen('new').V2Text = ''
				self.manager.get_screen('new').W1Text = ''
				self.manager.get_screen('new').W2Text = ''
				self.manager.get_screen('new').DVthText = ''
				self.manager.get_screen('new').DVthText = ''
				self.manager.get_screen('new').Vth1Text = ''
				self.manager.get_screen('new').Vth2Text = ''
				self.manager.get_screen('new').Wth1Text = ''
				self.manager.get_screen('new').Wth2Text = ''

				self.manager.get_screen('new').check = 1
			else:
				if self.k == 0:
					pass
				else:
					self.popup = thirdPopup()
					self.k = 0

	def h2t_triangles(self):
		a = Um * (1 - float(rne))
		b = Vth2 - a
		n = 0

		#########    HUB    ##########
		Vth1h = a * (rh / rm) ** n - b * (rm / rh)
		Vth2h = a * (rh / rm) ** n + b * (rm / rh)
		Vx1h = m.sqrt(abs(Vx ** 2 - 2 * a * (np.log(rh / rm) - b * ((rm / rh) - 1))))
		Vx2h = m.sqrt(abs(Vx ** 2 - 2 * a * (np.log(rh / rm) + b * ((rm / rh) - 1))))
		dVthh = Vth2h - Vth1h
		rneh = 1 + (a / Um) * (2 * (rh / rm) ** (n - 1) - n - 1) / (n - 1)
		feh1 = Vx1h / Uh
		feh2 = Vx2h / Uh
		peh = dVthh/Uh

		a1eh = - np.degrees(np.arctan(-((peh / 2) - 1 + rneh) / feh1))
		a2eh = np.degrees(np.arctan(((peh / 2) + 1 - rneh) / feh2))
		b1eh = np.degrees(np.arctan(((peh / 2) + rneh) / feh2))
		b2eh = - np.degrees(np.arctan(-((peh / 2) - rneh) / feh2))

		#########    TIP    ##########
		Vth1t = a * (rt / rm) ** n - b * (rm / rt)
		Vth2t = a * (rt / rm) ** n + b * (rm / rt)
		Vx1t = m.sqrt(abs(Vx ** 2 - 2 * a * (np.log(rt / rm) - b * ((rm / rt) - 1))))
		Vx2t = m.sqrt(abs(Vx ** 2 - 2 * a * (np.log(rt / rm) + b * ((rm / rt) - 1))))
		dVtht = Vth2t - Vth1t
		rnet = 1 + (a / Um) * (2 * (rt / rm) ** (n - 1) - n - 1) / (n - 1)
		fet1 = Vx1t / Ut
		fet2 = Vx2t / Ut
		pet = dVtht / Ut

		a1et = - np.degrees(np.arctan(-((pet / 2) - 1 + rnet) / fet1))
		a2et = np.degrees(np.arctan(((pet / 2) + 1 - rnet) / fet2))
		b1et = np.degrees(np.arctan(((pet / 2) + rnet) / fet1))
		b2et = - np.degrees(np.arctan(-((pet / 2) - rnet) / fet2))


		print("a:" ,a)
		print(b)
		print(rneh)
		print(rnet)
		print(Vx1h)
		print(Vx1t)
		print(Vth1h)
		print(Vth2h)
		print(feh1)
		print(feh2)
		print(peh)

		print(a1eh)

class NewWindow(Screen):

	DPI = Metrics.dpi/96

	pText  = StringProperty('0')
	fText  = StringProperty('0')
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
	UText  = StringProperty('0')
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



	check = NumericProperty(0)

	tc_namemText = StringProperty('0')
	tc_namehText = StringProperty('0')
	tc_nametText = StringProperty('0')
	ptnm_xText = StringProperty('0')
	ptnh_xText = StringProperty('0')
	ptnt_xText = StringProperty('0')

class WindowManager(ScreenManager):
	pass


kv = Builder.load_file("VelocityTrianglesApp.kv")

class VelocityTrianglesApp(App):
	def build(self):
		return kv

if __name__ == '__main__':
	vt = VelocityTrianglesApp()
	vt.run()