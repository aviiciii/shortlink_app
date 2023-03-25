import kivy 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget


# API 
import requests
from dotenv import load_dotenv
import os
load_dotenv()
import json

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 1

        self.input_form = GridLayout()

        self.input_form.cols = 2



        self.input_form.add_widget(Label(text="Long Url: ", font_size=36))
        self.long_url = TextInput(multiline=False)
        self.input_form.add_widget(self.long_url)

        self.input_form.add_widget(Label(text="Short Url: ", font_size=46))
        self.slug = TextInput(multiline=False)
        self.input_form.add_widget(self.slug)

        self.add_widget(self.input_form)

        self.shorten_button = Button(text="Shorten", font_size=40)
        self.shorten_button.bind(on_press=self.shorten)
        self.add_widget(self.shorten_button)

        self.message = Label(text="", font_size=40)
        self.add_widget(self.message)

    def shorten(self, instance):
        print("Button pressed!!")
        long_url = self.long_url.text
        slug = self.slug.text

        print(long_url, type(long_url))
        print(slug, type(slug))


        if slug:
            print("Slug is not empty")
            pass
        else:
            print("Slug is empty")

            # API call 
            url = "https://api.short.io/links/lnk_2MIx_9dCPkouo4fY"
            payload = json.dumps({"allowDuplicates": False, "domain": "we.laavesh.ml", "originalURL": long_url })
            headers = {
                'accept': "application/json",
                'content-type': "application/json",
                'authorization': os.getenv("API_KEY")
            }

            response = requests.request("POST", url, data=payload, headers=headers)

            res = json.dumps(response.json(), indent=4) 
            print(res)




        short_url = "https://we.laavesh.ml/" + slug

        self.add_widget(Label(text=f"Shortened!", font_size=20))

class HelloApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    HelloApp().run()