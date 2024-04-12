import kivy
import os
import sys
import pyperclip

kivy.require('2.3.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from storage_db import add_data, delete_data
from signup_db import signup
from hashing import hash_masterpwd, checkpwd
from encyption import encrypt, decrypt, initialize_cipher, generate_key

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
    def login(self):
        email = self.ids.email.text
        pwd = self.ids.password.text
        if email.strip() == "" or pwd.strip() == "":
            print("Please, enter required data to proceed.")
            return
        else:
            try:
                stored_mpwd =
            except ValueError as ve:
                print("ValueError occurred:", ve)
            except TypeError as te:
                print("TypeError occurred:", te)
            except Exception as e:
                print("An unexpected error occurred:", e)


class RegisterPage(Screen):
    def add_to_signup_db(self):
        email = self.ids.email.text
        masterpwd = self.ids.masterpwd.text
        hashed_masterpwd, salt = hash_masterpwd(masterpwd)
        signup(email, hashed_masterpwd, salt)


class RegfinishPage(Screen):
    pass


class MainPage(Screen):
    pass


class AddPage(Screen):
    def add_to_storage_db(self):
        app_name = self.ids.app_name.text
        email = self.ids.email.text
        pwd = self.ids.password.text

        if email.strip() == "" or pwd.strip() == "":
            print("Please, enter required data to proceed.")
            return
        else:
            try:
                key = generate_key()
                cipher = initialize_cipher(key)
                encrypted_pwd = encrypt(cipher, pwd)
                add_data(app_name, email, encrypted_pwd)
                print("Password stored securely.")
            except ValueError as ve:
                print("ValueError occurred:", ve)
            except TypeError as te:
                print("TypeError occurred:", te)
            except Exception as e:
                print("An unexpected error occurred:", e)

class DeletePage(Screen):
    def delete_data_from_database(self):
        # Get the app_name from TextInput widget
        app_name = self.ids.app_name.text

        # Call delete_data function from the database module
        delete_data(app_name)


class ShowPage(Screen):
    def fetch_from_db(self):
        email = self.ids.email.text
        password = self.ids.password.text
        app_name = self.ids.app_name.text
        add_data(email, password, app_name)


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
