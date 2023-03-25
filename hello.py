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

        # Input form
        self.input_form = GridLayout()
        self.input_form.cols = 2

        # Input - Long Url
        self.input_form.add_widget(Label(text="Long Url: ", font_size=36))
        self.long_url = TextInput(multiline=False)
        self.input_form.add_widget(self.long_url)

        # Input - Slug
        self.input_form.add_widget(Label(text="Short Url: ", font_size=46))
        self.slug = TextInput(multiline=False)
        self.input_form.add_widget(self.slug)

        # Add input form to main layout
        self.add_widget(self.input_form)


        # Shorten button
        self.shorten_button = Button(text="Shorten", font_size=40)
        self.shorten_button.bind(on_press=self.shorten)
        self.add_widget(self.shorten_button)

        # Message area
        self.message = Label(text="we.laavesh.ml", font_size=40)
        self.add_widget(self.message)


    # Shorten Api call function
    def shorten(self, instance):
        print("Button pressed!!")
        # Get input values
        long_url = self.long_url.text
        slug = self.slug.text

        # add https:// if not present
        if long_url[:8] != "https://":
            long_url = "https://" + long_url

        # Check if slug is given
        if slug:
            print("Slug present")
            pass
        else:
            print("Slug absent")

            # API call to we.laavesh.ml
            url = "https://api.short.io/links/lnk_2MIx_9dCPkouo4fY"
            payload = json.dumps({"allowDuplicates": False, "domain": "we.laavesh.ml", "originalURL": long_url })
            headers = {
                'accept': "application/json",
                'content-type': "application/json",
                'authorization': os.getenv("API_KEY")
            }

            # call api
            response = requests.request("POST", url, data=payload, headers=headers)
            # response
            res = json.dumps(response.json(), indent=4)
            res = json.loads(res)

            print(type(res))
            print(res["originalURL"], long_url)
            if res["originalURL"] == long_url:
                print("Updated! we.laavesh.ml")

            # clear input fields
            self.long_url.text = ""
            self.slug.text = ""

            # update message
            self.message.text = "we.laavesh.ml \n Updated!"

class HelloApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == '__main__':
    HelloApp().run()