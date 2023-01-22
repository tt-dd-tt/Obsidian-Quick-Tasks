from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        self.layout = FloatLayout()
        self.text_input = TextInput(pos_hint={'center_x': 0.5, 'center_y': 0.5},size_hint=(.8,.1), font_size=20, halign="center")
        self.button = Button(text="Confirm", pos_hint={'center_x': 0.5, 'center_y': 0.3},size_hint=(.3,.1))
        self.button.bind(on_release=self.write_to_file)
        self.layout.add_widget(self.text_input)
        self.layout.add_widget(self.button)
        return self.layout

    def write_to_file(self, instance):
        input_text = self.text_input.text
        if input_text == "":
            self.text_input.text = "You didn't write anything!"
            return
        markdown_file = open("file.md", "a")
        markdown_file.write("- [ ] " + input_text + "\n")
        markdown_file.close()
        self.text_input.text = ""

if __name__ == "__main__":
    MyApp().run() 
