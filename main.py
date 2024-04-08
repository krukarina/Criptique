import kivy

kivy.require('2.3.0')
import os
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from database import add_data
# Set configuration
Config.set('graphics', 'width', '720dp')
Config.set('graphics', 'height', '1080dp')

Window.clearcolor = "#f2f1ec"


# Define different screens
class View(Screen):
    pass


class GreetPage(Screen):
    pass


class LoginPage(Screen):
    pass


class RegisterPage(Screen):
    pass


class RegfinishPage(Screen):
    pass


class MainPage(Screen):
    pass


class AddPage(Screen):
    def add_data_to_db(self):
        login = self.ids.login.text
        password = self.ids.password.text
        app_name = self.ids.app_name.text

        add_data(login, password, app_name)


class ShowPage(Screen):
    def fetch_from_db(self):
        login = self.ids.login.text
        password = self.ids.password.text
        app_name = self.ids.app_name.text

        add_data(login, password, app_name)


class EditPage(Screen):
    pass


class SearchPage(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class CriptiqueApp(App):
    def build(self):
        return kv


kv = Builder.load_file('criptique.kv')

if __name__ == "__main__":
    CriptiqueApp().run()
