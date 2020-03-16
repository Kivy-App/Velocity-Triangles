from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.graphics import Color,Rectangle
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


class VelocityTriangles(Screen):
	p= ObjectProperty(None)  
	f= ObjectProperty(None)
	Rn= ObjectProperty(None)
	a1= ObjectProperty(None)
	a2= ObjectProperty(None)
	a3= ObjectProperty(None)
	b1= ObjectProperty(None)
	b2= ObjectProperty(None)
	b3= ObjectProperty(None)
	
	def angles(self):
		
		pe = self.p.text
		s = str(pe)
		l = Label(text = s,pos_hint={"x":-0.1,"y":0.1})
		self.add_widget(l)

		# if pe != '':
		# 	pe = float(pe)
	 #    else:
	 #    	pe = ''

	 #    if fe != '':
	 #        fe = float(fe)
	 #    else:
	 #        fe = ''

	 #    if Rne != '':
	 #        Rne = float(Rne)
	 #    else:
	 #        Rne = ''

	 #    if a1e != '':
	 #        a1e = float(a1e)
	 #    else:
	 #        a1e = ''

	 #    if a2e != '':
	 #         a2e= float(a2e)
	 #    else:
	 #        a2e = ''

	 #    if b1e != '':
	 #         b1e= float(b1e)
	 #    else:
	 #        b1e = ''

	 #    if b2e != '':
	 #         b2e= float(b2e)
	 #    else:
	 #        b2e = ''



		

    

class NewWindow(Screen):
	VelocityTriangles().angles()



class WindowManager(ScreenManager):
    pass

Config.set('graphics', 'resizable', True)
Window.size = (600, 700)


kv = Builder.load_file("VelocityTrianglesApp.kv")

class VelocityTrianglesApp(App):
    def build(self):
        return kv




if __name__ == '__main__':
	VelocityTrianglesApp().run()
