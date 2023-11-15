from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout

class NewPatientScreen(Screen):
    def save_patient(self, name, birth_date, sex):
        # Save the patient data to your database
        pass
