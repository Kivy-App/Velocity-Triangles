from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFillRoundFlatButton

def error_Popup():
    # show = P()
    #create content for the Popup
    bl = BoxLayout(orientation='vertical',padding = 30)
    label = Label(text ='This combination of non dimensional \n'\
                        'input has infinite solutions. Please \n'\
                        'fill in one more coefficient or angle ',halign = 'center',
                  valign = 'middle', color =[1, 1, 1, 1],font_size = '18dp')

    bl.add_widget(label)

    popupWindow = Popup(title="ERROR",title_color=[1,0,0,1],title_size = '25dp',separator_color=[1,0.4,0,1], content=bl,
                        size_hint=(None, None), size=('350dp','350dp'))

    btn = MDFillRoundFlatButton(text='OK got it !!!',
                                size_hint=(0.7,0.3), pos_hint={'center_x': 0.5}, on_release = popupWindow.dismiss)

    bl.add_widget(btn)
    popupWindow.open()


class P(BoxLayout):

    pass


def firstPopup():
    show = P()
    #create content for the Popup
    bl = BoxLayout(orientation='vertical',padding = 30)
    label = Label(text = 'You should put exactly 3 \n variables at the first segment',halign = 'center',
                  valign = 'middle', color =[1, 1, 1, 1],font_size = '18dp')
    bl.add_widget(label)

    popupWindow = Popup(title="ERROR",title_color=[1,0,0,1],title_size = '25dp',separator_color= [1,0.4,0,1], content= bl,
                        size_hint=(None, None), size=('350dp' ,'350dp'))

    btn = MDFillRoundFlatButton(text='OK got it !!!',
                               size_hint=(0.7,0.3), pos_hint={'center_x': 0.5}, on_release = popupWindow.dismiss)

    bl.add_widget(btn)
    popupWindow.open()

class P2(BoxLayout):
    pass

def secondPopup():
    show = P2()
    # create content for the Popup
    bl = BoxLayout(orientation='vertical',padding = 30)
    label = Label(text = '  This combination of variables\n'
                         '  is   not  valid.   \u03B11   has  to   be \n'
                         '  greater  than  \u03B21  and \u03B12  has \n'
                         '  to be greater than \u03B22. Please\n'
                         '  try  again with new  variables',halign = 'center',valign = 'middle', color =[1,1,1,1],font_size = '18dp')

    bl.add_widget(label)
    popupWindow = Popup(title="ERROR", title_color=[1, 0, 0, 1], title_size='25dp', separator_color=[1, 0.4, 0, 1],
                        content=bl,
                        size_hint=(None, None), size=('350dp', '350dp'))

    btn = MDFillRoundFlatButton(text='OK got it !!!', text_color=[0.5, 1, 1, 1],
                                size_hint=(0.7, 0.3), pos_hint={'center_x': 0.5}, on_release=popupWindow.dismiss)

    bl.add_widget(btn)
    popupWindow.open()

class P3(BoxLayout):
    pass

def thirdPopup():
    show = P3()
    # create content for the Popup
    bl = BoxLayout(orientation='vertical',padding=30)
    label = Label(text = ' Dimensional measurements \n missing. Please fill all the \n required measurements.',halign ='center',valign = 'middle', color =[1, 1, 1, 1],font_size = '18dp')

    bl.add_widget(label)
    popupWindow = Popup(title="ERROR", title_color=[1, 0, 0, 1], title_size='25dp', separator_color=[1, 0.4, 0, 1],
                        content=bl,
                        size_hint=(None, None), size=('350dp', '350dp'))

    btn = MDFillRoundFlatButton(text='OK got it !!!',
                                size_hint=(0.7, 0.3), pos_hint={'center_x': 0.5}, on_release=popupWindow.dismiss)

    bl.add_widget(btn)
    popupWindow.open()

class P4(BoxLayout):
    pass

class Prpm(BoxLayout):
    pass

def rpmPopup():
    show = Prpm()
    # create content for the Popup
    bl = BoxLayout(orientation='vertical',padding = 30)
    label = Label(text = ' Revoloutions per minute have \n to be positive number. Please \n try  again with  a positive value.' ,halign = 'center',valign = 'middle', color =[1, 1, 1, 1],font_size = '18dp')

    bl.add_widget(label)
    popupWindow = Popup(title="ERROR", title_color=[1, 0, 0, 1], title_size='25dp', separator_color=[1, 0.4, 0, 1],
                    content=bl,
                    size_hint=(None, None), size=('350dp', '350dp'))

    btn = MDFillRoundFlatButton(text='OK got it !!!',
                            size_hint=(0.7, 0.3), pos_hint={'center_x': 0.5}, on_release=popupWindow.dismiss)

    bl.add_widget(btn)
    popupWindow.open()

class Ph2t(BoxLayout):
    pass

def h2tPopup():
    show = Ph2t()
    # create content for the Popup
    bl = BoxLayout(orientation='vertical',padding = 30)
    label = Label(text = ' Hub to tip ratio has to be positive \n number and less than one.Please \n try again with  a valid value.' ,halign = 'center',valign = 'middle', color =[1, 1, 1, 1],font_size = '18dp')

    bl.add_widget(label)
    popupWindow = Popup(title="ERROR", title_color=[1, 0, 0, 1], title_size='25dp', separator_color=[1, 0.4, 0, 1],
                        content=bl,
                        size_hint=(None, None), size=('350dp', '350dp'))

    btn = MDFillRoundFlatButton(text='OK got it !!!',
                                size_hint=(0.7, 0.3), pos_hint={'center_x': 0.5}, on_release=popupWindow.dismiss)

    bl.add_widget(btn)
    popupWindow.open()

class Pdiam(BoxLayout):
    pass

def diamPopup():
    show = Pdiam()
    # create content for the Popup
    bl = BoxLayout(orientation='vertical',padding = 30)
    label = Label(text = ' Diameter  has to be positive number. \n Please try again with a positive value' ,halign = 'center',valign = 'middle', color =[1, 1, 1, 1],font_size = '18dp')

    bl.add_widget(label)
    popupWindow = Popup(title="ERROR", title_color=[1, 0, 0, 1], title_size='25dp', separator_color=[1, 0.4, 0, 1],
                        content=bl,
                        size_hint=(None, None), size=('350dp', '350dp'))

    btn = MDFillRoundFlatButton(text='OK got it !!!',
                                size_hint=(0.7, 0.3), pos_hint={'center_x': 0.5}, on_release=popupWindow.dismiss)

    bl.add_widget(btn)
    popupWindow.open()