from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.app import App  # Ensure to import App
from database.database import create_user

class SignupScreen(BoxLayout):
    error_message = StringProperty("")

    def signup(self, username, password, confirm_password):
        if password == confirm_password:
            create_user(username, password)
            self.error_message = ""
            App.get_running_app().root.current = 'login'
        else:
            self.error_message = "Passwords do not match!"
