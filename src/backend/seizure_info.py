from kivy.uix.screenmanager import Screen

class SeizureInfoScreen(Screen):
    def get_patient_names(self):
        # Fetch and return a list of patient names from your database
        pass

    def save_seizure_info(self, patient_name, seizure_start, seizure_duration, seizure_type):
        # Save the seizure info to your database
        pass
