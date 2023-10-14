from model.data_manager import DataManager
from model.record import Record
from view.display import Display
from view.input import Input
import pandas as pd
import os

class MainController:
    def __init__(self):
        self.data_manager = DataManager()
        self.display = Display()
        self.input = Input()
        self.records = []

    def run(self):
        self.load_data_from_csv()
        while True:
            self.display.display_message("Welcome to the Travel Records Management System!")
            user_choice = self.input.get_user_choice()
            if user_choice == "1":
                self.load_data_from_csv()
            elif user_choice == "2":
                self.save_data_to_csv()
            elif user_choice == "3":
                self.display_records()
            elif user_choice == "4":
                self.create_record()
            elif user_choice == "5":
                self.edit_record()
            elif user_choice == "6":
                self.delete_record()
            elif user_choice == "7":
                self.display.display_message("Exiting the application. Goodbye!")
                break
            else:
                self.display.display_error_message("Invalid choice. Please try again.")
                
            input("Press Enter to continue...")  # Wait for user input before clearing the screen
            os.system('cls' if os.name == 'nt' else 'clear')  # Clearing the screen

    def load_data_from_csv(self):
        try:
            self.records = self.data_manager.read_csv_data()
            self.display.display_message("Data loaded successfully from CSV.")
        except Exception as e:
            self.display.display_error_message(str(e))

    def save_data_to_csv(self):
        try:
            data = {
                'ref_number': [record.ref_number for record in self.records],
                'title_en': [record.title_en for record in self.records],
                'purpose_en': [record.purpose_en for record in self.records],
                'start_date': [record.start_date for record in self.records],
                'end_date': [record.end_date for record in self.records],
                'airfare': [record.airfare for record in self.records],
                'other_transport': [record.other_transport for record in self.records],
                'lodging': [record.lodging for record in self.records],
                'meals': [record.meals for record in self.records],
                'other_expenses': [record.other_expenses for record in self.records],
                'total': [record.total for record in self.records]
            }
            df = pd.DataFrame(data)
            df.to_csv('saved_travel_data.csv', index=False)
            self.display.display_message("Data saved successfully to 'saved_travel_data.csv'.")
        except Exception as e:
            self.display.display_error_message(f"Error saving data to CSV: {str(e)}")

    def display_records(self):
        """
        Display all or one record.
        """
        if self.records:
            print("Options:")
            print("1. Display all records")
            print("2. Display a single record")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.display.display_records(self.records)
            elif choice == "2":
                ref_number_to_display = input("Enter the reference number of the record to display: ")
                record_to_display = next((record for record in self.records if record.ref_number == ref_number_to_display), None)
                if record_to_display:
                    self.display.display_single_record(record_to_display)
                else:
                    self.display.display_error_message("Record not found.")
            else:
                self.display.display_error_message("Invalid choice. Please try again.")
        else:
            self.display.display_message("No records to display.")
            
            
    def create_record(self):
        try:
            details = self.input.get_record_details()
            new_record = Record(**details)
            self.records.append(new_record)
            self.display.display_message("Record created successfully.")
        except Exception as e:
            self.display.display_error_message(f"Error creating record: {str(e)}")

    def edit_record(self):
        try:
            ref_number_to_edit = input("Enter the reference number of the record to edit: ")
            record_to_edit = next((record for record in self.records if record.ref_number == ref_number_to_edit), None)
            if record_to_edit:
                details = self.input.get_record_details()
                for attr, value in details.items():
                    setattr(record_to_edit, attr, value)
                self.display.display_message("Record edited successfully.")
            else:
                self.display.display_error_message("Record not found.")
        except Exception as e:
            self.display.display_error_message(f"Error editing record: {str(e)}")

    def delete_record(self):
        try:
            ref_number_to_delete = input("Enter the reference number of the record to delete: ")
            record_to_delete = next((record for record in self.records if record.ref_number == ref_number_to_delete), None)
            if record_to_delete:
                self.records.remove(record_to_delete)
                self.display.display_message("Record deleted successfully.")
            else:
                self.display.display_error_message("Record not found.")
        except Exception as e:
            self.display.display_error_message(f"Error deleting record: {str(e)}")