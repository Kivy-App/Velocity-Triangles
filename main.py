from kivy.app import App
from kivy.config import Config
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import StringProperty
import math as m
import numpy as np
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import sympy as sy
from kivy.uix.scrollview import ScrollView

class P(BoxLayout):
    pass



def firstPopup():
    show = P()
    # create content for the Popup
    bl = BoxLayout(orientation='vertical',padding = 30)
    label = Label(text = ' At least three variables \n are required for the analysis',halign = 'center',valign = 'middle', color =[1, 0, 0, 1],font_size = '18dp')

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
    label = Label(text = ' This combination of variables \n is not valid ',halign = 'center',valign = 'middle', color =[1, 0, 0, 1],font_size = '18dp')

    bl.add_widget(label)
    popupWindow = Popup(title=" Error ", content=bl, size_hint=(None, None), size=('350dp' ,'350dp'))
    bl.add_widget(Button(text='OK got it !!!', size_hint=(0.7,0.3), pos_hint={'x': 0.01,'y':1.2}, on_release = popupWindow.dismiss))
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

    d1 = ObjectProperty(None)
    d2 = ObjectProperty(None)
    d3 = ObjectProperty(None)
    rh2t1 = ObjectProperty(None)
    rh2t2 = ObjectProperty(None)
    rh2t3 = ObjectProperty(None)
    n = ObjectProperty(None)

    k = NumericProperty(0)




    def systemsolver(self):
        try:
            global a1e
            global a2e
            global b1e
            global b2e
            global pe
            global fe
            global rne

            pe  = str(self.p.text)
            fe  = str(self.f.text)
            rne = str(self.rn.text)
            a1e = str(self.a1.text)
            a2e = str(self.a2.text)
            a3e = str(self.a3.text)
            b1e = str(self.b1.text)
            b2e = str(self.b2.text)
            b3e = str(self.b3.text)


            if pe == '':
                pe = sy.symbols('pe')
            else:
                pe  = str(self.p.text)

            if fe == '':
                fe = sy.symbols('fe')
            else:
                fe  = str(self.f.text)


            if rne == '':
                rne = sy.symbols('rne')
            else:
                rne  = str(self.rn.text)

            if a1e == '':
                a1e = sy.symbols('a1e')
            else:
                a1e  = str(self.a1.text)

            if a2e == '':
                a2e = sy.symbols('a2e')
            else:
                a2e  = str(self.a2.text)

            if b1e == '':
                b1e = sy.symbols('b1e')
            else:
                b1e  = str(self.b1.text)

            if b2e == '':
                b2e = sy.symbols('b2e')
            else:
                b2e  = str(self.b2.text)

            X = pe,fe,rne,a1e,a2e,b1e,b2e


            X=list(X)


            i=0

            if str(X[i])!= 'pe':
                del X[i]
                pe = float(pe)
            else:
                X[i]== 'pe'
                i=i+1

            if str(X[i])!='fe':
                del X[i]
                fe = float(fe)
            else:
                X[i]=='fe'
                i=i+1

            if str(X[i])!='rne':
                del X[i]
                rne = float(rne)
            else:
                X[i]=='rne'
                i=i+1

            if str(X[i])!= 'a1e':
                del X[i]
                a1e = float(a1e)
            else:
                X[i]=='a1e'
                i=i+1


            if str(X[i])!='a2e':
                del X[i]
                a2e = float(a2e)
            else:
                X[i]=='a2e'
                i=i+1

            if str(X[i])!='b1e':
                del X[i]
                b1e = float(b1e)
            else:
                X[i]=='b1e'
                i=i+1


            if str(X[i])!='b2e':
                del X[i]
                b2e = float(b2e)
            else:
                X[i]!='b2e'
                i = i+1

            self.k = i
            
            # print(i)

            sys = sy.nsolve((a1e + 57.2955*(sy.atan(-((pe / 2) - 1 + rne) / fe)),
                a2e- 57.2955*(sy.atan(((pe / 2)+1-rne) / fe)),
                b1e - 57.2955*(sy.atan(((pe / 2) + rne) / fe)),
                b2e + 57.2955*(sy.atan(-((pe / 2) - rne) / fe))),X,(1,1,1,1))

            
            r=0
            if str(self.p.text)=='':
                pe = str(round(sys[r],3))
                r=r+1
            else :
                pe = str(self.p.text)

            if str(self.f.text)=='':
                fe = str(round(sys[r],3))
                r=r+1
            else :
                fe = str(self.f.text)

            if str(self.rn.text)=='':
                rne = str(round(sys[r],3))
                r=r+1
            else :
                rne = str(self.rn.text)

            if str(self.a1.text)=='':
                a1e = str(round(sys[r],3))
                r=r+1
            else :
                a1e = str(self.a1.text)

            if str(self.a2.text)=='':
                a2e = str(round(sys[r],3))
                r=r+1
            else :
                a2e = str(self.a2.text)

            if str(self.b1.text)=='':
                b1e = str(round(sys[r],3))
                r=r+1
            else :
                b1e = str(self.b1.text)

            if str(self.b2.text)=='':
                b2e = str(round(sys[r],3))
                r=r+1
            else :
                b2e = str(self.b2.text)


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
            if i > 4:
                self.popup = firstPopup()
                self.k = 0  # mia allh timh oxi 4 gia na mhn allazei window
            else:
                self.popup = secondPopup()
                self.k = 0

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



    def dml(self):
        D1e = str(self.d1.text)
        D2e = str(self.d2.text)
        D3e = str(self.d3.text)
        Rh1e = str(self.rh2t1.text)
        Rh2e = str(self.rh2t2.text)
        Rh3e = str(self.rh2t3.text)
        Ne = str(self.n.text)


        self.rt = float(D1e)/2
        self.rh = float(Rh1e)*float(D1e)/2
        rti = self.rt
        rhi = self.rh
        self.rm = (rti+rhi)/2

        self.Um = 0.01666666 * float(Ne) * self.rm
        Umi = self.Um

        self.Uh = 0.01666666 * float(Ne) * self.rh
        Uhi = self.Uh

        self.Ut = 0.01666666 * float(Ne) * self.rt
        Uti = self.Ut

        self.Vx = float(fe)*Umi
        Vxi = self.Vx

        self.V1 = Vxi/m.cos(float(a1e))
        self.V2 = Vxi/m.cos(float(a2e))
        self.W1 = Vxi / m.cos(float(b1e))
        self.W2 = Vxi / m.cos(float(b2e))

        self.manager.get_screen('new').UmText = str(round(self.Um,3))
        self.manager.get_screen('new').UhText = str(round(self.Uh,3))
        self.manager.get_screen('new').UtText = str(round(self.Ut,3))
        self.manager.get_screen('new').VxText = str(round(self.Vx,3))
        self.manager.get_screen('new').V1Text = str(round(self.V1, 3))
        self.manager.get_screen('new').V2Text = str(round(self.V2, 3))
        self.manager.get_screen('new').W1Text = str(round(self.W1, 3))
        self.manager.get_screen('new').W2Text = str(round(self.W2, 3))

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

    UmText = StringProperty('0')
    UtText = StringProperty('0')
    UhText = StringProperty('0')
    VxText = StringProperty('0')
    V1Text = StringProperty('0')
    V2Text = StringProperty('0')
    W1Text = StringProperty('0')
    W2Text = StringProperty('0')

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