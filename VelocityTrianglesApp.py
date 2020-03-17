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



pe = None
l = None
class VelocityTriangles(Screen):
    global p
    p = ObjectProperty(None)
    def SetText(self):
        text =  str(self.p.text)
        self.manager.get_screen('new').labelText = text


class NewWindow(Screen):
	labelText = StringProperty('My Label')
    # def some1(self):
    #     ke = pe
    #     lk = Label(text= ke)
    #     self.add_widget(lk)




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





