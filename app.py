from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooser


class MyApp(App):
    def build(self):
        # create a layout and add a text input and button widget to it that binds to write_to_file function
        self.layout = FloatLayout()
        self.text_input = TextInput(pos_hint={'center_x': 0.5, 'center_y': 0.5},size_hint=(.8,.1), font_size=20, halign="center")
        self.button = Button(text="Confirm", pos_hint={'center_x': 0.5, 'center_y': 0.3},size_hint=(.3,.1))
        self.button.bind(on_release=self.write_to_file)
        self.layout.add_widget(self.text_input)
        self.layout.add_widget(self.button)
        # create another button and widget that binds to file_chooser function
        # this button will open a file chooser popup to choose a file to write to
        self.file_chooser_button = Button(text="Choose File", pos_hint={'center_x': 0.5, 'center_y': 0.1},size_hint=(.3,.1))
        self.file_chooser_button.bind(on_release=lambda x: self.file_chooser())
        self.layout.add_widget(self.file_chooser_button)

                
        return self.layout
   
    def file_chooser(self):
        self.file_chooser = FileChooser()
        self.file_chooser.bind(on_submit=lambda path, filename: self.handle_file_chooser_submit(path, filename))
        self.layout.add_widget(self.file_chooser)
        
       
        
    def handle_file_chooser_submit(self, path, filename):
            # code here to handle the selected file
            self.write_to_file(path, filename)

    

    def write_to_file(self, instance):
        input_text = self.text_input.text
        file_path = self.file_chooser.path
        if not file_path:
            return None
        markdown_file = open(file_path, "a")
        markdown_file.write("- [ ] " + input_text + "\n")
        markdown_file.close()
        




if __name__ == "__main__":
    MyApp().run()

