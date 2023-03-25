import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text="Long Url: ", font_size=36))
        self.long_url = TextInput(multiline=False)
        self.add_widget(self.long_url)

        self.add_widget(Label(text="Short Url: ", font_size=46))
        self.slug = TextInput(multiline=False)
        self.add_widget(self.slug)

        self.shorten_button = Button(text="Shorten", font_size=40)
        self.shorten_button.bind(on_press=self.shorten)
        self.add_widget(self.shorten_button)

    def shorten(self, instance):
        print("Button pressed!!")
        long_url = self.long_url.text
        slug = self.slug.text


        



        short_url = "https://link.laavesh.ml/" + slug

        self.add_widget(Label(text=f"Shortened: {short_url}", font_size=20))

class HelloApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    HelloApp().run()