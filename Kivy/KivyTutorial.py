

#       //  First simple window  //
"""
import kivy
from kivy.app import App
from kivy.uix.label import Label


class IanApp(App):
    def build(self):
        return Label(text= 'My first app')


if __name__ == "__main__":
    IanApp().run()

"""
#///////////////////////////////


#       // Labels Input and GUI layout  //

"""

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput




class MyApp(App):
    def build(self):
       return MyGrid()



class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Name: ")) 
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)  # Adding the text input box

        self.add_widget(Label(text="Last Name: "))
        self.lastname = TextInput(multiline=False)
        self.add_widget(self.lastname)

        self.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)



if __name__ == "__main__":
    MyApp().run()


"""
#/////////////////////////////////

#       // Buttons  //


"""
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
"""


"""

class MyApp(App):
    def build(self):
       return MyGrid()



class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Name: ")) 
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)  # Adding the text input box

        self.add_widget(Label(text="Last Name: "))
        self.lastname = TextInput(multiline=False)
        self.add_widget(self.lastname)

        self.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)

        self.submit = Button(text="Submit", font_size=40)
        self.add_widget(self.submit)

if __name__ == "__main__":
    MyApp().run()


"""
#--------------------------------------------------------
"""
class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1  # Set columns for main layout

        self.inside = GridLayout()  # Create a new grid layout
        self.inside.cols = 2  # set columns for the new grid layout

        # Create two diferent grids __ inside and outside

        self.inside.add_widget(Label(text="First Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        #-------------------------------------------------

        self.add_widget(self.inside)  # Add the interior layout to the main
        self.submit = Button(text="Submit", font_size=40)  # Creates second element as all the other elements will be counted as one 
        self.add_widget(self.submit)


    def pressed(self, instance):
        name = self.name.text
        last = self.lastName.text
        email = self.email.text

        print("Name:", name, "Last Name:", last, "Email:", email)
        self.name.text = ""
        self.lastName.text = ""
        self.email.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()





"""

#------------------------------------------------

"""

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="First Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)

        self.nice = Button(text="nice", font_size=40)  #creating nice button 
        self.nice.bind(on_press=self.nicego)   #creating action that can be called
        self.add_widget(self.submit)
        self.add_widget(self.nice)              #adding nice button

    
    def pressed(self, instance):  
        name = self.name.text
        last = self.lastName.text
        email = self.email.text

        print("Name:", name, "Last Name:", last, "Email:", email)
        self.name.text = ""
        self.lastName.text = ""
        self.email.text = ""
    

    def nicego(self, instance):   #action that will be executed when nice is called
        #name = self.name.text           #makes key get presed
        print('nice')




class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()

"""
#/////////////////////////////////////////////////////





#       // The kv Design Language //

#uses the kivy language to make the UI and uses the code as the way to manage data...  
"""

from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    name = ObjectProperty(None)      #  Creates a object propertie for the input...
    email = ObjectProperty(None)
    
    def btn(self):
        print("Name: ", self.name.text, 'email: ', self.email.text)



class MyApp(App):       #looks at class name and looks to a kv file with that name
    def build(self):
        return MyGrid()


if __name__ =='__main__':  
    MyApp().run()

"""
#////////////////////////////////////////////////////////////////////////









#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==


#       //  FloatLayout for Dynamic Placement  //
"""


import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class floatApp(App):
    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    floatApp().run()



"""
#////////////////////////////////////////////////////////////////////


#       //  Touch Input/Mouse Input  //
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty



class Touch(Widget):
    btn = ObjectProperty(None)

    
    #def on_touch_down(self, touch):
    #    print("Mouse Down", touch)
    #    self.btn.opacity = 0.5

    #def on_touch_move(self, touch):
    #    print("Mouse Move", touch)
    #

    def on_touch_up(self, touch):    #prints the relative and total position of the mouse
        print("Mouse UP", touch)
        self.btn.opacity = 1


class floatApp(App):
    def build(self):
        return Touch()


if __name__ == "__main__":
    floatApp().run()


"""

#////////////////////////////////////////////////////


#       // A simple Drawing app //
"""

from kivy.app import App
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.uix.widget import Widget
from kivy.graphics import Line


class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Line(points=(20, 30, 400, 500, 60, 500))     #it give the points of the line to draw and it will conect the dots
            Color(1, 0, 0, 0.5, mode="rgba")
            self.rect = Rectangle(pos=(0, 0), size=(50, 50)) 

    def on_touch_down(self, touch):
        self.rect.pos = touch.pos

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos

    def on_touch_down(self, touch):
        self.rect.pos = touch.pos

    def on_touch_move(self, touch):
        self.rect.pos = touch.pos

    def on_touch_down(self, touch):
        print("Mouse Down", touch)
        self.btn.opacity = 0.5

    def on_touch_move(self, touch):
        print("Mouse Move", touch)
    

    def on_touch_up(self, touch): 
        print("Mouse UP", touch)
        self.btn.opacity = 1

class floatApp(App):
    def build(self):
        return Touch()


if __name__ == "__main__":
    floatApp().run()


"""
#//////////////////////////////////////////////////////////////



from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(Screen):            #  The main widnow inherits the Screen class
    pass


class SecondWindow(Screen):
    pass


class ThirdWindow(Screen):
    print("you got to the third window")
    def pressed(self):
        print("nice")

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("main.kv")



class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()




















































#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
