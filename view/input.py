from view.display import Display
import pandas as pd

class Input:
    """
    A class to manage user inputs and provide interactive menus and prompts.

    This class provides static methods to interact with the user, offering
    options, capturing, and validating inputs for various functionalities
    like choosing options from the main menu and entering details for a travel record.

    Methods
    -------
    get_user_choice():
        Displays the main menu and validates the user's choice of action.
    get_record_details():
        Captures and validates the user's input for creating/editing a travel record.
    """

    @staticmethod
    def get_user_choice():
        """
        Displays the main menu and validates the user's choice of action.

        Returns
        -------
        choice : str
            A string representing the user's validated choice from the main menu.
        """
        print("\nOptions:")
        print("1. Reload data from Database")
        print("2. Save data to a new Database")
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
        """
        Captures and validates the user's input for creating/editing a travel record.

        Utilizes helper functions to validate float and date inputs and ensures
        that the user provides inputs in the expected format.

        Returns
        -------
        details : dict
            A dictionary containing validated inputs for a travel record.
        """
        # Validate float inputs with a function
        def get_float_input(prompt):
            """
            Validates and captures a float input from the user.

            Parameters
            ----------
            prompt : str
                The message displayed to the user when requesting input.

            Returns
            -------
            float
                A validated float value provided by the user.
            """
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
