import bcrypt
import kivy

import pyperclip

kivy.require('2.3.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from storage_db import add_data, delete_data, app_exists, get_password, get_key
from signup_db import signup, get_masterhash, email_exists
from hashing import hash_masterpwd
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
        if not email or not pwd:  # Check if either email or password is empty
            self.manager.current = 'wronglog'
            return
        try:
            stored_password_hash = get_masterhash(email)
            if stored_password_hash is not None and bcrypt.checkpw(pwd.encode(), stored_password_hash.encode()):
                print("Logged in successfully")
                self.manager.current = 'main'
                self.ids.email.text = ''
                self.ids.password.text = ''
            else:
                print("Wrong email or password")
                self.manager.current = 'wronglog'
        except Exception as e:
            print("An unexpected error occurred:", e)


class RegisterPage(Screen):
    def add_to_signup_db(self):
        email = self.ids.email.text
        masterpwd = self.ids.masterpwd.text
        if email_exists(email):
            self.manager.current = 'wrongreg'

        else:
            hashed_masterpwd, salt = hash_masterpwd(masterpwd)
            signup(email, hashed_masterpwd, salt)
            self.manager.current = 'reggood'


class RegisteredGoodPage(Screen):
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
                add_data(app_name, email, encrypted_pwd, key)
                self.manager.current = 'addgood'
                self.ids.app_name.text = ''
                self.ids.email.text = ''
                self.ids.password.text = ''

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
        try:
            if app_exists(app_name):
                delete_data(app_name)
                self.manager.current = 'deletegood'
            else:
                self.manager.current = 'deletewrong'
        except Exception as e:
            print("An unexpected error occurred:", e)

class FetchPage(Screen):
    def fetch_from_db(self):
        app_name = self.ids.app_name.text

        if not app_name:
            self.manager.current = 'fetchbad'
            return
        try:
            key = get_key(app_name)
            cipher = initialize_cipher(key)
            encrypted_password = get_password(app_name)

            if encrypted_password:
                decrypted_password = decrypt(cipher, encrypted_password)
                if decrypted_password:
                    pyperclip.copy(decrypted_password)
                    self.manager.current = 'fetchgood'
                else:
                    self.manager.current = 'fetchbad'
            else:
                self.manager.current = 'fetchbad'
        except Exception as e:
            print("An unexpected error occurred:", e)
            self.manager.current = 'fetchbad'

class WrongLogPage(Screen):
    pass


class WrongRegPage(Screen):
    pass


class DeleteGoodPage(Screen):
    pass


class AddDataGoodPage(Screen):
    pass


class DeleteWrongPage(Screen):
    pass


class FetchGoodPage(Screen):
    pass


class FetchBadPage(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class CriptiqueApp(App):
    def build(self):
        return kv


kv = Builder.load_file('criptique.kv')

if __name__ == "__main__":
    CriptiqueApp().run()
