from kivy.app import App
from kivy.uix.label import Label

class MinhaApp (App):
    def build(self):
        return Label(text="Olá senai!", font_size=100, font_name='arial',
             halign='left',
             valign='top'
        )
if __name__ == "__main__":
     MinhaApp().run()
    