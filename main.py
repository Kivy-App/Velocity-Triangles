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
from kivy.properties import StringProperty
import math as m
import numpy as np
from scipy.optimize import fsolve
from kivy.uix.image import Image

class VelocityTriangles(Screen):

    p = ObjectProperty(None)
    f = ObjectProperty(None)
    rn = ObjectProperty(None)
    a1 = ObjectProperty(None)
    a2 = ObjectProperty(None)
    a3 = ObjectProperty(None)
    b1 = ObjectProperty(None)
    b2 = ObjectProperty(None)
    b3 = ObjectProperty(None)

    def systemsolver(self):

        pe  = str(self.p.text)
        fe  = str(self.f.text)
        rne = str(self.rn.text)
        a1e = str(self.a1.text)
        a2e = str(self.a2.text)
        a3e = str(self.a3.text)
        b1e = str(self.b1.text)
        b2e = str(self.b2.text)
        b3e = str(self.b3.text)

        if pe!='':
            pe = str(self.p.text)
        else:
            pe=str('')

        if fe!='':
            fe = str(self.f.text)
        else:
            fe = str('')

        if rne!='':
            rne = str(self.rn.text)
        else:
            rne = str('')

        if a1e!='':
            a1e = str(self.a1.text)
        else:
            a1e = str('')

        if a2e!='':
            a2e = str(self.a2.text)
        else:
            a2e = str('')

        if a3e!='':
            a3e = str(self.a3.text)
        else:
            a3e = str('')

        if b1e!='':
            b1e = str(self.b1.text)
        else:
            b1e = str('')

        if b2e!='':
            b2e = str(self.b2.text)
        else:
            b2e = str('')

        if b3e!='':
            b3e = str(self.b3.text)
        else:
            b3e = str('')


        self.manager.get_screen('new').pText = pe
        self.manager.get_screen('new').fText = fe
        self.manager.get_screen('new').rnText = rne
        self.manager.get_screen('new').a1Text = a1e
        self.manager.get_screen('new').a2Text = a2e
        self.manager.get_screen('new').a3Text = a3e
        self.manager.get_screen('new').b1Text = b1e
        self.manager.get_screen('new').b2Text = b2e
        self.manager.get_screen('new').b3Text = b3e



    def fontsize(self, text):
        if Window.size[0]>400:
            dp = 7
            for i in range(0,Window.size[0],50):
                dp = dp+1
            return "{}dp".format(dp)
        else:
            dp = 5
            for i in range(0, Window.size[0], 50):
                dp = dp + 1
            return "{}dp".format(dp)

    def fontsize2(self, text):
        if Window.size[0]>400:
            dp = 5
            for i in range(0,Window.size[0],50):
                dp = dp+1
            return "{}dp".format(dp)
        else:
            dp = 3
            for i in range(0, Window.size[0], 50):
                dp = dp + 1
            return "{}dp".format(dp)

    def fontsize3(self, text):
        if Window.size[0]>400:
            dp = 9
            for i in range(0,Window.size[0],50):
                dp = dp+1
            return "{}dp".format(dp)
        else:
            dp = 7
            for i in range(0, Window.size[0], 50):
                dp = dp + 1
            return "{}dp".format(dp)


class NewWindow(Screen):
	pText  = StringProperty('My Label')
	fText  = StringProperty('My Label')
	rnText = StringProperty('My Label')
	a1Text = StringProperty('My Label')
	a2Text = StringProperty('My Label')
	a3Text = StringProperty('My Label')
	b1Text = StringProperty('My Label')
	b2Text = StringProperty('My Label')
	b3Text = StringProperty('My Label')

class WindowManager(ScreenManager):
    pass

Config.set('graphics', 'resizable', True)
Window.size = (600, 700)

kv = Builder.load_file("VelocityTrianglesApp.kv")

class VelocityTrianglesApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
	va = VelocityTrianglesApp()
	va.run()





