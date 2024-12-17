from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class TestApp(App):
    def build(self):
        # Hauptlayout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Label
        self.label = Label(text="Hallo, Kivy!", font_size=24)
        layout.add_widget(self.label)

        # Button
        button = Button(text="Klicke mich!", font_size=20, size_hint=(1, 0.3))
        button.bind(on_press=self.on_button_press)
        layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        self.label.text = "Button wurde geklickt!"


# App starten
if __name__ == '__main__':
    TestApp().run()
