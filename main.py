from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import StringProperty
import numpy as np
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class P(BoxLayout):
    pass

def firstPopup():
    show = P()
    # create content for the Popup
    bl = BoxLayout(orientation='vertical',padding = 30)
    label = Label(text = ' At least three variables \n are required for the analysis',halign = 'center',valign = 'middle', color =[1, 0, 0, 1],font_size = '18dp')

    bl.add_widget(label)
    popupWindow = Popup(title=" Error ", content=bl, size_hint=(None, None), size=('400dp' ,'400dp'))
    bl.add_widget(Button(text='OK got it !!!', size_hint=(0.7,0.3), pos_hint={'x': 0.15,'y':1.2}, on_release = popupWindow.dismiss))
    popupWindow.open()

class VelocityTriangles(Screen):

    p  = ObjectProperty(None)
    f  = ObjectProperty(None)
    rn = ObjectProperty(None)
    a1 = ObjectProperty(None)
    a2 = ObjectProperty(None)
    a3 = ObjectProperty(None)
    b1 = ObjectProperty(None)
    b2 = ObjectProperty(None)
    b3 = ObjectProperty(None)

    def systemsolver(self):
        try:
            pe  = str(self.p.text)
            fe  = str(self.f.text)
            rne = str(self.rn.text)
            a1e = str(self.a1.text)
            a2e = str(self.a2.text)
            a3e = str(self.a3.text)
            b1e = str(self.b1.text)
            b2e = str(self.b2.text)
            b3e = str(self.b3.text)

            a1e = str(round(-np.degrees(np.arctan(-((float(pe) / 2) - 1 + float(rne)) / float(fe))), 3))
            a2e = str(round(np.degrees(np.arctan(((float(pe) / 2)+1-float(rne)) / float(fe))),3))
            b1e = str(round(np.degrees(np.arctan(((float(pe) / 2) + float(rne)) / float(fe))),3))
            b2e = str(round(-np.degrees(np.arctan(-((float(pe) / 2) - float(rne)) / float(fe))),3))

            self.manager.get_screen('new').pText = pe
            self.manager.get_screen('new').fText = fe
            self.manager.get_screen('new').rnText = rne
            self.manager.get_screen('new').a1Text = a1e
            self.manager.get_screen('new').a2Text = a2e
            self.manager.get_screen('new').a3Text = a3e
            self.manager.get_screen('new').b1Text = b1e
            self.manager.get_screen('new').b2Text = b2e
            self.manager.get_screen('new').b3Text = b3e
        except:
            self.popup = firstPopup()

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
    pText  = StringProperty("0")
    fText  = StringProperty('0')
    rnText = StringProperty('0')
    a1Text = StringProperty('0')
    a2Text = StringProperty('0')
    a3Text = StringProperty('0')
    b1Text = StringProperty('0')
    b2Text = StringProperty('0')
    b3Text = StringProperty('0')

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

class WindowManager(ScreenManager):
    pass

Config.set('graphics', 'resizable', True)
Window.size = (400, 700)

kv = Builder.load_file("VelocityTrianglesApp.kv")

class VelocityTrianglesApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    va = VelocityTrianglesApp()
    va.run()