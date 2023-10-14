from view.display import Display
import pandas as pd

class Input:
    @staticmethod
    def get_user_choice():
        print("\nOptions:")
        print("1. Reload data from CSV")
        print("2. Save data to a new CSV")
        print("3. Display records")
        print("4. Create a new record")
        print("5. Edit a record")
        print("6. Delete a record")
        print("7. Exit")
        Display.display_creator_name()
        while True:
            choice = input("Enter your choice: ")
            if choice.isdigit() and 1 <= int(choice) <= 7:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

    @staticmethod
    def get_record_details():
        # Validate float inputs with a function
        def get_float_input(prompt):
            while True:
                try:
                    return float(input(prompt))
                except ValueError:
                    print("Invalid input. Please enter a number.")
        
        details = {}
        details['ref_number'] = input("Enter reference number: ")
        details['title_en'] = input("Enter title in English: ")
        details['purpose_en'] = input("Enter purpose of travel in English: ")  
        details['airfare'] = get_float_input("Enter cost of airfare: ")
        details['other_transport'] = get_float_input("Enter cost of other transportation: ")
        details['lodging'] = get_float_input("Enter cost of lodging: ")
        details['meals'] = get_float_input("Enter cost of meals: ")
        details['other_expenses'] = get_float_input("Enter cost of other expenses: ")
        details['total'] = get_float_input("Enter total cost: ")
        
        # Validate date format
        while True:
            details['start_date'] = input("Enter start date of travel (YYYY-MM-DD): ")
            try:
                pd.to_datetime(details['start_date'], format='%Y-%m-%d')
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        
        while True:
            details['end_date'] = input("Enter end date of travel (YYYY-MM-DD): ")
            try:
                pd.to_datetime(details['end_date'], format='%Y-%m-%d')
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        
        return details
