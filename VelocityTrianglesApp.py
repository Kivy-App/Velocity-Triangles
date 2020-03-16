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


pe = None
l = None
class VelocityTriangles(Screen):
    global p
    p = ObjectProperty(None)
    def some(self):
        global pe
        pe = str(self.p.text)
        global l
        # l = Label(text=pe, pos_hint={'x': - 0.3, 'y': -0.3})


class NewWindow(Screen):
    def some1(self):
        ke = pe
        lk = Label(text= ke)
        self.add_widget(lk)




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