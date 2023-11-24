from model.data_manager import DataManager
from model.record import Record
from view.display import Display
from view.input import Input
import pandas as pd
import os

class MainController:
    """
    A class to manage the main control flow of the Travel Records Management System.

    This class orchestrates the overall functionality of the application by
    interacting with data management, display, and input handling components.
    It provides methods to load and save data, display records, create, edit,
    and delete records, and manage the main user interaction loop.

    Attributes
    ----------
    data_manager : DataManager
        An instance of DataManager to handle data loading and saving.
    display : Display
        An instance of Display to manage the display of data and messages.
    input : Input
        An instance of Input to handle user inputs and interactions.
    records : list
        A list to store the travel records in memory.

    Methods
    -------
    run():
        Manages the main interaction loop, capturing user choices and executing corresponding actions.
    load_data_from_csv():
        Loads travel records from a CSV file into memory.
    save_data_to_csv():
        Saves the travel records from memory into a CSV file.
    display_records():
        Displays travel records to the user, offering options to display all or a single record.
    create_record():
        Captures user input to create a new travel record.
    edit_record():
        Captures user input to edit an existing travel record.
    delete_record():
        Deletes a travel record based on user input.
    """

    def __init__(self):
        self.data_manager = DataManager()
        self.display = Display()
        self.input = Input()
        self.records = []

    def run(self):
        """
        Manages the main interaction loop, capturing user choices and executing corresponding actions.

        The method provides a continuous loop, presenting the user with choices
        and executing the chosen action until the user decides to exit the application.
        """
        self.load_data_from_db()
        while True:
            self.display.display_message(
                "Welcome to the Travel Records Management System!")
            user_choice = self.input.get_user_choice()
            if user_choice == "1":
                self.load_data_from_db()
            elif user_choice == "2":
                self.save_data_to_db()
            elif user_choice == "3":
                self.display_records()
            elif user_choice == "4":
                self.create_record()
            elif user_choice == "5":
                self.edit_record()
            elif user_choice == "6":
                self.delete_record()
            elif user_choice == "7":
                self.sort_records()
            elif user_choice == "8":
                self.display.display_message(
                    "Exiting the application. Goodbye!")
                break
            else:
                self.display.display_error_message(
                    "Invalid choice. Please try again.")

            # Wait for user input before clearing the screen
            input("Press Enter to continue...")
            # Clearing the screen
            os.system('cls' if os.name == 'nt' else 'clear')

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
                ref_number_to_display = input(
                    "Enter the reference number of the record to display: ")
                record_to_display = next(
                    (record for record in self.records if record.ref_number == ref_number_to_display), None)
                if record_to_display:
                    self.display.display_single_record(record_to_display)
                else:
                    self.display.display_error_message("Record not found.")
            else:
                self.display.display_error_message(
                    "Invalid choice. Please try again.")
        else:
            self.display.display_message("No records to display.")

    def load_data_from_db(self):
        """
        Loads travel records from MongoDB into memory.
        """
        try:
            self.records = self.data_manager.read_data_from_db()
            self.display.display_message(
                "Data loaded successfully from the database.")
        except Exception as e:
            self.display.display_error_message(str(e))

    def save_data_to_db(self):
        """
        Saves the travel records from memory into MongoDB.
        """
        try:
            self.data_manager.save_records_to_db(self.records)
            self.display.display_message("Data saved successfully to the database.")
        except Exception as e:
            self.display.display_error_message(f"Error saving data to the database: {str(e)}")
            
    def create_record(self):
        """
        Captures user input to create a new travel record and saves it to the database.
        """
        try:
            details = self.input.get_record_details()
            new_record = Record(**details)
            self.data_manager.insert_record(new_record)
            self.display.display_message("Record created successfully.")
        except Exception as e:
            self.display.display_error_message(f"Error creating record: {str(e)}")

    def edit_record(self):
        """
        Captures user input to edit an existing travel record and updates it in the database.
        """
        try:
            ref_number_to_edit = input("Enter the reference number of the record to edit: ")
            updated_details = self.input.get_record_details()
            self.data_manager.update_record(ref_number_to_edit, updated_details)
            self.display.display_message("Record edited successfully.")
        except Exception as e:
            self.display.display_error_message(f"Error editing record: {str(e)}")

    def delete_record(self):
        """
        Deletes a travel record based on user input from the database.
        """
        try :
            ref_number_to_delete = input("Enter the reference number of the record to delete: ")
            self.data_manager.delete_record(ref_number_to_delete)
            self.display.display_message("Record deleted successfully.")
        except Exception as e:
            self.display.display_error_message(f"Error deleting record: {str(e)}")
            
    def sort_records(self):
        '''
        Handles the sorting of travel records based on user input.

        Prompts the user for sorting criteria and retrieves sorted records from the database.
        '''
        sort_criteria = self.input.get_sort_criteria()
        sorted_records = self.data_manager.get_sorted_records(sort_criteria)
        self.display.display_records(sorted_records)